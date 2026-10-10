# MySIGB — notes agent

Django 6.1 (Python 3.12). SIGB : catalogue, emprunts, adhérents, rôles, API (en construction — seule la page d'accueil `/` existe).

## Commandes

- Toujours utiliser le venv du projet : `./env/bin/python ...` (pas `python3` système, pas de nouveau venv).
- Vérifier : `./env/bin/python manage.py check`
- Tests : `./env/bin/python manage.py test` (aucun test écrit pour l'instant, `home/tests.py` est vide).
- Lancer : `./env/bin/python manage.py runserver` → http://127.0.0.1:8000/
- Après modif de modèles : `./env/bin/python manage.py makemigrations && ./env/bin/python manage.py migrate` (`db.sqlite3` est gitignoré).

## Conventions du repo

- `app/` = config Django uniquement ; chaque fonctionnalité = une app Django dédiée (ex : `home/`).
- URLs : `app/urls.py` fait `include()` des `home.urls` à la racine ; `home/urls.py` définit `app_name = "home"` → référencer avec `{% url 'home:index' %}`, jamais en dur.
- Templates : `templates/base.html` global (via `TEMPLATES['DIRS']`) + `APP_DIRS=True` ; ex : `home/templates/home/index.html` fait `{% extends "base.html" %}` avec les blocs `title` / `content`. **Pas de CSS** (choix utilisateur).
- UI en français.
- Settings (`app/settings.py`) : `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS` viennent de l'env (`DJANGO_SECRET_KEY`, `DJANGO_DEBUG`, `DJANGO_ALLOWED_HOSTS`, stdlib `os.environ`, sans dépendance). Modèle : `.env.example`. Ne jamais committer `.env` ni de vrai secret (fallback insecure présent uniquement pour le dev local).
- Dépôt propre pour push GitHub : `env/`, `__pycache__/`, `*.pyc`, `db.sqlite3`, `.env` ignorés. Ne pas ajouter de dossier d'outillage au repo sans demander.
- CI : workflow Gitleaks (`.github/workflows/secret-scanning.yml`) sur push/PR vers `main` — un secret commité fait échouer la CI.

## Skills sécu (global, `~/.agents/skills/`)

11 skills pentest/sécu web installées en global (pentest WSTG, XSS, SQLi, CSRF, IDOR, BFLA, OWASP API Top 10, audit security-headers, hardening Docker, Trivy, Gitleaks). Les activer sur demande langage naturel ou `@id` quand on audite ou durcit l'app.
