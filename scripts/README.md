# Scripts d'import vers MySIGB

Dossier prévu pour les futurs scripts d'import des données PMB vers le nouveau projet.

## Conventions obligatoires

- Toujours exécuter avec le venv du projet : `./env/bin/python scripts/<nom>.py`
  (pas de `python3` système, pas de nouveau venv).
- Ne jamais lire `sql/base_fourmies_*.sql` avec des outils qui remontent son contenu
  (lecture, recherche) : seuls les extracteurs locaux en flux, à sorties bornées
  non sensibles, sont autorisés (voir `docs/sql/ANALYSE_SQL.md`).
- Idempotence : réexécution sans doublons (clés stables source conservées,
  `arc_id`, codes-barres en chaînes).
- Lots bornés + checkpoints sans données personnelles + quarantaine locale des rejets.
- Mode simulation (`--dry-run`) par défaut ; aucun écart accepté sans explication.
- Ne jamais recopier mots de passe, hachages, sessions, jetons.
- Séquences et règles métier : voir `docs/sql/PLAN_REPRISE.md` et `MAPPING_IMPORT.md`.

## État

Aucun script d'import pour l'instant. Premier candidat : comptages locaux
(`COUNT` par table et par année, orphelins) — requêtes listées dans `PLAN_REPRISE.md`.
