# RELATIONS_BDD — relations issues de la base (constats, pas d'hypotheses)

> Source : DDL du dump (`CREATE TABLE`), extraction locale du 2026-10-21. Ce document ne contient QUE des faits observes dans la base : cles primaires, contraintes UNIQUE, index KEY, cles etrangeres declarees.
> Les liens applicatifs supposes par nommage (`expl_notice` -> `notices`...) sont dans RELATIONS_SQL.md et y sont marques HYPOTHESE. Ne pas confondre les deux documents.

## 1. Cles etrangeres declarees : aucune

Constat OBSERVE : 0 contrainte(s) FOREIGN KEY declaree(s) sur 619 tables (moteur MyISAM, aucune clause REFERENCES).
Consequence : la base n'impose aucune integrite referentielle ; les jointures sont portees par le code applicatif PMB, absent de l'export.

## 2. Unicites imposees par la base (prouvent une cardinalite)

Une contrainte UNIQUE ou PRIMARY KEY prouve qu'une valeur ne peut apparaitre qu'une fois : c'est une information de cardinalite garantie par la BDD, pas une hypothese.

| table | contrainte | colonnes | ce que la BDD garantit |
|---|---|---|---|
| `notices` | PRIMARY KEY | `notice_id` | au plus une ligne par valeur(s) |
| `exemplaires` | PRIMARY KEY | `expl_id` | au plus une ligne par valeur(s) |
| `exemplaires` | UNIQUE | `expl_cb` | au plus une ligne par valeur(s) |
| `bulletins` | PRIMARY KEY | `bulletin_id` | au plus une ligne par valeur(s) |
| `authors` | PRIMARY KEY | `author_id` | au plus une ligne par valeur(s) |
| `responsability` | PRIMARY KEY | `id_responsability`, `responsability_author`, `responsability_notice`, `responsability_fonction` | au plus une ligne par valeur(s) |
| `publishers` | PRIMARY KEY | `ed_id` | au plus une ligne par valeur(s) |
| `collections` | PRIMARY KEY | `collection_id` | au plus une ligne par valeur(s) |
| `sub_collections` | PRIMARY KEY | `sub_coll_id` | au plus une ligne par valeur(s) |
| `series` | PRIMARY KEY | `serie_id` | au plus une ligne par valeur(s) |
| `notices_categories` | PRIMARY KEY | `notcateg_notice`, `num_noeud`, `num_vedette` | au plus une ligne par valeur(s) |
| `empr` | PRIMARY KEY | `id_empr` | au plus une ligne par valeur(s) |
| `empr` | UNIQUE | `empr_cb` | au plus une ligne par valeur(s) |
| `empr_categ` | PRIMARY KEY | `id_categ_empr` | au plus une ligne par valeur(s) |
| `empr_codestat` | PRIMARY KEY | `idcode` | au plus une ligne par valeur(s) |
| `empr_statut` | PRIMARY KEY | `idstatut` | au plus une ligne par valeur(s) |
| `pret` | PRIMARY KEY | `pret_idexpl` | au plus une ligne par valeur(s) |
| `pret_archive` | PRIMARY KEY | `arc_id` | au plus une ligne par valeur(s) |
| `resa` | PRIMARY KEY | `id_resa` | au plus une ligne par valeur(s) |
| `resa_archive` | PRIMARY KEY | `resarc_id` | au plus une ligne par valeur(s) |
| `transferts` | PRIMARY KEY | `id_transfert` | au plus une ligne par valeur(s) |
| `transferts_demande` | PRIMARY KEY | `id_transfert_demande` | au plus une ligne par valeur(s) |
| `comptes` | PRIMARY KEY | `id_compte` | au plus une ligne par valeur(s) |
| `transactions` | PRIMARY KEY | `id_transaction` | au plus une ligne par valeur(s) |
| `log_retard` | PRIMARY KEY | `id_log` | au plus une ligne par valeur(s) |
| `recouvrements` | PRIMARY KEY | `recouvr_id` | au plus une ligne par valeur(s) |
| `docs_location` | PRIMARY KEY | `idlocation` | au plus une ligne par valeur(s) |
| `docs_section` | PRIMARY KEY | `idsection` | au plus une ligne par valeur(s) |
| `docs_statut` | PRIMARY KEY | `idstatut` | au plus une ligne par valeur(s) |
| `docs_type` | PRIMARY KEY | `idtyp_doc` | au plus une ligne par valeur(s) |
| `docs_codestat` | PRIMARY KEY | `idcode` | au plus une ligne par valeur(s) |
| `lenders` | PRIMARY KEY | `idlender` | au plus une ligne par valeur(s) |

## 3. Index KEY observes (candidats de jointure, pas des preuves de relation)

Un index KEY/INDEX accelere les recherches et signale les colonnes effectivement interrogees, mais ne prouve ni relation ni cardinalite.

### `notices` (16 index)

- `KEY `typdoc` (`typdoc`)`
- `KEY `tparent_id` (`tparent_id`)`
- `KEY `ed1_id` (`ed1_id`)`
- `KEY `ed2_id` (`ed2_id`)`
- `KEY `coll_id` (`coll_id`)`
- `KEY `subcoll_id` (`subcoll_id`)`
- `KEY `cb` (`code`)`
- `KEY `indexint` (`indexint`)`
- `KEY `sig_index` (`signature`)`
- `KEY `i_notice_n_biblio` (`niveau_biblio`)`
- `KEY `i_notice_n_hierar` (`niveau_hierar`)`
- `KEY `notice_eformat` (`eformat`)`
- `KEY `i_date_parution` (`date_parution`)`
- `KEY `i_not_statut` (`statut`)`
- `KEY `i_map_echelle_num` (`map_echelle_num`)`
- `KEY `i_map_projection_num` (`map_projection_num`)`

### `exemplaires` (10 index)

- `KEY `expl_typdoc` (`expl_typdoc`)`
- `KEY `expl_cote` (`expl_cote`)`
- `KEY `expl_notice` (`expl_notice`)`
- `KEY `expl_codestat` (`expl_codestat`)`
- `KEY `expl_owner` (`expl_owner`)`
- `KEY `expl_bulletin` (`expl_bulletin`)`
- `KEY `i_expl_location` (`expl_location`)`
- `KEY `i_expl_section` (`expl_section`)`
- `KEY `i_expl_statut` (`expl_statut`)`
- `KEY `i_expl_lastempr` (`expl_lastempr`)`

### `bulletins` (4 index)

- `KEY `bulletin_numero` (`bulletin_numero`)`
- `KEY `bulletin_notice` (`bulletin_notice`)`
- `KEY `date_date` (`date_date`)`
- `KEY `i_num_notice` (`num_notice`)`

### `authors` (5 index)

- `KEY `author_see` (`author_see`)`
- `KEY `author_name` (`author_name`)`
- `KEY `author_rejete` (`author_rejete`)`
- `KEY `i_author_type` (`author_type`)`
- `KEY `i_index_author_author_type` (`index_author`(333),`author_type`)`

### `responsability` (2 index)

- `KEY `responsability_notice` (`responsability_notice`)`
- `KEY `i_responsability_author` (`responsability_author`)`

### `publishers` (2 index)

- `KEY `ed_name` (`ed_name`)`
- `KEY `ed_ville` (`ed_ville`)`

### `collections` (2 index)

- `KEY `collection_name` (`collection_name`)`
- `KEY `collection_parent` (`collection_parent`)`

### `sub_collections` (1 index)

- `KEY `sub_coll_name` (`sub_coll_name`)`

### `series` (0 index)

- aucun index secondaire observe

### `notices_categories` (1 index)

- `KEY `num_noeud` (`num_noeud`)`

### `empr` (9 index)

- `KEY `empr_nom` (`empr_nom`)`
- `KEY `empr_date_adhesion` (`empr_date_adhesion`)`
- `KEY `empr_date_expiration` (`empr_date_expiration`)`
- `KEY `i_empr_categ` (`empr_categ`)`
- `KEY `i_empr_codestat` (`empr_codestat`)`
- `KEY `i_empr_location` (`empr_location`)`
- `KEY `i_empr_statut` (`empr_statut`)`
- `KEY `i_empr_typabt` (`type_abt`)`
- `KEY `i_empr_login` (`empr_login`)`

### `empr_categ` (0 index)

- aucun index secondaire observe

### `empr_codestat` (0 index)

- aucun index secondaire observe

### `empr_statut` (0 index)

- aucun index secondaire observe

### `pret` (2 index)

- `KEY `i_pret_idempr` (`pret_idempr`)`
- `KEY `i_pret_arc_id` (`pret_arc_id`)`

### `pret_archive` (8 index)

- `KEY `i_pa_expl_id` (`arc_expl_id`)`
- `KEY `i_pa_idempr` (`arc_id_empr`)`
- `KEY `i_pa_expl_notice` (`arc_expl_notice`)`
- `KEY `i_pa_expl_bulletin` (`arc_expl_bulletin`)`
- `KEY `i_pa_arc_fin` (`arc_fin`)`
- `KEY `i_pa_arc_empr_categ` (`arc_empr_categ`)`
- `KEY `i_pa_arc_expl_location` (`arc_expl_location`)`
- `KEY `i_pa_arc_expl_section` (`arc_expl_section`)`

### `resa` (6 index)

- `KEY `resa_date_fin` (`resa_date_fin`)`
- `KEY `resa_date` (`resa_date`)`
- `KEY `resa_cb` (`resa_cb`)`
- `KEY `i_idbulletin` (`resa_idbulletin`)`
- `KEY `i_idnotice` (`resa_idnotice`)`
- `KEY `i_resa_idempr` (`resa_idempr`)`

### `resa_archive` (4 index)

- `KEY `i_pa_idempr` (`resarc_id_empr`)`
- `KEY `i_pa_notice` (`resarc_idnotice`)`
- `KEY `i_pa_bulletin` (`resarc_idbulletin`)`
- `KEY `i_pa_resarc_date` (`resarc_date`)`

### `transferts` (2 index)

- `KEY `etat_transfert` (`etat_transfert`)`
- `KEY `i_etat_transfert_origine` (`etat_transfert`,`origine`)`

### `transferts_demande` (5 index)

- `KEY `num_transfert` (`num_transfert`)`
- `KEY `num_location_source` (`num_location_source`)`
- `KEY `num_location_dest` (`num_location_dest`)`
- `KEY `num_expl` (`num_expl`)`
- `KEY `i_resa_trans` (`resa_trans`)`

### `comptes` (1 index)

- `KEY `i_cpt_proprio_id` (`proprio_id`)`

### `transactions` (2 index)

- `KEY `i_realisee` (`realisee`)`
- `KEY `i_compte_id` (`compte_id`)`

### `cache_amendes` (1 index)

- `KEY `id_empr` (`id_empr`)`

### `log_retard` (0 index)

- aucun index secondaire observe

### `recouvrements` (0 index)

- aucun index secondaire observe

### `docs_location` (1 index)

- `KEY `locdoc_owner` (`locdoc_owner`)`

### `docs_section` (1 index)

- `KEY `sdoc_owner` (`sdoc_owner`)`

### `docs_statut` (1 index)

- `KEY `statusdoc_owner` (`statusdoc_owner`)`

### `docs_type` (0 index)

- aucun index secondaire observe

### `docs_codestat` (1 index)

- `KEY `statisdoc_owner` (`statisdoc_owner`)`

### `lenders` (0 index)

- aucun index secondaire observe

## 4. Inventaire global des unicites (toutes tables)

- Tables avec PRIMARY KEY composite : 158.
- Tables SANS primary key observee : 54 (doublons exacts possibles cote base).
- Tables avec au moins une contrainte UNIQUE hors PK : 58.

| table | UNIQUE sur |
|---|---|
| `ai_session_shared_list` | `num_ai_session_semantique`, `num_empr`, `num_shared_list` |
| `authorities` | `num_object`, `type_object` |
| `connectors_out_setcaches` | `connectors_out_setcache_setnum` |
| `connectors_out_setcategs` | `connectors_out_setcateg_name` |
| `connectors_out_sets` | `connector_out_set_caption` |
| `contribution_area_datastore_g2t` | `g`, `t` |
| `contribution_area_datastore_id2val` | `id`, `val_type` |
| `contribution_area_datastore_o2val` | `id` |
| `contribution_area_datastore_s2val` | `id` |
| `contribution_area_datastore_setting` | `k` |
| `contribution_area_datastore_triple` | `t` |
| `empr` | `empr_cb` |
| `empr_temp` | `cb` |
| `entrepots_localisations` | `loc_code` |
| `es_esgroups` | `esgroup_name` |
| `es_esusers` | `esuser_username` |
| `exemplaires` | `expl_cb` |
| `exemplaires_temp` | `cb` |
| `gestion_login_attempt` | `gestion_login_attempt_ip`, `gestion_login_attempt_login`, `gestion_login_attempt_time` |
| `groupe` | `libelle_groupe` |
| `indexint` | `indexint_name`, `num_pclass` |
| `ip_blacklist` | `ip_blacklist_ip` |
| `ip_whitelist` | `ip_whitelist_ip` |
| `mails_configuration` | `name_mail_configuration` |
| `mfa_mail` | `context` |
| `mfa_otp` | `context` |
| `mfa_services` | `context` |
| `mfa_sms` | `context` |
| `mots` | `mot` |
| `onto_uri` | `uri` |
| `ontodemo_g2t` | `g`, `t` |
| `ontodemo_id2val` | `id`, `val_type` |
| `ontodemo_o2val` | `id` |
| `ontodemo_s2val` | `id` |
| `ontodemo_setting` | `k` |
| `ontodemo_triple` | `t` |
| `ontology_g2t` | `g`, `t` |
| `ontology_id2val` | `id`, `val_type` |
| `ontology_o2val` | `id` |
| `ontology_s2val` | `id` |
| `ontology_setting` | `k` |
| `ontology_triple` | `t` |
| `opac_login_attempt` | `opac_login_attempt_ip`, `opac_login_attempt_login`, `opac_login_attempt_time` |
| `parametres` | `type_param`, `sstype_param` |
| `parametres2` | `type_param`, `sstype_param` |
| `parametres_uncached` | `type_param`, `sstype_param` |
| `rdfstore_g2t` | `g`, `t` |
| `rdfstore_id2val` | `id`, `val_type` |
| `rdfstore_o2val` | `id` |
| `rdfstore_s2val` | `id` |
| `rdfstore_setting` | `k` |
| `rdfstore_triple` | `t` |
| `sauv_tables` | `sauv_table_nom` |
| `tabs` | `tab_module`, `tab_categ`, `tab_sub` |
| `thesaurus` | `libelle_thesaurus` |
| `transaction_payments` | `order_number` |
| `visionneuse_params` | `visionneuse_params_class` |
| `words` | `word`, `lang` |

## 5. Lecture pour la reprise

- `pret` : PK sur `pret_idexpl` OBSERVEE => la base interdit deux prets en cours sur le meme exemplaire. A reproduire en contrainte cible.
- `empr.empr_cb`, `exemplaires.expl_cb` : UNIQUE OBSERVEES => codes-barres utilisables comme cles metier stables (conserver en chaines, zeros initiaux significatifs).
- `responsability` : PK composite incluant un auto-increment => la base N'EMPECHE PAS les doublons (notice, auteur, fonction). Dedupliquer a l'import (voir MAPPING_IMPORT).
- Tables sans PK : a identifier dans le dictionnaire avant tout import differentiel (pas de cle stable cote source).
