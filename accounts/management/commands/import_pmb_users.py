"""Importe les comptes PMB ``users`` vers les ``Compte`` MySIGB.

Fonctionne sur Windows et Linux (Python + Django uniquement, aucun appel
système) : ``./env/bin/python manage.py import_pmb_users --source=...``
(Linux) ou ``env\\Scripts\\python.exe manage.py import_pmb_users --source=...``
(Windows).

Règles (confidentialité + sécurité) :
- les secrets PMB (``pwd``, ``user_digest``) ne sont JAMAIS importés ;
- chaque compte créé reçoit un mot de passe inutilisable et
  ``force_password_change=True`` (changement imposé au 1er login) ;
- la sortie n'affiche QUE des comptes (lus/créés/existants/rejetés) et la
  distribution des droits : jamais de noms, logins ni secrets ;
- par défaut : simulation (``--dry-run``), ``--apply`` pour écrire ;
- idempotent : rejouer ne crée aucun doublon (clé = ``legacy_userid``).
"""
import json
import re
from collections import Counter
from datetime import datetime, time, timezone as fuseau
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError
from django.db import models
from django.utils import timezone

from accounts.models import Compte, Preferences

TABLE = "users"
INSERT_PREFIX = f"INSERT INTO `{TABLE}`"
TAILLE_MAX_INSTRUCTION = 10_000_000  # borne anti-explosion (table users : minuscule)

# Colonne PMB -> champ du profil Preferences (si présente dans l'export).
CHAMPS_PREFERENCES = {
    "nb_per_page_search", "nb_per_page_select", "nb_per_page_gestion",
    "param_popup_ticket", "param_sounds", "param_rfid_activate",
    "param_chat_activate", "param_licence", "deflt_notice_statut",
    "deflt_notice_statut_analysis", "deflt_integration_notice_statut",
    "xmlta_indexation_lang", "deflt_docs_type", "deflt_serials_docs_type",
    "deflt_lenders", "deflt_styles", "deflt_docs_statut", "deflt_docs_codestat",
    "value_deflt_lang", "value_deflt_fonction", "value_deflt_relation",
    "value_deflt_relation_serial",
}


def decouper_valeurs(texte):
    """Découpe ``(a,'b',NULL,...)`` en valeurs Python (str/None/int).

    Gère quotes simples, '' échappé et backslash. Lève ValueError si
    le tuple est mal formé. Pur Python, multi-OS.
    """
    valeurs, i, n = [], 0, len(texte)
    while i < n:
        while i < n and texte[i] in " (, \t\r\n":
            i += 1
        if i >= n:
            break
        if texte[i] == ")":
            break
        if texte[i] == "'":
            i += 1
            tampon = []
            while i < n:
                c = texte[i]
                if c == "\\" and i + 1 < n:
                    tampon.append(texte[i + 1])
                    i += 2
                    continue
                if c == "'":
                    if i + 1 < n and texte[i + 1] == "'":
                        tampon.append("'")
                        i += 2
                        continue
                    i += 1
                    break
                tampon.append(c)
                i += 1
            else:
                raise ValueError("chaîne non terminée")
            valeurs.append("".join(tampon))
        else:
            j = i
            while j < n and texte[j] not in ",)":
                j += 1
            brut = texte[i:j].strip()
            if brut == "NULL":
                valeurs.append(None)
            elif re.fullmatch(r"-?\d+", brut):
                valeurs.append(int(brut))
            elif brut == "":
                raise ValueError("valeur vide")
            else:
                valeurs.append(brut)
            i = j
        while i < n and texte[i] in " \t\r\n":
            i += 1
        if i < n and texte[i] == ",":
            i += 1
    return valeurs


def colonnes_create(bloc):
    """Ordre des colonnes d'un bloc CREATE TABLE (lignes `` `nom` ...``)."""
    noms = []
    for ligne in bloc.splitlines():
        m = re.match(r"\s*`([^`]+)`\s+", ligne)
        if m:
            noms.append(m.group(1))
    return noms


def decode_robuste(brute):
    """Décode une ligne : utf-8 strict, sinon cp1252 (FR Windows), sinon latin-1.

    Retourne (texte, recodee) ; le latin-1 ne peut pas échouer (données
    binaires type BLOB des autres tables : préservées sans planter).
    """
    try:
        return brute.decode("utf-8"), False
    except UnicodeDecodeError:
        pass
    try:
        return brute.decode("cp1252"), True
    except UnicodeDecodeError:
        return brute.decode("latin-1"), True


def convertir_langue(valeur):
    """'fr_FR' -> 'fr' (Django utilise 'fr')."""
    if not valeur:
        return "fr"
    return valeur.split("_")[0].split("-")[0].lower() or "fr"


def convertir_date_reunion(valeur):
    """'2020-01-15' -> datetime UTC (minuit). None si vide/zéro."""
    if not valeur or valeur.startswith("0000"):
        return None
    try:
        jour = datetime.strptime(valeur[:10], "%Y-%m-%d").date()
    except ValueError:
        return None
    return timezone.make_aware(datetime.combine(jour, time.min), fuseau.utc)


class Command(BaseCommand):
    """Importe PMB ``users`` (simulation par défaut, ``--apply`` pour écrire)."""

    help = "Importe les comptes PMB (table users) : simulation par défaut, --apply pour écrire."

    def add_arguments(self, parser):
        parser.add_argument("--source", required=True, help="Chemin du dump PMB (.sql, local).")
        parser.add_argument("--apply", action="store_true", help="Écrit en base (défaut : simulation).")
        parser.add_argument("--rejets", default=None, help="Fichier local JSON des rejets (ligne + motif, sans valeurs).")

    def handle(self, *args, **options):
        chemin = Path(options["source"])
        if not chemin.is_file():
            raise CommandError(f"source introuvable : {chemin}")
        lignes = self._extraire_instructions(chemin)
        if not lignes["colonnes"]:
            raise CommandError("bloc CREATE TABLE `users` introuvable dans la source")
        resultat = self._importer(lignes, appliquer=options["apply"])
        self.stdout.write(
            "lus={lus} crees={crees} existants={existants} rejets={rejets} "
            "lignes_recodees={recodees} mode={mode}".format(
                mode="apply" if options["apply"] else "dry-run",
                recodees=lignes.get("recodees", 0),
                **resultat["compteurs"],
            )
        )
        distribution = " ".join(f"{k}:{v}" for k, v in sorted(resultat["droits"].items()))
        self.stdout.write(f"droits distincts (effectifs) : {distribution or 'aucun'}")
        if options["rejets"] and resultat["motifs"]:
            Path(options["rejets"]).write_text(
                json.dumps(resultat["motifs"], ensure_ascii=False, indent=1), encoding="utf-8"
            )
            self.stdout.write(f"rejets detailles dans {options['rejets']} (local, a ne pas committer)")

    def _extraire_instructions(self, chemin):
        colonnes, requetes, tampon, dans_create = [], [], [], False
        recodees = 0
        with open(chemin, "rb") as f:
            for brute in f:
                ligne = decode_robuste(brute)
                if ligne is None:
                    continue
                recodees += 1 if ligne[1] else 0
                ligne = ligne[0]
                if ligne.startswith(f"CREATE TABLE `{TABLE}`"):
                    dans_create, tampon = True, [ligne]
                    continue
                if dans_create:
                    tampon.append(ligne)
                    if ligne.rstrip().endswith(";"):
                        colonnes = colonnes_create("".join(tampon))
                        dans_create, tampon = False, []
                    continue
                if ligne.startswith(INSERT_PREFIX):
                    if len(ligne) > TAILLE_MAX_INSTRUCTION:
                        raise CommandError("instruction INSERT users trop volumineuse, abandon")
                    requetes.append(ligne)
        return {"colonnes": colonnes, "requetes": requetes, "recodees": recodees}

    def _importer(self, lignes, appliquer):
        compteurs = Counter(lus=0, crees=0, existants=0, rejets=0)
        droits, motifs = Counter(), []
        for requete in lignes["requetes"]:
            corps = requete[requete.find("VALUES") + len("VALUES"):]
            for morceau in self._decouper_requetes(corps):
                try:
                    valeurs = decouper_valeurs(morceau)
                except ValueError:
                    compteurs["rejets"] += 1
                    motifs.append({"motif": "tuple mal formé"})
                    continue
                if len(valeurs) != len(lignes["colonnes"]):
                    compteurs["rejets"] += 1
                    motifs.append({"motif": "nombre de colonnes inattendu"})
                    continue
                ligne = dict(zip(lignes["colonnes"], valeurs))
                compteurs["lus"] += 1
                droits[ligne.get("rights", 0)] += 1
                if appliquer:
                    etat = self._appliquer_ligne(ligne, motifs)
                    compteurs[etat] += 1
        return {"compteurs": compteurs, "droits": droits, "motifs": motifs}

    @staticmethod
    def _decouper_requetes(corps):
        """Découpe ``(...),(...) ;`` en tuples (parenthèses de premier niveau)."""
        morceaux, profondeur, debut, guillemet = [], 0, None, None
        i, n = 0, len(corps)
        while i < n:
            c = corps[i]
            if guillemet:
                if c == "\\" and i + 1 < n:
                    i += 2
                    continue
                if c == guillemet:
                    guillemet = None
                i += 1
                continue
            if c == "'":
                guillemet, i = c, i + 1
                continue
            if c == "(":
                if profondeur == 0:
                    debut = i
                profondeur += 1
            elif c == ")":
                profondeur -= 1
                if profondeur == 0 and debut is not None:
                    morceaux.append(corps[debut:i + 1])
                    debut = None
            elif c == ";" and profondeur == 0:
                break
            i += 1
        return morceaux

    @staticmethod
    def _appliquer_ligne(ligne, motifs):
        try:
            legacy = int(ligne["userid"])
        except (TypeError, ValueError):
            motifs.append({"motif": "userid invalide"})
            return "rejets"
        if Compte.objects.filter(legacy_userid=legacy).exists():
            return "existants"
        if Compte.objects.filter(username=ligne.get("username") or "").exists():
            motifs.append({"motif": "username déjà pris"})
            return "rejets"
        compte = Compte(
            username=ligne.get("username") or "",
            first_name=ligne.get("prenom") or "",
            last_name=ligne.get("nom") or "",
            langue=convertir_langue(ligne.get("user_lang")),
            legacy_userid=legacy,
            legacy_rights=int(ligne.get("rights") or 0),
            is_staff=True,
        )
        date_reunion = convertir_date_reunion(ligne.get("create_dt"))
        if date_reunion is not None:
            compte.date_joined = date_reunion
        compte.set_unusable_password()
        compte.save()  # crée aussi les préférences (signal)
        prefs = {k: ligne[k] for k in CHAMPS_PREFERENCES if k in ligne and ligne[k] not in (None, "")}
        for champ, valeur in prefs.items():
            champ_modele = Preferences._meta.get_field(champ)
            if isinstance(valeur, str) and not isinstance(
                champ_modele, (models.CharField, models.TextField)
            ):
                try:
                    valeur = int(valeur)
                except ValueError:
                    continue
            setattr(compte.preferences, champ, valeur)
        compte.preferences.save()
        return "crees"
