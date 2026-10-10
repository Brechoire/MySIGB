# MySIGB

Système intégré de gestion de bibliothèque (Django).

## Prérequis

- Python 3.12

## Installation

```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py runserver
```

Ouvrir http://127.0.0.1:8000/

## Structure

- `app/` : configuration Django (settings, urls)
- `home/` : page d'accueil (`/`)
- `templates/` : gabarit de base `base.html`
