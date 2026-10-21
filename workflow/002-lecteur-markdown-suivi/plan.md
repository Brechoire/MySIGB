# 002 — Lecteur markdown du suivi + lien footer

## Demande

Avoir dans le site une page « suivi » qui affiche les fichiers `.md` en version web
(interprétation markdown) et permet de naviguer entre eux façon GitHub.
Lien dans le footer comme le lien vers le changelog.

## Objectif

Lire les plans `workflow/` directement dans MySIGB en HTML navigable,
sans relire le markdown brut.

## Todolist

- [x] Rendre `plan.md` en HTML (titres, sections, todolist) dans l'app `changelog`
- [x] Garder la navigation liste + détail façon historique
- [x] Ajouter le lien « Suivi » dans le footer de `base.html`
- [x] Vérifier : `check` + `test` + rendu `/suivi/`
- [ ] Prochaine demande : créer `workflow/003-...`

## Fait

- `changelog/services.py` : `rendre_markdown()` via `Markdown==3.8`
  (extensions `fenced_code`, `tables`), périmètre limité à `workflow/`.
- `changelog/views.py` : `detail` fournit `contenu_html` au gabarit.
- `changelog/templates/changelog/detail.html` : `{{ plan.contenu_html|safe }}`
  au lieu du bloc `<pre>` brut.
- `templates/base.html` : nav footer avec `{% url 'changelog:index' %}`
  (lien header conservé).
- `requirements.txt` : ajout `Markdown==3.8`.
- 4 tests ajoutés : conversion titres/sections, chaîne vide,
  détail rend `<h2>Demande</h2>`, footer de `/` contient `<footer` + `/suivi/`.

## Vérification

- `./env/bin/python manage.py check` : OK
- `./env/bin/python manage.py test` : 11 tests OK
- `/suivi/001-...` et `/suivi/002-...` rendus en HTML, 404 conservée.
