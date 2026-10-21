# AUDIT_SQL — PMB Fourmies

| id | prio | constat | preuve | impact | confiance | recommandation | verification |
|---|---|---|---|---|---|---|---|
| A1 | P1 | Dump conserve dans l'arbre de travail (decision humaine du 21/10/2026) | sql/ dans le repo, .gitignore seul rempart | exposition via indexeurs/synchro/outils IA | haute | ne versionner que docs/sql ; interdire pieces jointes du dump | revue d'acces locale, non executee |
| A2 | P1 | Aucune FK declaree : integrite porte par l'applicatif | 0 contrainte FOREIGN KEY sur 619 CREATE TABLE (MyISAM) | orphelins possibles a la reprise | haute | contraintes cible + controles orphelins avant import | requetes proposees (comptes orphelins), non executees |
| A3 | P1 | Secrets et donnees perso presents par nature | colonnes password/digest/token + 129 defauts masques ; champs mail/tel/adresse/naissance | reprise accidentelle de secrets | haute | exclure secrets/sessions/hachages ; reinitialiser acces ; trier archives perso | inventaire local des colonnes sensibles, non execute |
| A4 | P2 | Sentinelles non standard (dates 0000-00-00, '', 0) | types date/datetime NOT NULL avec defaut 0000-00-00 observes | rejet en mode strict / Django | haute | regle de transformation NULL/sentinelles par colonne (voir MAPPING) | profilage local des valeurs, non execute |
| A5 | P2 | PK composite de responsability n'empeche pas les doublons metier | PK observee (id auto + auteur + notice + fonction) | doublons auteur possibles | moyenne |  dedupliquer a l'import (notice,auteur,fonction,ordre) | requete de doublons proposee, non executee |
| A6 | P2 | 381 tables sans INSERT : perimetre flou | 238 tables visees par INSERT sur 619 | modeliser du mort ou rater du vivant | moyenne | classer avant import : supprimer/ignorer vs reprendre vide | liste proposee dans PMB_DOMAINES, a valider |
| A7 | P2 | Ni vues, ni declencheurs, ni routines dans l'export | 0/0/0 observes | regles metier dans le code PMB absent | haute | reconstituer les regles (prets, relances, amendes) depuis PMB version confirmee | lecture du code PMB, non effectuee |
| A8 | P3 | utf8mb3 source : prevoir utf8mb4 cible | CHARSET=utf8mb3 observe | emojis/caracteres rares perdus ou erreurs | haute | conversion + collation explicite a l'import | test sur jeu synthetique accentue, non execute |
| A9 | P2 | AUTO_INCREMENT n'est pas un effectif | max observes (ex. notices 140577) vs instructions INSERT partielles | sur/sous-dimensionnement des lots | haute | compter en local (COUNT) avant de calibrer les lots | requetes COUNT proposees, non executees |
