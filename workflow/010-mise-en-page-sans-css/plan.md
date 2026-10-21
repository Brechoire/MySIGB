# 010 — Mise en page correcte sans CSS (HTML sémantique)

## Demande

Mise en page correcte, sans CSS (contrainte repo).

## Objectif

Pages lisibles et structurées avec du seul HTML : tableaux, fieldsets, légendes.

## Todolist

- [x] TDD : assertions `<table>`, `<caption>`, `<fieldset>` (RED 3 échecs)
- [x] Accueil : liste des comptes en `<table>` (`<caption>`, `thead`/`tbody`, `scope`)
- [x] Formulaires connexion/mot de passe en `<fieldset>` + `<legend>`
- [x] Fiche compte : préférences en tableaux par groupe (`Pagination`, `Affichage`, `Catalogage`)
- [x] Vérifier : `check` + `test` (40 tests)
- [ ] Prochaine demande : créer `workflow/011-...` en incrémentant le numéro

## Fait

- Aucun CSS ajouté (ni `<style>`, ni attribut `style`) — identité conservée en `dl`, listes de navigation en `ul`.
- `scope="col"`/`scope="row"` pour l'accessibilité des tableaux.

## Vérification

- `./env/bin/python manage.py test` : 40/40 OK ; `check` : 0 problème.
