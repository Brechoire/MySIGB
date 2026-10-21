# MySIGB — notes agent

Django 6.1 (Python 3.12). SIGB : catalogue, emprunts, adhérents, rôles, API (en construction — pages existantes : `/` (home), `/suivi/` (changelog : suivi workflow + lecteur markdown)).

## Commandes

- Toujours utiliser le venv du projet : `./env/bin/python ...` (pas `python3` système, pas de nouveau venv).
- Vérifier : `./env/bin/python manage.py check`
- Tests : `./env/bin/python manage.py test` (`changelog/tests.py` : services + vues ; `home/tests.py` vide).
- Lancer : `./env/bin/python manage.py runserver` → http://127.0.0.1:8000/
- Après modif de modèles : `./env/bin/python manage.py makemigrations && ./env/bin/python manage.py migrate` (`db.sqlite3` est gitignoré).
- Après modif de `requirements.txt` : `./env/bin/pip install -r requirements.txt`.

## Conventions du repo

- `app/` = config Django uniquement ; chaque fonctionnalité = une app Django dédiée (ex : `home/`).
- URLs : `app/urls.py` fait `include()` des `home.urls` à la racine ; `home/urls.py` définit `app_name = "home"` → référencer avec `{% url 'home:index' %}`, jamais en dur.
- Templates : `templates/base.html` global (via `TEMPLATES['DIRS']`) + `APP_DIRS=True` ; ex : `home/templates/home/index.html` fait `{% extends "base.html" %}` avec les blocs `title` / `content`. **Pas de CSS** (choix utilisateur).
- Navigation : lien « Suivi » dans le header ET dans le footer (`{% url 'changelog:index' %}`).
- Suivi : dossier versionné `workflow/`, un sous-dossier `NNN-slug/plan.md` par demande, numéro incrémenté (`001-...`, `002-...`), rubriques demande / objectif / todolist / fait / vérification. À chaque demande, créer le dossier suivant.
- `changelog/` : app lecture seule, sans modèle ni DB, lit uniquement `workflow/` via `services.py` (`list_plans`, `get_plan`, `rendre_markdown` avec `Markdown==3.8`, extensions `fenced_code`, `tables`). Vues `index` (dernier plan + historique) / `detail` (404 si inexistant), anti-traversée (`^[0-9]{3}-[a-z0-9-]+$` + `is_relative_to`). `|safe` uniquement sur le HTML généré depuis `workflow/` (fichiers versionnés de confiance).
- UI en français.
- Settings (`app/settings.py`) : `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS` viennent de l'env (`DJANGO_SECRET_KEY`, `DJANGO_DEBUG`, `DJANGO_ALLOWED_HOSTS`, stdlib `os.environ`, sans dépendance). Modèle : `.env.example`. Ne jamais committer `.env` ni de vrai secret (fallback insecure présent uniquement pour le dev local).
- Dépôt propre pour push GitHub : `env/`, `__pycache__/`, `*.pyc`, `db.sqlite3`, `.env` ignorés. Ne pas ajouter de dossier d'outillage au repo sans demander.
- CI : workflow Gitleaks (`.github/workflows/secret-scanning.yml`) sur push/PR vers `main` — un secret commité fait échouer la CI.

## Skills sécu (global, `~/.agents/skills/`)

11 skills pentest/sécu web installées en global (pentest WSTG, XSS, SQLi, CSRF, IDOR, BFLA, OWASP API Top 10, audit security-headers, hardening Docker, Trivy, Gitleaks). Les activer sur demande langage naturel ou `@id` quand on audite ou durcit l'app.
