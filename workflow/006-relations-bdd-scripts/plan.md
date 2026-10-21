# 006 — Relations issues de la BDD + dossier scripts/

## Demande

Créer un dossier `scripts/` pour les futurs scripts d'import vers le nouveau projet,
mais avant : analyser les relations entre les tables et l'ajouter dans la doc,
en spécifiant que ce sont les relations issues de la BDD.

## Objectif

Distinguer ce que la base garantit vraiment (contraintes déclarées) des liens
applicatifs supposés, et cadrer les futurs scripts d'import.

## Todolist

- [x] Générer `docs/sql/RELATIONS_BDD.md` depuis la méta extraite (sans relire le dump)
- [x] Lier le document depuis `ANALYSE_SQL.md`
- [x] Créer `scripts/README.md` (conventions, état : aucun script)
- [x] Vérifier : 0 fuite, `check` + `test`
- [ ] Prochaine demande : créer `workflow/007-...` en incrémentant le numéro

## Fait

- `docs/sql/RELATIONS_BDD.md` : 0 FK déclarée observée (MyISAM), unicités
  prouvant une cardinalité (PK `pret` = exemplaire, CB uniques...),
  index par table centrale (candidats de jointure, pas des preuves),
  inventaire global des UNIQUE, lecture pour la reprise.
  Mention explicite : constats BDD ici, hypothèses de nommage dans RELATIONS_SQL.md.
- `scripts/README.md` : conventions (venv, flux local, idempotence, lots,
  dry-run, pas de secrets) + renvois vers PLAN_REPRISE/MAPPING_IMPORT.
- Dossier `scripts/` explicitement demandé : dérogation à la règle
  « pas de dossier d'outillage sans demander ».

## Vérification

- `grep INSERT/VALUES` dans `docs/sql/RELATIONS_BDD.md` : 0 ; emails : 0.
- `./env/bin/python manage.py check` : OK.
- `./env/bin/python manage.py test` : 11 tests OK.
