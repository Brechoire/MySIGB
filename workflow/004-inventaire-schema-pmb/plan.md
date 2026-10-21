# 004 — Inventaire schéma PMB en markdown dans sql/

## Demande

Fichier `.md` qui énumère toutes les tables et champs de la BDD avec une description de quoi elle sert, ajouté dans le dossier `sql/`.

## Objectif

Avoir une cartographie locale du dump PMB Fourmies (619 tables) pour préparer la reprise vers MySIGB (notices, prêts, adhérents, retards, comptes pro), sans committer le dump ni les données perso.

## Todolist

- [x] Parser en streaming les `CREATE TABLE` du dump (lecture seule, sans INSERT/RGPD)
- [x] Générer `sql/schema-pmb.md` : 619 tables, champs + types + rôle, descriptions FR
- [x] Vérifier : 619 tables, `sql/` toujours ignoré, `check` + `test` OK
- [ ] Prochaine demande : créer `workflow/005-...` en incrémentant le numéro

## Fait

- `/tmp/opencode/gen_schema_pmb.py` : parse `sql/base_fourmies_19_03_2026.sql`, descriptions curées pour les tables cœur (`notices`, `exemplaires`, `empr`, `pret`, `pret_archive`, `comptes`...) + heuristiques par préfixe PMB pour les 600 autres, rôles par champ (FK logiques, RGPD, montants, code-barres...).
- `sql/schema-pmb.md` : 372 Ko, 10 063 lignes, 619 tables (`##`), sommaire par domaine (catalogue / adhérents / circulation / retards / finance / référentiels / annexes).
- Fichier dans `sql/` donc couvert par `.gitignore:62` (`git check-ignore` → ignoré, `git status` → `!! sql/`), aucune donnée lecteur reprise (schéma seul).

## Vérification

- `grep -c '^## `' sql/schema-pmb.md` : 619.
- `git check-ignore -v -- sql/schema-pmb.md` : `.gitignore:62:sql/`.
- `./env/bin/python manage.py check` : OK.
- `./env/bin/python manage.py test` : 11 tests OK.
