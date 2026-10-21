# ANALYSE_SQL — PMB Fourmies

## Synthese

Base PMB (SIGB de bibliotheque) : catalogue (notices/exemplaires/bulletins), autorites (auteurs, editeurs, matieres), adherents, circulation (prets/resas/transferts), retards, comptes/finance, referentiels des 12 sites du reseau. Aucune cle etrangere declaree (moteur MyISAM) : les liens sont applicatifs, a valider avant toute reprise.

## Sources

- Fichier : `sql/base_fourmies_19_03_2026.sql` (local, non versionne) ; copie compressee `.gz` supposee identique (taille decompressee annoncee coherente, a confirmer).
- Taille : 3 811 084 014 o ; SHA-256 : `8287509f...c56e` (complet dans MEMO_SQL.md).
- Analyse : 2026-10-21, extracteur DDL local en flux (INSERT jamais accumules, 129 literaux sensibles masques dans le DDL).
- Moteur/version (indices d'en-tete, certitude elevee) :
  - `-- MariaDB dump 10.19  Distrib 10.6.22-MariaDB, for debian-linux-gnu (x86_64)`
  - `-- Host: localhost    Database: fourmies`
  - `-- Server version	10.6.22-MariaDB-0ubuntu0.22.04.1`
  - `-- Current Database: `fourmies``
  - `CREATE DATABASE /*!32312 IF NOT EXISTS*/ `fourmies` /*!40100 DEFAULT CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci */;`
  - `USE `fourmies`;`
## Couverture

- Objets : 619 tables, 0 vues, 0 declencheurs, 0 routines, 619 DROP, 0 ALTER hors boilerplate.
- Moteurs : MyISAM x619.
- Donnees : 3897 instructions INSERT reparties sur 238 tables ; 381 tables sans INSERT.
- Mesure : comptes d'instructions uniquement (ni tuples, ni lignes reelles). Volumes exacts : requetes proposees, non executees (voir PLAN_REPRISE).
- Non couvert : 0 point(s) (details MEMO_SQL) ; aucune portion masquee silencieusement.
## Domaines

- Catalogue : voir PMB_DOMAINES.md.
- Adherents : voir PMB_DOMAINES.md.
- Circulation : voir PMB_DOMAINES.md.
- Retards : voir PMB_DOMAINES.md.
- Comptes/Finance : voir PMB_DOMAINES.md.
- Referentiels : voir PMB_DOMAINES.md.
- Dictionnaire : DICTIONNAIRE_SQL.md ; relations : RELATIONS_SQL.md (hypotheses applicatives) et RELATIONS_BDD.md (constats issus de la BDD) ; audit : AUDIT_SQL.md.
