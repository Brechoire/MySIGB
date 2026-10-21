# MEMO_SQL — memoire compacte

- Source : sql/base_fourmies_19_03_2026.sql, 3 811 084 014 o, SHA-256 8287509f055df878c6e8e15cb17ed58efebc56ef05833c062f4c7ce54758c9d4 ; .gz 571 458 668 o, SHA-256 69b672fc... (contenu suppose identique, a confirmer).
- Analyse : 2026-10-21, extracteur DDL local (flux, INSERT jamais accumules, 129 defauts masques, 0 portion non couverte).
- Invariants : 619 CREATE + 619 DROP ; 0 FK declaree ; MyISAM x619 (totalite) ; utf8mb3 ; CB uniques (empr, exemplaires) ; PK pret = exemplaire.
- Hypotheses : liens par nommage (RELATIONS_SQL) ; comptes pro = empr categ 2 ; PMB v8 (declare).
- Pieges : 0000-00-00/''/0 ; PK composite responsability ; categories PK (num_noeud,langue) ; AUTO_INCREMENT != effectif ; INSERT statements != tuples != lignes.
- Decisions 21/10/2026 : perimetre complet ; dump reste dans sql/ (risque assume) ; doc dans docs/sql/ ; secrets non repris.
- Prochaines actions : COUNT locaux, code PMB v8 (relances/amendes), correspondance comptes pro/sites, custom fields utilises ou non.
