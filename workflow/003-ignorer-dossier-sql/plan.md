# 003 — Ignorer le dossier sql (sauvegarde BDD PMB)

## Demande

Ignorer le dossier `sql/` nouvellement créé car il contient une sauvegarde de la BDD de PMB, il ne doit pas être commit.

## Objectif

Éviter tout commit accidentel du dump PMB (`sql/*.sql`, `*.sql.gz`) tout en gardant le dossier utilisable en local.

## Todolist

- [x] Ajouter `sql/` au `.gitignore`
- [x] Vérifier : `sql/` ignoré par git, non suivi, `.gitignore` pris en compte
- [ ] Prochaine demande : créer `workflow/004-...` en incrémentant le numéro

## Fait

- `.gitignore` : nouvelle rubrique « Sauvegardes locales » avec `sql/`.
- Dossier `sql/` laissé en place en local (`base_fourmies_19_03_2026.sql`, `.sql.gz`), non suivi par git.
- Créé `workflow/003-ignorer-dossier-sql/plan.md` (ce fichier).

## Vérification

- `git check-ignore -v -- sql/` : retourne `.gitignore` (ignoré).
- `git status --short --ignored -- sql/` : affiche `!! sql/`.
- `git ls-files -- sql/` : vide (rien de suivi).
