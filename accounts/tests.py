"""Tests de l'app accounts (comptes de connexion repris de PMB `users`).

Conventions : noms en français, comportements réels, aucune donnée PMB réelle
(jeu de données fictif pour la commande d'import).
"""
import io
import tempfile
from pathlib import Path

from django.contrib import admin
from django.core.management import call_command
from django.db import IntegrityError
from django.test import TestCase, Client

DUMP_FICTIF = """-- MariaDB dump fictif
CREATE TABLE `users` (
  `userid` int(5) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL DEFAULT '',
  `pwd` varchar(50) NOT NULL DEFAULT '',
  `nom` varchar(30) NOT NULL DEFAULT '',
  `prenom` varchar(30) DEFAULT NULL,
  `rights` int(8) unsigned NOT NULL DEFAULT 0,
  `user_lang` varchar(5) NOT NULL DEFAULT 'fr_FR',
  `create_dt` date NOT NULL DEFAULT '2020-01-15',
  PRIMARY KEY (`userid`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3;
INSERT INTO `users` VALUES (1,'jdupont','ancien_hash','Dupont','Jeanne',16,'fr_FR','2020-01-15'),(2,'pmb_api','autre_hash','API','',4,'fr_FR','2021-06-01');
"""


def _ecrire_dump_fictif() -> Path:
    tmp = Path(tempfile.mkdtemp())
    chemin = tmp / "users_fictif.sql"
    chemin.write_text(DUMP_FICTIF, encoding="utf-8")
    return chemin


class CompteModeleTest(TestCase):
    def test_creation_avec_champs_pmb(self):
        from accounts.models import Compte
        compte = Compte.objects.create_user(
            username="jdupont",
            first_name="Jeanne",
            last_name="Dupont",
            langue="fr",
            legacy_userid=1,
            legacy_rights=16,
        )
        relu = Compte.objects.get(username="jdupont")
        self.assertEqual(relu.first_name, "Jeanne")
        self.assertEqual(relu.last_name, "Dupont")
        self.assertEqual(relu.legacy_userid, 1)
        self.assertEqual(relu.legacy_rights, 16)
        self.assertTrue(relu.force_password_change)
        self.assertFalse(relu.has_usable_password())

    def test_username_unique(self):
        from accounts.models import Compte
        Compte.objects.create_user(username="jdupont")
        with self.assertRaises(IntegrityError):
            Compte.objects.create_user(username="jdupont")

    def test_username_limite_a_100_caracteres(self):
        from accounts.models import Compte
        champ = Compte._meta.get_field("username")
        self.assertEqual(champ.max_length, 100)

    def test_preferences_creees_automatiquement(self):
        from accounts.models import Compte
        compte = Compte.objects.create_user(username="jdupont")
        self.assertIsNotNone(compte.preferences)
        self.assertEqual(compte.preferences.nb_per_page_search, 4)


class ImportPmbUsersTest(TestCase):
    def test_dry_run_par_defaut_necrit_rien(self):
        from accounts.models import Compte
        chemin = _ecrire_dump_fictif()
        sortie = io.StringIO()
        call_command("import_pmb_users", f"--source={chemin}", stdout=sortie)
        self.assertEqual(Compte.objects.count(), 0)
        self.assertIn("crees=0", sortie.getvalue())

    def test_apply_cree_les_comptes_sans_mot_de_passe_utilisable(self):
        from accounts.models import Compte
        chemin = _ecrire_dump_fictif()
        sortie = io.StringIO()
        call_command("import_pmb_users", f"--source={chemin}", "--apply", stdout=sortie)
        self.assertEqual(Compte.objects.count(), 2)
        jdupont = Compte.objects.get(username="jdupont")
        self.assertEqual(jdupont.first_name, "Jeanne")
        self.assertEqual(jdupont.legacy_userid, 1)
        self.assertFalse(jdupont.has_usable_password())
        self.assertTrue(jdupont.force_password_change)
        self.assertIn("crees=2", sortie.getvalue())

    def test_apply_est_idempotent(self):
        from accounts.models import Compte
        chemin = _ecrire_dump_fictif()
        call_command("import_pmb_users", f"--source={chemin}", "--apply", stdout=io.StringIO())
        sortie = io.StringIO()
        call_command("import_pmb_users", f"--source={chemin}", "--apply", stdout=sortie)
        self.assertEqual(Compte.objects.count(), 2)
        self.assertIn("crees=0", sortie.getvalue())

    def test_sortie_ne_contient_aucune_donnee_personnelle(self):
        chemin = _ecrire_dump_fictif()
        sortie = io.StringIO()
        call_command("import_pmb_users", f"--source={chemin}", "--apply", stdout=sortie)
        texte = sortie.getvalue()
        self.assertNotIn("jdupont", texte)
        self.assertNotIn("Dupont", texte)
        self.assertNotIn("ancien_hash", texte)

    def test_fichier_non_utf8_accent_fidelite(self):
        tmp = Path(tempfile.mkdtemp())
        chemin = tmp / "users_latin.sql"
        chemin.write_bytes(
            "CREATE TABLE `users` (\n"
            "  `userid` int(5) NOT NULL AUTO_INCREMENT,\n"
            "  `username` varchar(100) NOT NULL DEFAULT '',\n"
            "  PRIMARY KEY (`userid`)\n"
            ") ENGINE=MyISAM DEFAULT CHARSET=utf8mb3;\n".encode("utf-8")
            + b"INSERT INTO `users` VALUES (1,'caf\xe9');\n"
        )
        sortie = io.StringIO()
        call_command("import_pmb_users", f"--source={chemin}", "--apply", stdout=sortie)
        from accounts.models import Compte
        self.assertTrue(Compte.objects.filter(username="café").exists())

    def test_ligne_binaire_autre_table_ignoree_proprement(self):
        tmp = Path(tempfile.mkdtemp())
        chemin = tmp / "users_binaire.sql"
        chemin.write_bytes(
            b"INSERT INTO `autre` VALUES (1,'\x89\x9d binaire');\n"
            + "CREATE TABLE `users` (\n"
            "  `userid` int(5) NOT NULL AUTO_INCREMENT,\n"
            "  `username` varchar(100) NOT NULL DEFAULT '',\n"
            "  PRIMARY KEY (`userid`)\n"
            ") ENGINE=MyISAM DEFAULT CHARSET=utf8mb3;\n".encode("utf-8")
            + b"INSERT INTO `users` VALUES (1,'jdupont');\n"
        )
        sortie = io.StringIO()
        call_command("import_pmb_users", f"--source={chemin}", "--apply", stdout=sortie)
        from accounts.models import Compte
        self.assertTrue(Compte.objects.filter(username="jdupont").exists())
        self.assertIn("lus=1", sortie.getvalue())


class ConnexionVuesTest(TestCase):
    def test_page_connexion_repond_200(self):
        reponse = Client().get("/comptes/connexion/")
        self.assertEqual(reponse.status_code, 200)
        self.assertContains(reponse, "<fieldset>")

    def test_compte_force_doitchanger_son_mot_de_passe(self):
        from accounts.models import Compte
        compte = Compte.objects.create_user(username="jdupont", password="Secret123!")
        compte.force_password_change = True
        compte.save()
        client = Client()
        client.force_login(compte)
        reponse = client.get("/")
        self.assertRedirects(reponse, "/comptes/mot-de-passe/")

    def test_changement_mot_de_passe_leve_le_forcage(self):
        from accounts.models import Compte
        compte = Compte.objects.create_user(username="jdupont", password="Secret123!")
        compte.force_password_change = True
        compte.save()
        client = Client()
        client.force_login(compte)
        reponse = client.post("/comptes/mot-de-passe/", {
            "old_password": "Secret123!",
            "new_password1": "Nouveau-Secret456!",
            "new_password2": "Nouveau-Secret456!",
        })
        self.assertEqual(reponse.status_code, 302)
        compte.refresh_from_db()
        self.assertFalse(compte.force_password_change)

    def test_deconnexion_en_post(self):
        from accounts.models import Compte
        compte = Compte.objects.create_user(username="jdupont", password="Secret123!")
        compte.force_password_change = False
        compte.save()
        client = Client()
        client.force_login(compte)
        reponse = client.post("/comptes/deconnexion/")
        self.assertEqual(reponse.status_code, 302)


class CompteAdminTest(TestCase):
    def test_compte_enregistre_dans_ladmin(self):
        from accounts.models import Compte
        self.assertIn(Compte, admin.site._registry)
