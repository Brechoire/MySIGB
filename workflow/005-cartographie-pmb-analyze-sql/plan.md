# 005 — Cartographie PMB (skill analyze-sql)

## Demande

Utiliser le skill `analyze-sql` pour cartographier la base PMB (dump confidentiel local) :
structure et relations d'abord, puis éléments nécessaires à la reprise.
Réponses : comptes pro = ~10 comptes type collectivités ; périmètre complet ;
dump reste dans `sql/`, doc dans `docs/sql/` ; PMB v8 (déclaratif).

## Objectif

Mémoire durable du schéma, des liens et du mapping vers le futur projet,
sans jamais exposer de données personnelles, dans `docs/sql/`.

## Todolist

- [x] Extracteur DDL local en flux + test sur données fictives (0 fuite)
- [x] Extraction réelle : 619 tables, 0 vues/triggers/routines, 129 défauts masqués, 0 non couvert
- [x] Générer `docs/sql/` (8 fichiers, 0 INSERT/VALUES, 0 email/tél)
- [x] Vérifier : `check` + `test`
- [ ] Prochaines actions (voir MEMO_SQL) : COUNT locaux, code PMB v8 (relances/amendes), comptes pro/sites, custom fields
- [ ] Prochaine demande : créer `workflow/006-...` en incrémentant le numéro

## Fait

- `/tmp/opencode/extract_ddl.py` (hors repo) : DDL seul retenu, INSERT jamais accumulés
  (classement par préfixe), erreurs sans contenu, literaux sensibles masqués.
- `docs/sql/` : ANALYSE_SQL, DICTIONNAIRE_SQL (619 tables), RELATIONS_SQL
  (0 FK déclarée observée, liens = hypothèses `-.->`), AUDIT_SQL (A1–A9),
  MEMO_SQL, PMB_DOMAINES, MAPPING_IMPORT (cibles « à décider »),
  PLAN_REPRISE (lots, dry-run, retour arrière).
- Invariants : MyISAM x619, utf8mb3, CB uniques, PK `pret` = exemplaire,
  3 897 instructions INSERT sur 238 tables (ni tuples, ni lignes réelles).
- Décisions 21/10/2026 conservées : périmètre complet, dump dans `sql/`,
  secrets non repris, PMB v8 à confirmer.
- Correctif `.gitignore` : motif `sql/` → `/sql/` (le motif nu ignorait aussi
  `docs/sql/`) ; dump toujours ignoré, `docs/sql/` versionnable.

## Vérification

- Jeu fictif : 3 défauts masqués, 0 valeur remontée (emails/téls absents).
- Réel : `grep INSERT/VALUES` dans `docs/sql/` = 0 ; emails = 0 ; téls = 0.
- `./env/bin/python manage.py check` : OK.
- `./env/bin/python manage.py test` : 11 tests OK.
