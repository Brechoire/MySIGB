# 009 — Fiche compte (staff) + SIGB réservée aux connectés

## Demande

Cliquer sur un compte pour voir toutes ses infos. Décision : staff uniquement.
Dans tous les cas, la SIGB n'est accessible qu'aux connectés et non référençable.

## Objectif

Annuaire interne : fiche complète par compte + verrouillage global (login requis, anti-indexation).

## Todolist

- [x] TDD : `accounts/tests_acces.py` (11 tests) + `home/tests.py` adaptés (RED vu)
- [x] `accounts/views.detail` (`staff_member_required`, 404, aucun secret) + template + route `<username>/` en dernier
- [x] `ConnexionRequiseMiddleware` (tout derrière login ; exemptions : connexion/déconnexion/robots/admin-login/statiques) + `X-Robots-Tag: noindex, nofollow` sur chaque réponse
- [x] `robots.txt` (`Disallow: /`) + liens cliquables sur `/`
- [x] Adapter les tests `changelog` au login obligatoire (changement de comportement voulu)
- [x] Vérifier : `check` + `test` (40 tests)
- [ ] Prochaine demande : créer `workflow/010-...` en incrémentant le numéro

## Fait

- Fiche : identifiant, noms, langue, statuts, dates, forçage, refs PMB, préférences (Pagination/Affichage/Catalogage). Hash mdp testé absent.
- Anonymes → `login?next=...` partout ; non-staff → redirection login ; admin login/robots publics.
- Ruling : pas de 403 custom, `staff_member_required` standard (coût : UX redirigée, acceptable en interne).

## Vérification

- `./env/bin/python manage.py test` : 40/40 OK (dont 6 tests préexistants adaptés au login obligatoire) ; `check` : 0 problème.
