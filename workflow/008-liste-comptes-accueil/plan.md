# 008 — Liste des comptes sur la page d'accueil

## Demande

Afficher la liste des users sur la page d'accueil.

## Objectif

Rendre visibles les comptes enregistrés dès `/` (username + nom complet).

## Todolist

- [x] TDD : tests d'abord (RED vu : contenu absent), puis vue + template (GREEN)
- [x] `home/views.py` : `index` fournit `comptes` triés par username
- [x] Template : section « Comptes enregistrés », message si vide
- [x] Vérifier : `check` + `test` (28 tests)
- [ ] Prochaine demande : créer `workflow/009-...` en incrémentant le numéro

## Fait

- `home/tests.py` : 2 tests (liste + état vide).
- `home/templates/home/index.html` : section avec `get_full_name` conditionnel.
- Note : liste publique (accueil sans login) — assumé pour un outil interne ;
  à restreindre si l'ouverture change.

## Vérification

- `./env/bin/python manage.py test home` : 2/2 (après RED 0/2).
- `./env/bin/python manage.py test` : 28/28 OK ; `check` : 0 problème.
