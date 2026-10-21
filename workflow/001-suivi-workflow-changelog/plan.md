# 001 — Suivi workflow + changelog visible dans MySIGB

## Demande

Mettre en place un système de suivi : à chaque demande, un dossier `workflow/` numéroté
(qui s'incrémente) avec ce qui a été demandé et ce qui a été fait, plus un changelog
intégré visible dans MySIGB qui énumère ce qui a été fait dans le dernier commit.

## Objectif

Permettre de revenir sur le projet après plusieurs jours et savoir en 2 minutes
où on en était et ce qui reste à faire, sans relire tout le code.

## Todolist

- [x] Créer le dossier `workflow/001-suivi-workflow-changelog/plan.md` (ce fichier)
- [x] Créer l'app Django `changelog` (services, vues, urls, templates, tests)
- [x] Brancher `changelog` dans `app/settings.py`, `app/urls.py` (`/suivi/`) et `templates/base.html`
- [x] Vérifier : `check` + `test` + rendu `/suivi/`
- [ ] Prochaine demande : créer `workflow/002-...` en incrémentant le numéro

## Fait

- App `changelog` lecture seule des dossiers `workflow/NNN-slug/plan.md`, sans base de données.
- `GET /suivi/` : met en avant le dernier plan + liste l'historique trié.
- `GET /suivi/<numero>/` : détail d'un plan, 404 si inexistant.
- Protection contre la traversée de chemin (regex `^[0-9]{3}-[a-z0-9-]+$`, vérification `is_relative_to`).
- 7 tests (`changelog/tests.py`) : tri, dossier vide, recherche par numéro court,
  rejet `../`, vues 200 + 404.
- Conventions respectées : app dédiée, `app_name`, `{% url %}`, `extends "base.html"`,
  blocs `title`/`content`, UI en français, pas de CSS.

## Vérification

- `./env/bin/python manage.py check` : OK
- `./env/bin/python manage.py test changelog -v 2` : 7 tests OK
- `./env/bin/python manage.py test` : OK
- Page `/suivi/` rendue avec ce plan 001 comme dernier plan.
