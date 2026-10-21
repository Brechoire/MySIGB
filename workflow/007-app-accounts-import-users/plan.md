# 007 — App accounts (comptes PMB users) + import Python multi-OS

## Demande

Créer une app `compte` reprenant la table PMB `users` pour la connexion :
mots de passe non repris (sécu + RGPD), super-compte admin qui réinitialise,
tous les champs importés (modèle documenté en français), bonnes pratiques
Django, script d'import Python (Windows + Linux).
Confirmé : nom code `accounts` (évite le clash avec PMB `comptes` financiers).

## Objectif

Socle d'authentification MySIGB : connexion, changement forcé au 1er login,
admin de réinitialisation, import idempotent et sec des 22 comptes staff.

## Todolist

- [x] TDD : tests d'abord (RED vu : modèle manquant, puis `timezone.utc`, puis encodage)
- [x] Modèles `Compte` (AbstractUser) + `Preferences` + signal, admin, middleware, vues/URLs/templates FR
- [x] Commande `import_pmb_users` (dry-run défaut, --apply, --rejets, sortie = comptes seuls)
- [x] Bugs réels corrigés en RED→GREEN : `timezone.utc` → `datetime.timezone.utc` ; décodage utf-8 → cp1252 → latin-1 (dump réel mixte)
- [x] Validation dump réel en dry-run : `lus=22 ... mode=dry-run` (0 écriture, 0 fuite)
- [x] Docs : MAPPING_IMPORT (ligne users), AGENTS.md (app + /comptes/)
- [x] Vérifier : `check` + `test` (24 tests)
- [ ] Rôles/groupes : mapper `users_roles*` + distribution des droits (observée : bitmask variés) — prochaine demande
- [ ] Emails agents pour reset par email (absents de PMB) — à décider
- [ ] Prochaine demande : créer `workflow/008-...` en incrémentant le numéro

## Fait

- `accounts/` : modèles (help_text FR + référence colonne PMB par champ),
  `AUTH_USER_MODEL`, `LANGUAGE_CODE='fr-fr'`, `LOGIN_*`, middleware de forçage,
  URLs `/comptes/` (connexion/déconnexion POST/mot-de-passe), nav header conditionnelle.
- `createsuperuser` pour le super-compte ; admin change mdp → re-forçage auto.
- Rulings : travail sur `main` (pratique repo, solo) ; prénoms/noms en 150 (standard
  Django, source 30 documentée) ; sortie commande = agrégats uniquement.

## Vérification

- `./env/bin/python manage.py test accounts` : 15/15 (modèle, commande, vues, admin).
- `./env/bin/python manage.py test` : 24/24 OK ; `check` : 0 problème.
- Dry-run réel : comptes seuls, aucune valeur personnelle remontée.
