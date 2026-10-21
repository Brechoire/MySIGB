# DICTIONNAIRE_SQL — PMB Fourmies

619 tables : `colonne | type exact | NULL | defaut | cles | role`.
Defauts entre crochets = literaux masques (voir dump local). « lien suppose » = hypothese de nommage, pas une contrainte.
Preuve par table indiquee sous son titre.

## `abo_liste_lecture`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 1/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_empr` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `num_liste` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `etat` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `commentaire` | text NOT NULL | non | — |  |  |

## `abts_abts`

Domaine probable : abonnements de periodiques (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 2/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `abt_id` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `abt_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `abt_name_opac` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `base_modele_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `base_modele_id` | int(11) NOT NULL DEFAULT 0 | non | 0 |  | identifiant |
| `num_notice` | int(11) NOT NULL DEFAULT 0 | non | 0 |  | lien suppose -> notices.notice_id |
| `date_debut` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `date_fin` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `fournisseur` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `destinataire` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `cote` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | cote |
| `typdoc_id` | int(11) NOT NULL DEFAULT 0 | non | 0 |  | identifiant |
| `exemp_auto` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `location_id` | int(11) NOT NULL DEFAULT 0 | non | 0 |  | identifiant |
| `section_id` | int(11) NOT NULL DEFAULT 0 | non | 0 |  | identifiant |
| `lender_id` | int(11) NOT NULL DEFAULT 0 | non | 0 |  | identifiant |
| `statut_id` | int(11) NOT NULL DEFAULT 0 | non | 0 |  | identifiant |
| `codestat_id` | int(11) NOT NULL DEFAULT 0 | non | 0 |  | identifiant |
| `type_antivol` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `duree_abonnement` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `abt_numeric` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `prix` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | montant |
| `abt_status` | int(1) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |
| `expl_custom_fields` | mediumtext DEFAULT NULL | oui | NULL |  | champ exemplaire |

## `abts_abts_modeles`

Domaine probable : abonnements de periodiques (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 3/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `modele_id` | int(11) NOT NULL DEFAULT 0 | non | 0 | PK | identifiant |
| `abt_id` | int(11) NOT NULL DEFAULT 0 | non | 0 | PK | identifiant |
| `num` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `vol` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `tome` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `delais` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `critique` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_statut_general` | smallint(5) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `abts_grille_abt`

Domaine probable : abonnements de periodiques (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 4/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_bull` | int(11) NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `num_abt` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `date_parution` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `modele_id` | int(11) NOT NULL DEFAULT 0 | non | 0 |  | identifiant |
| `type` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `nombre` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `numero` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `ordre` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `state` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `abts_grille_modele`

Domaine probable : abonnements de periodiques (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 5/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_modele` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `date_parution` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | PK,DEFAUT MASQUE | date |
| `type_serie` | int(11) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `numero` | varchar(50) NOT NULL DEFAULT '' | non | '' |  |  |
| `nombre_recu` | int(11) NOT NULL DEFAULT 1 | non | 1 |  |  |

## `abts_modeles`

Domaine probable : abonnements de periodiques (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 6/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `modele_id` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `modele_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `num_notice` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  | lien suppose -> notices.notice_id |
| `num_periodicite` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `duree_abonnement` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `date_debut` | date DEFAULT NULL | oui | NULL |  | date |
| `date_fin` | date DEFAULT NULL | oui | NULL |  | date |
| `days` | varchar(7) NOT NULL DEFAULT '1111111' | non | '1111111' |  |  |
| `day_month` | varchar(31) NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE |  |
| `week_month` | varchar(6) NOT NULL DEFAULT '111111' | non | '111111' |  |  |
| `week_year` | varchar(54) NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE |  |
| `month_year` | varchar(12) NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE |  |
| `num_cycle` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_combien` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_increment` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_date_unite` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_increment_date` | int(11) NOT NULL DEFAULT 0 | non | 0 |  | date |
| `num_increment_day_of_month` | int(2) NOT NULL DEFAULT 1 | non | 1 |  |  |
| `num_increment_month_of_year` | int(2) NOT NULL DEFAULT 1 | non | 1 |  |  |
| `num_depart` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `vol_actif` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `vol_increment` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `vol_date_unite` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `vol_increment_numero` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `vol_increment_date` | int(11) NOT NULL DEFAULT 0 | non | 0 |  | date |
| `vol_increment_day_of_month` | int(2) NOT NULL DEFAULT 1 | non | 1 |  |  |
| `vol_increment_month_of_year` | int(2) NOT NULL DEFAULT 1 | non | 1 |  |  |
| `vol_cycle` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `vol_combien` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `vol_depart` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `tom_actif` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `tom_increment` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `tom_date_unite` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `tom_increment_numero` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `tom_increment_date` | int(11) NOT NULL DEFAULT 0 | non | 0 |  | date |
| `tom_increment_day_of_month` | int(2) NOT NULL DEFAULT 1 | non | 1 |  |  |
| `tom_increment_month_of_year` | int(2) NOT NULL DEFAULT 1 | non | 1 |  |  |
| `tom_cycle` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `tom_combien` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `tom_depart` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `format_aff` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `format_periode` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |

## `abts_periodicites`

Domaine probable : abonnements de periodiques (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 15 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 7/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `periodicite_id` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `libelle` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `duree` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `unite` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `retard_periodicite` | int(4) DEFAULT 0 | oui | 0 |  |  |
| `seuil_periodicite` | int(4) DEFAULT 0 | oui | 0 |  |  |
| `consultation_duration` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `abts_status`

Domaine probable : abonnements de periodiques (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 2 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 8/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `abts_status_id` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `abts_status_gestion_libelle` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `abts_status_opac_libelle` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `abts_status_class_html` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `abts_status_bulletinage_active` | tinyint(1) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |

## `acces_profiles`

Domaine probable : droits d'acces / profils (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 9/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `prf_id` | int(2) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `prf_type` | int(1) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |
| `prf_name` | varchar(255) NOT NULL | non | — |  | libelle |
| `prf_rule` | blob NOT NULL | non | — |  |  |
| `prf_hrule` | text NOT NULL | non | — |  |  |
| `prf_used` | int(2) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `dom_num` | int(2) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `acces_rights`

Domaine probable : droits d'acces / profils (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 10/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `dom_num` | int(2) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `usr_prf_num` | int(2) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `res_prf_num` | int(2) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `dom_rights` | int(2) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `actes`

Domaine probable : acquisitions (commandes, factures) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 11/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_acte` | int(8) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `date_acte` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `numero` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `type_acte` | int(3) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `statut` | int(3) unsigned NOT NULL DEFAULT 0 | non | 0 |  | metadonnee catalogue |
| `date_paiement` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `num_paiement` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `num_entite` | int(5) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_fournisseur` | int(5) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_contact_livr` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_contact_fact` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_exercice` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `commentaires` | text NOT NULL | non | — |  |  |
| `reference` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `index_acte` | text NOT NULL | non | — |  |  |
| `devise` | varchar(25) NOT NULL DEFAULT '' | non | '' |  |  |
| `commentaires_i` | text NOT NULL | non | — |  |  |
| `date_valid` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `date_ech` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `nom_acte` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |

## `admin_session`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 12/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `userid` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `session` | mediumblob DEFAULT NULL | oui | NULL |  |  |

## `ai_session_semantique`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 13/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_ai_session_semantique` | int(11) NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `ai_session_semantique_name` | varchar(255) NOT NULL | non | — |  | libelle |
| `ai_session_semantique_questions` | mediumblob NOT NULL DEFAULT '[]' | non | '[]' |  |  |
| `ai_session_semantique_reponses` | mediumblob NOT NULL DEFAULT '[]' | non | '[]' |  |  |
| `ai_session_semantique_num_objects` | mediumblob NOT NULL DEFAULT '[]' | non | '[]' |  |  |
| `ai_session_semantique_anonyme_sessid` | varchar(12) NOT NULL DEFAULT '' | non | '' |  |  |
| `ai_session_semantique_type` | int(11) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `ai_session_shared_list`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 14/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_ai_session_semantique` | int(11) unsigned NOT NULL | non | — | UNIQUE |  |
| `num_empr` | int(11) unsigned NOT NULL | non | — | UNIQUE |  |
| `num_shared_list` | int(11) unsigned NOT NULL | non | — | UNIQUE |  |

## `ai_settings`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 15/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_ai_setting` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `settings_ai_settings` | mediumblob NOT NULL | non | — |  |  |
| `active_ai_settings` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `ai_shared_list`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 16/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_ai_shared_list` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `settings_ai_shared_list` | mediumblob NOT NULL | non | — |  |  |

## `ai_shared_list_docnum`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 17/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_ai_shared_list_docnum` | int(11) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `name_ai_shared_list_docnum` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `content_ai_shared_list_docnum` | mediumtext NOT NULL DEFAULT '' | non | '' |  |  |
| `mimetype_ai_shared_list_docnum` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `extfile_ai_shared_list_docnum` | varchar(20) NOT NULL DEFAULT '' | non | '' |  |  |
| `path_ai_shared_list_docnum` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `hash_name_ai_shared_list_docnum` | mediumtext NOT NULL DEFAULT '' | non | '' |  |  |
| `hash_binary_ai_shared_list_docnum` | mediumtext NOT NULL DEFAULT '' | non | '' |  |  |
| `num_list_ai_shared_list_docnum` | int(11) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `flag_ai_shared_list_docnum` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `analysis`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 18/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `analysis_bulletin` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `analysis_notice` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |

## `analytics_services`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 19/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_analytics_service` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `analytics_service_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `analytics_service_active` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `analytics_service_parameters` | mediumtext NOT NULL | non | — |  |  |
| `analytics_service_template` | text NOT NULL | non | — |  |  |
| `analytics_service_consent_template` | text NOT NULL | non | — |  |  |

## `anim_animation_categories`

Domaine probable : action culturelle (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 20/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_animation` | int(11) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `num_noeud` | int(11) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `ordre_categorie` | int(11) DEFAULT NULL | oui | NULL |  |  |

## `anim_animation_custom`

Domaine probable : action culturelle (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 21/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `idchamp` | int(11) NOT NULL AUTO_INCREMENT | non | — | PK,AI |  |
| `num_type` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `titre` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `type` | varchar(10) NOT NULL DEFAULT 'text' | non | 'text' |  |  |
| `datatype` | varchar(10) NOT NULL DEFAULT '' | non | '' |  |  |
| `options` | text DEFAULT NULL | oui | NULL |  |  |
| `multiple` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `obligatoire` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `ordre` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `search` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `export` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `exclusion_obligatoire` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `pond` | int(11) NOT NULL DEFAULT 100 | non | 100 |  |  |
| `opac_sort` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `comment` | blob NOT NULL | non | — |  |  |
| `filters` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `custom_classement` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |

## `anim_animation_custom_dates`

Domaine probable : action culturelle (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 22/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `anim_animation_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `anim_animation_custom_origine` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `anim_animation_custom_date_type` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `anim_animation_custom_date_start` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `anim_animation_custom_date_end` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `anim_animation_custom_order` | int(11) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |

## `anim_animation_custom_lists`

Domaine probable : action culturelle (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 23/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_anim_animation_custom_list` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `anim_animation_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `anim_animation_custom_list_value` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `anim_animation_custom_list_lib` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `ordre` | int(11) DEFAULT NULL | oui | NULL |  |  |

## `anim_animation_custom_values`

Domaine probable : action culturelle (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 24/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `anim_animation_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `anim_animation_custom_origine` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `anim_animation_custom_small_text` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `anim_animation_custom_text` | text DEFAULT NULL | oui | NULL |  |  |
| `anim_animation_custom_integer` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `anim_animation_custom_date` | date DEFAULT NULL | oui | NULL |  | date |
| `anim_animation_custom_float` | float DEFAULT NULL | oui | NULL |  |  |
| `anim_animation_custom_order` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `anim_animation_locations`

Domaine probable : action culturelle (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 25/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_animation` | int(11) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `num_location` | int(11) NOT NULL DEFAULT 0 | non | 0 | PK |  |

## `anim_animations`

Domaine probable : action culturelle (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 26/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_animation` | int(11) NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `name` | varchar(255) NOT NULL | non | — |  |  |
| `comment` | text DEFAULT NULL | oui | NULL |  |  |
| `description` | text DEFAULT NULL | oui | NULL |  |  |
| `global_quota` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `internet_quota` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `num_status` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `num_event` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `num_parent` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `expiration_delay` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `registration_required` | tinyint(1) DEFAULT NULL | oui | NULL |  |  |
| `auto_registration` | tinyint(1) DEFAULT NULL | oui | NULL |  |  |
| `allow_waiting_list` | tinyint(1) DEFAULT NULL | oui | NULL |  |  |
| `num_cart` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_type` | int(11) NOT NULL DEFAULT 1 | non | 1 |  |  |
| `num_calendar` | int(11) NOT NULL DEFAULT 1 | non | 1 |  |  |
| `logo` | blob DEFAULT NULL | oui | NULL |  |  |
| `unique_registration` | tinyint(4) DEFAULT 0 | oui | 0 |  |  |
| `num_public_type` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `anim_animations_fields_global_index`

Domaine probable : action culturelle (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 27/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_animation` | mediumint(8) NOT NULL DEFAULT 0 | non | 0 | PK | identifiant |
| `code_champ` | int(3) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `code_ss_champ` | int(3) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `ordre` | int(4) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `value` | text NOT NULL | non | — |  |  |
| `pond` | int(4) NOT NULL DEFAULT 100 | non | 100 |  |  |
| `lang` | varchar(10) NOT NULL DEFAULT '' | non | '' | PK |  |
| `authority_num` | varchar(50) NOT NULL DEFAULT '0' | non | '0' |  |  |

## `anim_animations_words_global_index`

Domaine probable : action culturelle (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 28/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_animation` | mediumint(8) NOT NULL DEFAULT 0 | non | 0 | PK | identifiant |
| `code_champ` | int(3) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `code_ss_champ` | int(3) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `num_word` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `pond` | int(4) NOT NULL DEFAULT 100 | non | 100 |  |  |
| `position` | int(11) NOT NULL DEFAULT 1 | non | 1 | PK |  |
| `field_position` | int(11) NOT NULL DEFAULT 1 | non | 1 | PK |  |

## `anim_calendar`

Domaine probable : action culturelle (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 2 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 29/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_calendar` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `color` | varchar(255) NOT NULL DEFAULT '#0D9B7A' | non | '#0D9B7A' |  |  |

## `anim_events`

Domaine probable : action culturelle (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 30/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_event` | int(11) NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `start_date` | datetime DEFAULT NULL | oui | NULL |  | date |
| `end_date` | datetime DEFAULT NULL | oui | NULL |  | date |
| `num_config` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `during_day` | int(11) DEFAULT 0 | oui | 0 |  |  |

## `anim_mailing_list`

Domaine probable : action culturelle (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 31/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_mailing_list` | int(11) NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `send_at` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE |  |
| `num_animation` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `auto_send` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `nb_success_mails` | int(11) NOT NULL DEFAULT 0 | non | 0 |  | donnee perso RGPD |
| `nb_error_mails` | int(11) NOT NULL DEFAULT 0 | non | 0 |  | donnee perso RGPD |
| `mailing_content` | blob NOT NULL | non | — |  | donnee perso RGPD |
| `response_content` | blob NOT NULL | non | — |  |  |
| `num_user` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_campaign` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `anim_mailing_types`

Domaine probable : action culturelle (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 32/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_mailing_type` | int(11) NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `name` | varchar(255) DEFAULT '' | oui | '' |  |  |
| `delay` | int(11) DEFAULT 0 | oui | 0 |  |  |
| `periodicity` | int(1) DEFAULT 0 | oui | 0 |  |  |
| `auto_send` | int(1) DEFAULT 0 | oui | 0 |  |  |
| `num_template` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `campaign` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_sender` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `anim_mailings`

Domaine probable : action culturelle (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 33/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_mailing` | int(11) NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `num_animation` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_mailing_type` | int(11) NOT NULL DEFAULT 0 | non | 0 |  | donnee perso RGPD |
| `already_mail` | int(1) NOT NULL DEFAULT 0 | non | 0 |  | donnee perso RGPD |

## `anim_price_type_categories`

Domaine probable : action culturelle (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 34/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_price_type` | int(11) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `num_noeud` | int(11) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `ordre_categorie` | int(11) DEFAULT NULL | oui | NULL |  |  |

## `anim_price_type_custom`

Domaine probable : action culturelle (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 35/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `idchamp` | int(11) NOT NULL AUTO_INCREMENT | non | — | PK,AI |  |
| `num_type` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `titre` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `type` | varchar(10) NOT NULL DEFAULT 'text' | non | 'text' |  |  |
| `datatype` | varchar(10) NOT NULL DEFAULT '' | non | '' |  |  |
| `options` | text DEFAULT NULL | oui | NULL |  |  |
| `multiple` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `obligatoire` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `ordre` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `search` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `export` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `exclusion_obligatoire` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `pond` | int(11) NOT NULL DEFAULT 100 | non | 100 |  |  |
| `opac_sort` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `comment` | blob NOT NULL | non | — |  |  |
| `filters` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `custom_classement` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |

## `anim_price_type_custom_dates`

Domaine probable : action culturelle (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 36/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `anim_price_type_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `anim_price_type_custom_origine` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `anim_price_type_custom_date_type` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `anim_price_type_custom_date_start` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `anim_price_type_custom_date_end` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `anim_price_type_custom_order` | int(11) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |

## `anim_price_type_custom_lists`

Domaine probable : action culturelle (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 37/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_anim_price_type_custom_list` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `anim_price_type_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `anim_price_type_custom_list_value` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `anim_price_type_custom_list_lib` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `ordre` | int(11) DEFAULT NULL | oui | NULL |  |  |

## `anim_price_type_custom_values`

Domaine probable : action culturelle (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 38/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `anim_price_type_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `anim_price_type_custom_origine` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `anim_price_type_custom_small_text` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `anim_price_type_custom_text` | text DEFAULT NULL | oui | NULL |  |  |
| `anim_price_type_custom_integer` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `anim_price_type_custom_date` | date DEFAULT NULL | oui | NULL |  | date |
| `anim_price_type_custom_float` | float DEFAULT NULL | oui | NULL |  |  |
| `anim_price_type_custom_order` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `anim_price_types`

Domaine probable : action culturelle (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 2 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 39/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_price_type` | int(11) NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `name` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `default_value` | float(12,2) DEFAULT NULL | oui | NULL |  |  |

## `anim_prices`

Domaine probable : action culturelle (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 40/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_price` | int(11) NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `num_animation` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `name` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `value` | float(12,2) DEFAULT NULL | oui | NULL |  |  |
| `num_price_type` | int(11) DEFAULT NULL | oui | NULL |  |  |

## `anim_public_type`

Domaine probable : action culturelle (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 41/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_public_type` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `label` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |

## `anim_registration_origins`

Domaine probable : action culturelle (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 2 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 42/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_registration_origin` | int(11) NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `name` | varchar(255) DEFAULT NULL | oui | NULL |  |  |

## `anim_registration_status`

Domaine probable : action culturelle (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 4 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 43/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_registration_status` | int(11) NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `name` | varchar(255) DEFAULT NULL | oui | NULL |  |  |

## `anim_registrations`

Domaine probable : action culturelle (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 44/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_registration` | int(11) NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `nb_registered_persons` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `name` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `email` | varchar(255) DEFAULT NULL | oui | NULL |  | donnee perso RGPD |
| `phone_number` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `num_animation` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `num_registration_status` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `num_empr` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `num_origin` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `date` | timestamp NOT NULL DEFAULT current_timestamp() | non | current_timestamp() |  |  |
| `hash` | varchar(255) DEFAULT '' | oui | '' |  |  |

## `anim_registred_persons`

Domaine probable : action culturelle (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 45/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_person` | int(11) NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `num_empr` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `num_price` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `num_registration` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `person_name` | varchar(255) DEFAULT NULL | oui | NULL |  | libelle |

## `anim_status`

Domaine probable : action culturelle (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 2 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 46/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_status` | int(11) NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `label` | varchar(255) NOT NULL | non | — |  | libelle |
| `color` | varchar(7) DEFAULT '#0D9B7A' | oui | '#0D9B7A' |  |  |

## `anim_types`

Domaine probable : action culturelle (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 2 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 47/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_type` | int(11) NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `label` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |

## `arch_emplacement`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 2 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 48/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `archempla_id` | int(8) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `archempla_libelle` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |

## `arch_statut`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 2 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 49/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `archstatut_id` | int(8) NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `archstatut_gestion_libelle` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `archstatut_opac_libelle` | varchar(255) NOT NULL | non | — |  | libelle |
| `archstatut_visible_opac` | tinyint(1) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |
| `archstatut_visible_opac_abon` | tinyint(1) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |
| `archstatut_visible_gestion` | tinyint(1) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |
| `archstatut_class_html` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |

## `arch_type`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 2 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 50/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `archtype_id` | int(8) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `archtype_libelle` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |

## `ark`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 51/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `identifier` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `metadata` | blob DEFAULT NULL | oui | NULL |  |  |
| `entity_type` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |

## `ark_entity_pmb`

Domaine probable : identifiants perennes ARK (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 52/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id` | int(11) NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `entity_type` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `entity_id` | int(11) NOT NULL DEFAULT 0 | non | 0 |  | identifiant |
| `num_ark` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `audit`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 72, preuve : CREATE TABLE observe (bloc 53/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `type_obj` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `object_id` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  | identifiant |
| `user_id` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  | identifiant |
| `user_name` | varchar(20) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `type_modif` | int(1) NOT NULL DEFAULT 1 | non | 1 |  |  |
| `quand` | timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp() | non | current_timestamp() |  |  |
| `info` | text NOT NULL | non | — |  |  |
| `type_user` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `aut_link`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 54/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_aut_link` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `aut_link_from` | int(2) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `aut_link_from_num` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `aut_link_to` | int(2) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `aut_link_to_num` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `aut_link_type` | varchar(10) NOT NULL DEFAULT '' | non | '' |  |  |
| `aut_link_comment` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `aut_link_string_start_date` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | date |
| `aut_link_string_end_date` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | date |
| `aut_link_start_date` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `aut_link_end_date` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `aut_link_rank` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `aut_link_direction` | varchar(4) NOT NULL DEFAULT '' | non | '' |  |  |
| `aut_link_reverse_link_num` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `authentication_configs`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 55/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `source_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `settings` | mediumblob NOT NULL | non | — |  |  |
| `context` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `ranking` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `authentication_models`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 56/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `source_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `settings` | mediumblob NOT NULL | non | — |  |  |
| `context` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `author_custom`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 57/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `idchamp` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI |  |
| `num_type` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `titre` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `type` | varchar(10) NOT NULL DEFAULT 'text' | non | 'text' |  |  |
| `datatype` | varchar(10) NOT NULL DEFAULT '' | non | '' |  |  |
| `options` | text DEFAULT NULL | oui | NULL |  |  |
| `multiple` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `obligatoire` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `ordre` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `search` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `export` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `filters` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `exclusion_obligatoire` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `pond` | int(11) NOT NULL DEFAULT 100 | non | 100 |  |  |
| `opac_sort` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `comment` | blob NOT NULL | non | — |  |  |
| `custom_classement` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |

## `author_custom_dates`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 58/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `author_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `author_custom_origine` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `author_custom_date_type` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `author_custom_date_start` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `author_custom_date_end` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `author_custom_order` | int(11) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |

## `author_custom_lists`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 59/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_author_custom_list` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `author_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `author_custom_list_value` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `author_custom_list_lib` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `ordre` | int(11) DEFAULT NULL | oui | NULL |  |  |

## `author_custom_values`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 60/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `author_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `author_custom_origine` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `author_custom_small_text` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `author_custom_text` | text DEFAULT NULL | oui | NULL |  |  |
| `author_custom_integer` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `author_custom_date` | date DEFAULT NULL | oui | NULL |  | date |
| `author_custom_float` | float DEFAULT NULL | oui | NULL |  |  |
| `author_custom_order` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `authorities`

Domaine probable : autorites (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 166992 (borne sup, pas effectif), instructions INSERT : 2, preuve : CREATE TABLE observe (bloc 61/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_authority` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `num_object` | int(9) unsigned NOT NULL DEFAULT 0 | non | 0 | UNIQUE |  |
| `type_object` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | UNIQUE |  |
| `num_statut` | int(2) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |
| `thumbnail_url` | mediumblob NOT NULL | non | — |  |  |

## `authorities_caddie`

Domaine probable : autorites (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 3 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 62/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `idcaddie` | int(8) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI |  |
| `name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `type` | varchar(20) NOT NULL DEFAULT '' | non | '' |  |  |
| `comment` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `autorisations` | mediumtext DEFAULT NULL | oui | NULL |  |  |
| `autorisations_all` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `caddie_classement` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `acces_rapide` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `favorite_color` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `creation_user_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `creation_date` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |

## `authorities_caddie_content`

Domaine probable : autorites (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 63/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `caddie_id` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 | PK | identifiant |
| `object_id` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK | identifiant |
| `flag` | varchar(10) DEFAULT NULL | oui | NULL |  |  |

## `authorities_caddie_procs`

Domaine probable : autorites (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 64/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `idproc` | smallint(5) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI |  |
| `type` | varchar(20) NOT NULL DEFAULT 'SELECT' | non | 'SELECT' |  |  |
| `name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `requete` | blob NOT NULL | non | — |  |  |
| `comment` | tinytext NOT NULL | non | — |  |  |
| `autorisations` | mediumtext DEFAULT NULL | oui | NULL |  |  |
| `autorisations_all` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `parameters` | text DEFAULT NULL | oui | NULL |  |  |

## `authorities_fields_global_index`

Domaine probable : autorites (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 25, preuve : CREATE TABLE observe (bloc 65/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_authority` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK | identifiant |
| `type` | int(5) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `code_champ` | int(10) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `code_ss_champ` | int(3) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `ordre` | int(4) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `value` | text NOT NULL | non | — |  |  |
| `pond` | int(4) NOT NULL DEFAULT 100 | non | 100 |  |  |
| `lang` | varchar(10) NOT NULL DEFAULT '' | non | '' | PK |  |
| `authority_num` | varchar(50) NOT NULL DEFAULT '' | non | '' |  |  |

## `authorities_sources`

Domaine probable : autorites (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 5894 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 66/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_authority_source` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `num_authority` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `authority_number` | varchar(50) NOT NULL DEFAULT '' | non | '' |  |  |
| `authority_type` | varchar(20) NOT NULL DEFAULT '' | non | '' |  |  |
| `num_origin_authority` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `authority_favorite` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `import_date` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `update_date` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |

## `authorities_statuts`

Domaine probable : autorites (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 2 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 67/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_authorities_statut` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `authorities_statut_label` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `authorities_statut_class_html` | varchar(25) NOT NULL DEFAULT '' | non | '' |  |  |
| `authorities_statut_available_for` | text DEFAULT NULL | oui | NULL |  |  |
| `authorities_statuts_autocomplete` | int(1) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |
| `authorities_statuts_searcher_autority` | int(1) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |

## `authorities_words_global_index`

Domaine probable : autorites (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 16, preuve : CREATE TABLE observe (bloc 68/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_authority` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK | identifiant |
| `type` | int(5) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `code_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `code_ss_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `num_word` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `pond` | int(10) unsigned NOT NULL DEFAULT 100 | non | 100 |  |  |
| `position` | int(10) unsigned NOT NULL DEFAULT 1 | non | 1 | PK |  |
| `field_position` | int(10) unsigned NOT NULL DEFAULT 1 | non | 1 | PK |  |

## `authors`

Autorite : auteurs (personnes / collectivites / congres).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 102982 (borne sup, pas effectif), instructions INSERT : 5, preuve : CREATE TABLE observe (bloc 69/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `author_id` | mediumint(8) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `author_type` | enum('70','71','72') NOT NULL DEFAULT '70' | non | '70' |  |  |
| `author_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `author_rejete` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `author_date` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | date |
| `author_see` | mediumint(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `author_web` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `index_author` | text DEFAULT NULL | oui | NULL |  |  |
| `author_comment` | text DEFAULT NULL | oui | NULL |  |  |
| `author_lieu` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `author_ville` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `author_pays` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `author_subdivision` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `author_numero` | varchar(50) NOT NULL DEFAULT '' | non | '' |  |  |
| `author_import_denied` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `author_isni` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |

## `authperso`

Domaine probable : autorites personnalisables (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 70/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_authperso` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `authperso_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `authperso_notice_onglet_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `authperso_isbd_script` | text NOT NULL | non | — |  |  |
| `authperso_view_script` | text NOT NULL | non | — |  |  |
| `authperso_opac_search` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `authperso_opac_multi_search` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `authperso_gestion_search` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `authperso_gestion_multi_search` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `authperso_comment` | text NOT NULL | non | — |  |  |
| `authperso_oeuvre_event` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `authperso_responsability_authperso` | tinyint(4) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `authperso_authorities`

Domaine probable : autorites personnalisables (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 71/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_authperso_authority` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `authperso_authority_authperso_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `authperso_infos_global` | text NOT NULL | non | — |  |  |
| `authperso_index_infos_global` | text NOT NULL | non | — |  |  |

## `authperso_custom`

Domaine probable : autorites personnalisables (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 72/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `idchamp` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI |  |
| `custom_prefixe` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `num_type` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `titre` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `type` | varchar(10) NOT NULL DEFAULT 'text' | non | 'text' |  |  |
| `datatype` | varchar(10) NOT NULL DEFAULT '' | non | '' |  |  |
| `options` | text DEFAULT NULL | oui | NULL |  |  |
| `multiple` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `obligatoire` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `ordre` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `search` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `export` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `filters` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `exclusion_obligatoire` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `pond` | int(11) NOT NULL DEFAULT 100 | non | 100 |  |  |
| `opac_sort` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `comment` | blob NOT NULL | non | — |  |  |
| `custom_classement` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |

## `authperso_custom_dates`

Domaine probable : autorites personnalisables (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 73/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `authperso_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `authperso_custom_origine` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `authperso_custom_date_type` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `authperso_custom_date_start` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `authperso_custom_date_end` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `authperso_custom_order` | int(11) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |

## `authperso_custom_lists`

Domaine probable : autorites personnalisables (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 74/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_authperso_custom_list` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `authperso_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `authperso_custom_list_value` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `authperso_custom_list_lib` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `ordre` | int(11) DEFAULT NULL | oui | NULL |  |  |

## `authperso_custom_values`

Domaine probable : autorites personnalisables (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 75/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `authperso_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `authperso_custom_origine` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `authperso_custom_small_text` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `authperso_custom_text` | text DEFAULT NULL | oui | NULL |  |  |
| `authperso_custom_integer` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `authperso_custom_date` | date DEFAULT NULL | oui | NULL |  | date |
| `authperso_custom_float` | float DEFAULT NULL | oui | NULL |  |  |
| `authperso_custom_order` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `avis`

Avis des lecteurs sur notices.

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 40 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 76/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_avis` | mediumint(8) NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `num_empr` | mediumint(8) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_notice` | mediumint(8) NOT NULL DEFAULT 0 | non | 0 |  | lien suppose -> notices.notice_id |
| `type_object` | mediumint(8) NOT NULL | non | — |  |  |
| `note` | int(3) DEFAULT NULL | oui | NULL |  |  |
| `sujet` | text DEFAULT NULL | oui | NULL |  |  |
| `commentaire` | text DEFAULT NULL | oui | NULL |  |  |
| `dateajout` | timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp() | non | current_timestamp() |  |  |
| `valide` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `avis_rank` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `avis_private` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `avis_num_liste_lecture` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `bannette_abon`

Domaine probable : DSI / bannettes (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 77/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_bannette` | int(9) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `num_empr` | int(9) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `actif` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `bannette_mail` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | donnee perso RGPD |

## `bannette_contenu`

Domaine probable : DSI / bannettes (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 78/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_bannette` | int(9) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `num_notice` | int(9) unsigned NOT NULL DEFAULT 0 | non | 0 | PK | lien suppose -> notices.notice_id |
| `date_ajout` | timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp() | non | current_timestamp() |  | date |

## `bannette_empr_categs`

Domaine probable : DSI / bannettes (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 79/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `empr_categ_num_bannette` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK | champ adherent |
| `empr_categ_num_categ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK | champ adherent |

## `bannette_empr_groupes`

Domaine probable : DSI / bannettes (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 80/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `empr_groupe_num_bannette` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK | champ adherent |
| `empr_groupe_num_groupe` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK | champ adherent |

## `bannette_equation`

Domaine probable : DSI / bannettes (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 81/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_bannette` | int(9) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `num_equation` | int(9) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |

## `bannette_exports`

Domaine probable : DSI / bannettes (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 82/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_bannette` | int(11) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `export_format` | int(3) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `export_data` | longblob NOT NULL | non | — |  |  |
| `export_nomfichier` | varchar(255) DEFAULT '' | oui | '' |  |  |

## `bannette_facettes`

Domaine probable : DSI / bannettes (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 83/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_ban_facette` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `ban_facette_critere` | int(5) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `ban_facette_ss_critere` | int(5) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `ban_facette_order` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `ban_facette_order_sort` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `ban_facette_datatype_sort` | varchar(255) NOT NULL DEFAULT 'alpha' | non | 'alpha' |  |  |

## `bannette_tpl`

Domaine probable : DSI / bannettes (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 2 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 84/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `bannettetpl_id` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `bannettetpl_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `bannettetpl_comment` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `bannettetpl_tpl` | text NOT NULL | non | — |  |  |

## `bannettes`

Domaine probable : DSI / bannettes (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 2 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 85/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_bannette` | int(9) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `num_classement` | int(8) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |
| `nom_bannette` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `comment_gestion` | text NOT NULL | non | — |  |  |
| `comment_public` | text NOT NULL | non | — |  |  |
| `entete_mail` | text NOT NULL | non | — |  | donnee perso RGPD |
| `date_last_remplissage` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `date_last_envoi` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `proprio_bannette` | int(9) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `bannette_auto` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `periodicite` | int(3) unsigned NOT NULL DEFAULT 7 | non | 7 |  |  |
| `diffusion_email` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  | donnee perso RGPD |
| `categorie_lecteurs` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `nb_notices_diff` | int(4) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_panier` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `limite_type` | char(1) NOT NULL DEFAULT '' | non | '' |  |  |
| `limite_nombre` | int(6) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `update_type` | char(1) NOT NULL DEFAULT 'C' | non | 'C' |  |  |
| `typeexport` | varchar(20) NOT NULL DEFAULT '' | non | '' |  |  |
| `prefixe_fichier` | varchar(50) NOT NULL DEFAULT '' | non | '' |  |  |
| `param_export` | blob NOT NULL | non | — |  |  |
| `piedpage_mail` | text NOT NULL | non | — |  | donnee perso RGPD |
| `notice_display_type` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `notice_tpl` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `django_directory` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `group_type` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `group_pperso` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `display_notice_in_every_group` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `statut_not_account` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `archive_number` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `document_generate` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `document_notice_display_type` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `document_notice_tpl` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `document_django_directory` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `document_insert_docnum` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `document_group` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `document_add_summary` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `groupe_lecteurs` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `bannette_opac_accueil` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `bannette_tpl_num` | int(6) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `bannette_aff_notice_number` | int(10) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |
| `associated_campaign` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `bannette_num_sender` | int(5) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `bannette_diffusions_history` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `bannettes_descriptors`

Domaine probable : DSI / bannettes (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 86/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_bannette` | int(11) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `num_noeud` | int(11) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `bannette_descriptor_order` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `bannettes_diffusions`

Domaine probable : DSI / bannettes (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 87/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_diffusion` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `diffusion_num_bannette` | int(9) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `diffusion_mail_object` | text DEFAULT NULL | oui | NULL |  | donnee perso RGPD |
| `diffusion_mail_content` | mediumtext DEFAULT NULL | oui | NULL |  | donnee perso RGPD |
| `diffusion_date` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `diffusion_records` | text DEFAULT NULL | oui | NULL |  |  |
| `diffusion_deleted_records` | text DEFAULT NULL | oui | NULL |  |  |
| `diffusion_recipients` | text DEFAULT NULL | oui | NULL |  |  |
| `diffusion_failed_recipients` | text DEFAULT NULL | oui | NULL |  |  |
| `diffusion_equations` | text DEFAULT NULL | oui | NULL |  |  |

## `barcodes_sheets`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 88/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_barcodes_sheet` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `barcodes_sheet_label` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `barcodes_sheet_data` | text NOT NULL | non | — |  |  |
| `barcodes_sheet_order` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `budgets`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 89/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_budget` | int(8) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `num_entite` | int(5) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_exercice` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `libelle` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `commentaires` | text DEFAULT NULL | oui | NULL |  |  |
| `montant_global` | double(12,2) unsigned NOT NULL DEFAULT 0.00 | non | 0.00 |  | montant |
| `seuil_alerte` | int(3) unsigned NOT NULL DEFAULT 100 | non | 100 |  |  |
| `statut` | int(3) unsigned NOT NULL DEFAULT 0 | non | 0 |  | metadonnee catalogue |
| `type_budget` | int(3) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `bulletins`

Bulletin de periodique (exemplaire + depouillement d'articles).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 17141 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 90/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `bulletin_id` | int(8) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `bulletin_numero` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `bulletin_notice` | int(8) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `mention_date` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | date |
| `date_date` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `bulletin_titre` | text DEFAULT NULL | oui | NULL |  | libelle |
| `index_titre` | text DEFAULT NULL | oui | NULL |  | libelle |
| `bulletin_cb` | varchar(30) DEFAULT NULL | oui | NULL |  | code-barres (unique observe) |
| `num_notice` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  | lien suppose -> notices.notice_id |

## `cache_amendes`

Cache calcule des amendes par adherent.

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 91/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_empr` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  | identifiant |
| `cache_date` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `data_amendes` | blob NOT NULL | non | — |  |  |

## `caddie`

Paniers de notices (traitements par lots).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 424 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 92/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `idcaddie` | int(8) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI |  |
| `name` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `type` | varchar(20) NOT NULL DEFAULT 'NOTI' | non | 'NOTI' |  |  |
| `comment` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `autorisations` | mediumtext DEFAULT NULL | oui | NULL |  |  |
| `autorisations_all` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `caddie_classement` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `acces_rapide` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `favorite_color` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `creation_user_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `creation_date` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |

## `caddie_content`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 93/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `caddie_id` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 | PK | identifiant |
| `object_id` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK | identifiant |
| `content` | varchar(100) NOT NULL DEFAULT '' | non | '' | PK |  |
| `blob_type` | varchar(100) DEFAULT '' | oui | '' |  |  |
| `flag` | varchar(10) DEFAULT NULL | oui | NULL |  |  |

## `caddie_procs`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 105 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 94/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `idproc` | smallint(5) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI |  |
| `type` | varchar(20) NOT NULL DEFAULT 'SELECT' | non | 'SELECT' |  |  |
| `name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `requete` | blob NOT NULL | non | — |  |  |
| `comment` | tinytext NOT NULL | non | — |  |  |
| `autorisations` | mediumtext DEFAULT NULL | oui | NULL |  |  |
| `autorisations_all` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `parameters` | text DEFAULT NULL | oui | NULL |  |  |

## `campaigns`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 6 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 95/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_campaign` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `campaign_type` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `campaign_label` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `campaign_date` | datetime DEFAULT NULL | oui | NULL |  | date |
| `campaign_num_user` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `campaigns_descriptors`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 96/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_campaign` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `num_noeud` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `campaign_descriptor_order` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `campaigns_logs`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 97/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `campaign_log_num_campaign` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `campaign_log_num_recipient` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `campaign_log_hash` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `campaign_log_url` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `campaign_log_date` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |

## `campaigns_recipients`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 3539 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 98/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_campaign_recipient` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `campaign_recipient_hash` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `campaign_recipient_num_campaign` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `campaign_recipient_num_empr` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `campaign_recipient_empr_cp` | varchar(5) NOT NULL DEFAULT '' | non | '' |  |  |
| `campaign_recipient_empr_ville` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `campaign_recipient_empr_prof` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `campaign_recipient_empr_year` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `campaign_recipient_empr_categ` | smallint(5) unsigned DEFAULT 0 | oui | 0 |  |  |
| `campaign_recipient_empr_codestat` | smallint(5) unsigned DEFAULT 0 | oui | 0 |  |  |
| `campaign_recipient_empr_sexe` | tinyint(3) unsigned DEFAULT 0 | oui | 0 |  |  |
| `campaign_recipient_empr_statut` | bigint(20) unsigned DEFAULT 0 | oui | 0 |  |  |
| `campaign_recipient_empr_location` | int(6) unsigned DEFAULT 0 | oui | 0 |  |  |

## `campaigns_stats`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 99/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `campaign_stat_num_campaign` | int(11) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `campaign_stat_data` | text NOT NULL | non | — |  |  |
| `campaign_stat_date` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |

## `campaigns_tags`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 100/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_campaign` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `num_tag` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `campaign_tag_order` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `cashdesk`

Domaine probable : caisse (guichet) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 101/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `cashdesk_id` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `cashdesk_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `cashdesk_autorisations` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `cashdesk_transactypes` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `cashdesk_cashbox` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `cashdesk_locations`

Domaine probable : caisse (guichet) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 102/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `cashdesk_loc_cashdesk_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `cashdesk_loc_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |

## `cashdesk_sections`

Domaine probable : caisse (guichet) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 103/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `cashdesk_section_cashdesk_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `cashdesk_section_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |

## `categ_custom`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 104/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `idchamp` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI |  |
| `num_type` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `titre` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `type` | varchar(10) NOT NULL DEFAULT 'text' | non | 'text' |  |  |
| `datatype` | varchar(10) NOT NULL DEFAULT '' | non | '' |  |  |
| `options` | text DEFAULT NULL | oui | NULL |  |  |
| `multiple` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `obligatoire` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `ordre` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `search` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `export` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `filters` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `exclusion_obligatoire` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `pond` | int(11) NOT NULL DEFAULT 100 | non | 100 |  |  |
| `opac_sort` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `comment` | blob NOT NULL | non | — |  |  |
| `custom_classement` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |

## `categ_custom_dates`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 105/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `categ_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `categ_custom_origine` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `categ_custom_date_type` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `categ_custom_date_start` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `categ_custom_date_end` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `categ_custom_order` | int(11) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |

## `categ_custom_lists`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 106/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_categ_custom_list` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `categ_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `categ_custom_list_value` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `categ_custom_list_lib` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `ordre` | int(11) DEFAULT NULL | oui | NULL |  |  |

## `categ_custom_values`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 107/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `categ_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `categ_custom_origine` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `categ_custom_small_text` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `categ_custom_text` | text DEFAULT NULL | oui | NULL |  |  |
| `categ_custom_integer` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `categ_custom_date` | date DEFAULT NULL | oui | NULL |  | date |
| `categ_custom_float` | float DEFAULT NULL | oui | NULL |  |  |
| `categ_custom_order` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `categories`

Autorite : categories matiere du thesaurus.

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 2, preuve : CREATE TABLE observe (bloc 108/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_thesaurus` | int(3) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |
| `num_noeud` | int(9) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `langue` | varchar(5) NOT NULL DEFAULT 'fr_FR' | non | 'fr_FR' | PK |  |
| `libelle_categorie` | text NOT NULL | non | — |  | libelle |
| `note_application` | text NOT NULL | non | — |  |  |
| `comment_public` | text NOT NULL | non | — |  |  |
| `comment_voir` | text NOT NULL | non | — |  |  |
| `index_categorie` | text NOT NULL | non | — |  |  |
| `path_word_categ` | text NOT NULL | non | — |  |  |
| `index_path_word_categ` | text NOT NULL | non | — |  |  |

## `certificates`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 109/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id` | int(11) NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `private_key` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `cert` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |

## `chat_groups`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 110/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_chat_group` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `chat_group_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `chat_group_author_user_type` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `chat_group_author_user_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `chat_messages`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 111/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_chat_message` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `chat_message_from_user_type` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `chat_message_from_user_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `chat_message_to_user_type` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `chat_message_to_user_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `chat_message_text` | text NOT NULL | non | — |  |  |
| `chat_message_file` | blob DEFAULT NULL | oui | NULL |  |  |
| `chat_message_read` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `chat_message_date` | timestamp NOT NULL DEFAULT current_timestamp() | non | current_timestamp() |  | date |

## `chat_users_groups`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 112/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `chat_user_group_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `chat_user_group_user_type` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `chat_user_group_user_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `chat_user_group_unread_messages_number` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `classements`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 2 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 113/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_classement` | int(8) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `type_classement` | char(3) NOT NULL DEFAULT 'BAN' | non | 'BAN' |  |  |
| `nom_classement` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `classement_opac_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `classement_order` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `cms`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 2 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 114/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_cms` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `cms_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `cms_comment` | text NOT NULL | non | — |  |  |
| `cms_opac_default` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `cms_opac_view_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `cms_articles`

Domaine probable : portail CMS (hors perimetre de reprise a priori) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 1436 (borne sup, pas effectif), instructions INSERT : 84, preuve : CREATE TABLE observe (bloc 115/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_article` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `article_title` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `article_resume` | mediumtext NOT NULL | non | — |  |  |
| `article_contenu` | mediumtext NOT NULL | non | — |  |  |
| `article_logo` | mediumblob NOT NULL | non | — |  |  |
| `article_publication_state` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `article_start_date` | datetime DEFAULT NULL | oui | NULL |  | date |
| `article_end_date` | datetime DEFAULT NULL | oui | NULL |  | date |
| `num_section` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `article_num_type` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `article_creation_date` | datetime DEFAULT NULL | oui | NULL |  | date |
| `article_order` | int(10) unsigned DEFAULT 0 | oui | 0 |  |  |
| `article_update_timestamp` | timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp() | non | current_timestamp() |  |  |

## `cms_articles_descriptors`

Domaine probable : portail CMS (hors perimetre de reprise a priori) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 116/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_article` | int(11) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `num_noeud` | int(11) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `article_descriptor_order` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `cms_build`

Domaine probable : portail CMS (hors perimetre de reprise a priori) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 74788 (borne sup, pas effectif), instructions INSERT : 3, preuve : CREATE TABLE observe (bloc 117/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_build` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `build_version_num` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `build_type` | varchar(255) NOT NULL DEFAULT 'cadre' | non | 'cadre' |  |  |
| `build_fixed` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `build_obj` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `build_page` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `build_parent` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `build_child_before` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `build_child_after` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `build_css` | text NOT NULL | non | — |  |  |
| `build_div` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `cms_cache_cadres`

Domaine probable : portail CMS (hors perimetre de reprise a priori) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 46, preuve : CREATE TABLE observe (bloc 118/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `cache_cadre_hash` | varchar(32) NOT NULL | non | — | PK |  |
| `cache_cadre_type_content` | varchar(30) NOT NULL | non | — | PK |  |
| `cache_cadre_create_date` | timestamp NOT NULL DEFAULT current_timestamp() | non | current_timestamp() |  | date |
| `cache_cadre_content` | mediumtext NOT NULL | non | — |  |  |
| `cache_cadre_header` | mediumtext NOT NULL | non | — |  |  |

## `cms_cadre_content`

Domaine probable : portail CMS (hors perimetre de reprise a priori) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 1260 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 119/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_cadre_content` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `cadre_content_hash` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `cadre_content_type` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `cadre_content_object` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `cadre_content_num_cadre` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `cadre_content_data` | text NOT NULL | non | — |  |  |
| `cadre_content_num_cadre_content` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `cms_cadres`

Domaine probable : portail CMS (hors perimetre de reprise a priori) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 217 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 120/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_cadre` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `cadre_hash` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `cadre_object` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `cadre_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `cadre_fixed` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `cadre_styles` | text NOT NULL | non | — |  |  |
| `cadre_dom_parent` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `cadre_dom_after` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `cadre_url` | text NOT NULL | non | — |  |  |
| `cadre_memo_url` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `cadre_classement` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `cadre_modcache` | varchar(255) NOT NULL DEFAULT 'get_post_view' | non | 'get_post_view' |  |  |
| `cadre_css_class` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |

## `cms_collections`

Domaine probable : portail CMS (hors perimetre de reprise a priori) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 2 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 121/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_collection` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `collection_title` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `collection_description` | text NOT NULL | non | — |  |  |
| `collection_num_parent` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `collection_num_storage` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `cms_documents`

Domaine probable : portail CMS (hors perimetre de reprise a priori) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 81 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 122/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_document` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `document_title` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `document_description` | text NOT NULL | non | — |  |  |
| `document_filename` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `document_mimetype` | varchar(100) NOT NULL DEFAULT '' | non | '' |  |  |
| `document_filesize` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `document_vignette` | mediumblob NOT NULL | non | — |  |  |
| `document_url` | text NOT NULL | non | — |  |  |
| `document_path` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `document_create_date` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `document_num_storage` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `document_type_object` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `document_num_object` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `cms_documents_links`

Domaine probable : portail CMS (hors perimetre de reprise a priori) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 123/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `document_link_type_object` | varchar(255) NOT NULL DEFAULT '' | non | '' | PK |  |
| `document_link_num_object` | int(11) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `document_link_num_document` | int(11) NOT NULL DEFAULT 0 | non | 0 | PK |  |

## `cms_editorial_custom`

Domaine probable : portail CMS (hors perimetre de reprise a priori) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 80 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 124/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `idchamp` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI |  |
| `num_type` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `titre` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `type` | varchar(10) NOT NULL DEFAULT 'text' | non | 'text' |  |  |
| `datatype` | varchar(10) NOT NULL DEFAULT '' | non | '' |  |  |
| `options` | text DEFAULT NULL | oui | NULL |  |  |
| `multiple` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `obligatoire` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `ordre` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `search` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `export` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `filters` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `exclusion_obligatoire` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `pond` | int(11) NOT NULL DEFAULT 100 | non | 100 |  |  |
| `opac_sort` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `comment` | blob NOT NULL | non | — |  |  |
| `custom_classement` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |

## `cms_editorial_custom_dates`

Domaine probable : portail CMS (hors perimetre de reprise a priori) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 125/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `cms_editorial_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `cms_editorial_custom_origine` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `cms_editorial_custom_date_type` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `cms_editorial_custom_date_start` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `cms_editorial_custom_date_end` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `cms_editorial_custom_order` | int(11) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |

## `cms_editorial_custom_lists`

Domaine probable : portail CMS (hors perimetre de reprise a priori) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 15 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 126/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_cms_editorial_custom_list` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `cms_editorial_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `cms_editorial_custom_list_value` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `cms_editorial_custom_list_lib` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `ordre` | int(11) DEFAULT NULL | oui | NULL |  |  |

## `cms_editorial_custom_values`

Domaine probable : portail CMS (hors perimetre de reprise a priori) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 6, preuve : CREATE TABLE observe (bloc 127/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `cms_editorial_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `cms_editorial_custom_origine` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `cms_editorial_custom_small_text` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `cms_editorial_custom_text` | mediumtext DEFAULT NULL | oui | NULL |  |  |
| `cms_editorial_custom_integer` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `cms_editorial_custom_date` | date DEFAULT NULL | oui | NULL |  | date |
| `cms_editorial_custom_float` | float DEFAULT NULL | oui | NULL |  |  |
| `cms_editorial_custom_order` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `cms_editorial_fields_global_index`

Domaine probable : portail CMS (hors perimetre de reprise a priori) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 128/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_obj` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `type` | varchar(20) NOT NULL DEFAULT '' | non | '' | PK |  |
| `code_champ` | int(3) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `code_ss_champ` | int(3) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `ordre` | int(4) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `value` | text NOT NULL | non | — |  |  |
| `pond` | int(4) NOT NULL DEFAULT 100 | non | 100 |  |  |
| `lang` | varchar(10) NOT NULL DEFAULT '' | non | '' | PK |  |
| `authority_num` | varchar(50) NOT NULL DEFAULT '' | non | '' |  |  |

## `cms_editorial_publications_states`

Domaine probable : portail CMS (hors perimetre de reprise a priori) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 5 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 129/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_publication_state` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `editorial_publication_state_label` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `editorial_publication_state_opac_show` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `editorial_publication_state_auth_opac_show` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `editorial_publication_state_class_html` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |

## `cms_editorial_types`

Domaine probable : portail CMS (hors perimetre de reprise a priori) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 22 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 130/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_editorial_type` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `editorial_type_element` | varchar(20) NOT NULL DEFAULT '' | non | '' |  |  |
| `editorial_type_label` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `editorial_type_comment` | text NOT NULL | non | — |  |  |
| `editorial_type_extension` | text NOT NULL | non | — |  |  |
| `editorial_type_permalink_num_page` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `editorial_type_permalink_var_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |

## `cms_editorial_words_global_index`

Domaine probable : portail CMS (hors perimetre de reprise a priori) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 2, preuve : CREATE TABLE observe (bloc 131/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_obj` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `type` | varchar(20) NOT NULL DEFAULT '' | non | '' | PK |  |
| `code_champ` | int(11) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `code_ss_champ` | int(11) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `num_word` | int(11) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `pond` | int(11) NOT NULL DEFAULT 100 | non | 100 |  |  |
| `position` | int(11) NOT NULL DEFAULT 1 | non | 1 | PK |  |

## `cms_hash`

Domaine probable : portail CMS (hors perimetre de reprise a priori) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 132/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `hash` | varchar(255) NOT NULL DEFAULT '' | non | '' | PK |  |

## `cms_managed_modules`

Domaine probable : portail CMS (hors perimetre de reprise a priori) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 133/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `managed_module_name` | varchar(255) NOT NULL DEFAULT '' | non | '' | PK | libelle |
| `managed_module_box` | text NOT NULL | non | — |  |  |

## `cms_modules_extensions_datas`

Domaine probable : portail CMS (hors perimetre de reprise a priori) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 134/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_extension_datas` | int(10) NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `extension_datas_module` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `extension_datas_type` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `extension_datas_type_element` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `extension_datas_num_element` | int(10) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `extension_datas_datas` | blob DEFAULT NULL | oui | NULL |  |  |

## `cms_pages`

Domaine probable : portail CMS (hors perimetre de reprise a priori) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 15 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 135/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_page` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `page_hash` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `page_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `page_description` | text NOT NULL | non | — |  |  |
| `page_classement` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |

## `cms_pages_env`

Domaine probable : portail CMS (hors perimetre de reprise a priori) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 136/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `page_env_num_page` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI |  |
| `page_env_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `page_env_id_selector` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |

## `cms_sections`

Domaine probable : portail CMS (hors perimetre de reprise a priori) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 149 (borne sup, pas effectif), instructions INSERT : 14, preuve : CREATE TABLE observe (bloc 137/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_section` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `section_title` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `section_resume` | mediumtext NOT NULL | non | — |  |  |
| `section_logo` | mediumblob NOT NULL | non | — |  |  |
| `section_publication_state` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `section_start_date` | datetime DEFAULT NULL | oui | NULL |  | date |
| `section_end_date` | datetime DEFAULT NULL | oui | NULL |  | date |
| `section_num_parent` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `section_num_type` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `section_creation_date` | datetime DEFAULT NULL | oui | NULL |  | date |
| `section_order` | int(10) unsigned DEFAULT 0 | oui | 0 |  |  |
| `section_update_timestamp` | timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp() | non | current_timestamp() |  |  |

## `cms_sections_descriptors`

Domaine probable : portail CMS (hors perimetre de reprise a priori) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 138/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_section` | int(11) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `num_noeud` | int(11) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `section_descriptor_order` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `cms_toolkits`

Domaine probable : portail CMS (hors perimetre de reprise a priori) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 139/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `cms_toolkit_name` | varchar(255) NOT NULL DEFAULT '' | non | '' | PK | libelle |
| `cms_toolkit_active` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `cms_toolkit_data` | text NOT NULL | non | — |  |  |
| `cms_toolkit_order` | int(3) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `cms_vars`

Domaine probable : portail CMS (hors perimetre de reprise a priori) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 23 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 140/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_var` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `var_num_page` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `var_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `var_comment` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |

## `cms_version`

Domaine probable : portail CMS (hors perimetre de reprise a priori) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 1046 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 141/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_version` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `version_cms_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `version_date` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `version_comment` | text NOT NULL | non | — |  |  |
| `version_public` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `version_user` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `collection_custom`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 142/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `idchamp` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI |  |
| `num_type` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `titre` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `type` | varchar(10) NOT NULL DEFAULT 'text' | non | 'text' |  |  |
| `datatype` | varchar(10) NOT NULL DEFAULT '' | non | '' |  |  |
| `options` | text DEFAULT NULL | oui | NULL |  |  |
| `multiple` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `obligatoire` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `ordre` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `search` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `export` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `filters` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `exclusion_obligatoire` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `pond` | int(11) NOT NULL DEFAULT 100 | non | 100 |  |  |
| `opac_sort` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `comment` | blob NOT NULL | non | — |  |  |
| `custom_classement` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |

## `collection_custom_dates`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 143/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `collection_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `collection_custom_origine` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `collection_custom_date_type` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `collection_custom_date_start` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `collection_custom_date_end` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `collection_custom_order` | int(11) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |

## `collection_custom_lists`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 144/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_collection_custom_list` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `collection_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `collection_custom_list_value` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `collection_custom_list_lib` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `ordre` | int(11) DEFAULT NULL | oui | NULL |  |  |

## `collection_custom_values`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 145/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `collection_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `collection_custom_origine` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `collection_custom_small_text` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `collection_custom_text` | text DEFAULT NULL | oui | NULL |  |  |
| `collection_custom_integer` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `collection_custom_date` | date DEFAULT NULL | oui | NULL |  | date |
| `collection_custom_float` | float DEFAULT NULL | oui | NULL |  |  |
| `collection_custom_order` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `collections`

Autorite : collections editoriales.

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 15143 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 146/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `collection_id` | mediumint(8) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `collection_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `collection_parent` | mediumint(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `collection_issn` | varchar(12) NOT NULL DEFAULT '' | non | '' |  |  |
| `index_coll` | text DEFAULT NULL | oui | NULL |  |  |
| `collection_web` | text NOT NULL | non | — |  |  |
| `collection_comment` | text NOT NULL | non | — |  |  |
| `authority_import_denied` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `collections_state`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 2 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 147/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `collstate_id` | int(8) NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `id_serial` | mediumint(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  | identifiant |
| `location_id` | smallint(5) unsigned NOT NULL DEFAULT 0 | non | 0 |  | identifiant |
| `state_collections` | text NOT NULL | non | — |  |  |
| `collstate_emplacement` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `collstate_type` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `collstate_origine` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `collstate_cote` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `collstate_archive` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `collstate_statut` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `collstate_lacune` | text NOT NULL | non | — |  |  |
| `collstate_note` | text NOT NULL | non | — |  |  |

## `collstate_bulletins`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 148/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `collstate_bulletins_num_collstate` | int(8) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `collstate_bulletins_num_bulletin` | int(8) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `collstate_bulletins_order` | int(8) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `collstate_custom`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 149/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `idchamp` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI |  |
| `name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `titre` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `type` | varchar(10) NOT NULL DEFAULT 'text' | non | 'text' |  |  |
| `datatype` | varchar(10) NOT NULL DEFAULT '' | non | '' |  |  |
| `options` | text DEFAULT NULL | oui | NULL |  |  |
| `multiple` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `obligatoire` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `ordre` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `search` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `export` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `filters` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `exclusion_obligatoire` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `pond` | int(11) NOT NULL DEFAULT 100 | non | 100 |  |  |
| `opac_sort` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `comment` | blob NOT NULL | non | — |  |  |
| `custom_classement` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |

## `collstate_custom_dates`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 150/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `collstate_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `collstate_custom_origine` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `collstate_custom_date_type` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `collstate_custom_date_start` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `collstate_custom_date_end` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `collstate_custom_order` | int(11) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |

## `collstate_custom_lists`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 151/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_collstate_custom_list` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `collstate_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `collstate_custom_list_value` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `collstate_custom_list_lib` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `ordre` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `collstate_custom_values`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 152/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `collstate_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `collstate_custom_origine` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `collstate_custom_small_text` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `collstate_custom_text` | text DEFAULT NULL | oui | NULL |  |  |
| `collstate_custom_integer` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `collstate_custom_date` | date DEFAULT NULL | oui | NULL |  | date |
| `collstate_custom_float` | float DEFAULT NULL | oui | NULL |  |  |
| `collstate_custom_order` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `comptes`

Comptes adherents (~2 par lecteur : types 1/2, solde, prepaye).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 19018 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 153/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_compte` | int(8) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `libelle` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `type_compte_id` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  | identifiant |
| `solde` | decimal(16,2) DEFAULT 0.00 | oui | 0.00 |  | montant |
| `prepay_mnt` | decimal(16,2) NOT NULL DEFAULT 0.00 | non | 0.00 |  | montant |
| `proprio_id` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  | identifiant |
| `droits` | text NOT NULL | non | — |  |  |

## `connectors`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 154/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `connector_id` | varchar(20) NOT NULL DEFAULT '' | non | '' | PK | identifiant |
| `parameters` | text NOT NULL | non | — |  |  |
| `repository` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `timeout` | int(11) NOT NULL DEFAULT 5 | non | 5 |  |  |
| `retry` | int(11) NOT NULL DEFAULT 3 | non | 3 |  |  |
| `ttl` | int(11) NOT NULL DEFAULT 1440 | non | 1440 |  |  |

## `connectors_categ`

Domaine probable : connecteurs (OAI, sources externes) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 155/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `connectors_categ_id` | smallint(5) NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `connectors_categ_name` | varchar(64) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `opac_expanded` | smallint(6) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `connectors_categ_sources`

Domaine probable : connecteurs (OAI, sources externes) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 156/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_categ` | smallint(6) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `num_source` | smallint(6) NOT NULL DEFAULT 0 | non | 0 | PK |  |

## `connectors_out`

Domaine probable : connecteurs (OAI, sources externes) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 12 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 157/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `connectors_out_id` | int(11) NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `connectors_out_config` | longblob NOT NULL | non | — |  |  |

## `connectors_out_oai_deleted_records`

Domaine probable : connecteurs (OAI, sources externes) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 158/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_set` | int(11) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `num_notice` | int(11) unsigned NOT NULL DEFAULT 0 | non | 0 | PK | lien suppose -> notices.notice_id |
| `deletion_date` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |

## `connectors_out_oai_tokens`

Domaine probable : connecteurs (OAI, sources externes) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 159/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `connectors_out_oai_token_token` | varchar(32) NOT NULL | non | — | PK | SECRET : ne pas reprendre (reinitialiser cote cible) |
| `connectors_out_oai_token_environnement` | text NOT NULL | non | — |  | SECRET : ne pas reprendre (reinitialiser cote cible) |
| `connectors_out_oai_token_expirationdate` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | SECRET : ne pas reprendre (reinitialiser cote cible) |

## `connectors_out_setcache_values`

Domaine probable : connecteurs (OAI, sources externes) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 160/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `connectors_out_setcache_values_cachenum` | int(11) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `connectors_out_setcache_values_value` | int(11) NOT NULL DEFAULT 0 | non | 0 | PK |  |

## `connectors_out_setcaches`

Domaine probable : connecteurs (OAI, sources externes) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 3 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 161/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `connectors_out_setcache_id` | int(11) NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `connectors_out_setcache_setnum` | int(11) NOT NULL DEFAULT 0 | non | 0 | UNIQUE |  |
| `connectors_out_setcache_lifeduration` | int(4) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `connectors_out_setcache_lifeduration_unit` | enum('seconds','minutes','hours','days','weeks','months') NOT NULL DEFAULT 'seconds' | non | 'seconds' |  |  |
| `connectors_out_setcache_lastupdatedate` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE |  |

## `connectors_out_setcateg_sets`

Domaine probable : connecteurs (OAI, sources externes) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 162/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `connectors_out_setcategset_setnum` | int(11) NOT NULL | non | — | PK |  |
| `connectors_out_setcategset_categnum` | int(11) NOT NULL DEFAULT 0 | non | 0 | PK |  |

## `connectors_out_setcategs`

Domaine probable : connecteurs (OAI, sources externes) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 3 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 163/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `connectors_out_setcateg_id` | int(11) NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `connectors_out_setcateg_name` | varchar(100) NOT NULL DEFAULT '' | non | '' | UNIQUE | libelle |

## `connectors_out_sets`

Domaine probable : connecteurs (OAI, sources externes) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 3 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 164/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `connector_out_set_id` | int(11) NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `connector_out_set_caption` | varchar(100) NOT NULL DEFAULT '' | non | '' | UNIQUE |  |
| `connector_out_set_type` | int(4) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `connector_out_set_config` | longblob NOT NULL | non | — |  |  |
| `being_refreshed` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `connectors_out_sources`

Domaine probable : connecteurs (OAI, sources externes) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 5 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 165/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `connectors_out_source_id` | int(11) NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `connectors_out_sources_connectornum` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `connectors_out_source_name` | varchar(100) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `connectors_out_source_comment` | varchar(200) NOT NULL DEFAULT '' | non | '' |  |  |
| `connectors_out_source_config` | longblob NOT NULL | non | — |  |  |

## `connectors_out_sources_esgroups`

Domaine probable : connecteurs (OAI, sources externes) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 166/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `connectors_out_source_esgroup_sourcenum` | int(11) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `connectors_out_source_esgroup_esgroupnum` | int(11) NOT NULL DEFAULT 0 | non | 0 | PK |  |

## `connectors_sources`

Domaine probable : connecteurs (OAI, sources externes) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 7 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 167/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `source_id` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `id_connector` | varchar(20) NOT NULL DEFAULT '' | non | '' |  | identifiant |
| `parameters` | mediumtext NOT NULL | non | — |  |  |
| `comment` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `repository` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `timeout` | int(11) NOT NULL DEFAULT 5 | non | 5 |  |  |
| `retry` | int(11) NOT NULL DEFAULT 3 | non | 3 |  |  |
| `ttl` | int(11) NOT NULL DEFAULT 1440 | non | 1440 |  |  |
| `opac_allowed` | int(3) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `rep_upload` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `upload_doc_num` | int(11) NOT NULL DEFAULT 1 | non | 1 |  |  |
| `enrichment` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `opac_affiliate_search` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `opac_selected` | int(3) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `gestion_selected` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `type_enrichment_allowed` | text NOT NULL | non | — |  |  |
| `ico_notice` | varchar(256) NOT NULL DEFAULT '' | non | '' |  |  |
| `last_sync_date` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `clean_html` | int(3) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `contact_form_objects`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 6 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 168/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_object` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `object_label` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `object_message` | text NOT NULL | non | — |  |  |
| `num_contact_form` | int(11) NOT NULL DEFAULT 1 | non | 1 |  |  |

## `contact_forms`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 3 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 169/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_contact_form` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `contact_form_label` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `contact_form_desc` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `contact_form_parameters` | mediumtext NOT NULL | non | — |  |  |
| `contact_form_recipients` | mediumtext NOT NULL | non | — |  |  |

## `contribution_area_areas`

Domaine probable : espace de contribution OPAC (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 170/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_area` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `area_title` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `area_comment` | text NOT NULL | non | — |  |  |
| `area_color` | varchar(10) NOT NULL DEFAULT '' | non | '' |  |  |
| `area_order` | int(5) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `area_status` | int(10) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |
| `area_opac_visibility` | int(1) NOT NULL DEFAULT 1 | non | 1 |  |  |
| `area_repo_template_authorities` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `area_repo_template_records` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `area_editing_entity` | tinyint(4) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `area_logo` | varchar(255) DEFAULT NULL | oui | NULL |  |  |

## `contribution_area_clipboard`

Domaine probable : espace de contribution OPAC (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 171/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_clipboard` | int(11) NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `datas` | text DEFAULT NULL | oui | NULL |  |  |
| `created_at` | datetime DEFAULT NULL | oui | NULL |  |  |

## `contribution_area_computed_fields`

Domaine probable : espace de contribution OPAC (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 172/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_computed_fields` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `computed_fields_area_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `computed_fields_field_num` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `computed_fields_template` | text DEFAULT NULL | oui | NULL |  |  |

## `contribution_area_computed_fields_used`

Domaine probable : espace de contribution OPAC (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 173/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_computed_fields_used` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `computed_fields_used_origine_field_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `computed_fields_used_label` | text DEFAULT NULL | oui | NULL |  |  |
| `computed_fields_used_num` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `computed_fields_used_alias` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |

## `contribution_area_datastore_g2t`

Domaine probable : espace de contribution OPAC (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 174/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `g` | mediumint(8) unsigned NOT NULL | non | — | UNIQUE |  |
| `t` | mediumint(8) unsigned NOT NULL | non | — | UNIQUE |  |

## `contribution_area_datastore_id2val`

Domaine probable : espace de contribution OPAC (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 731 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 175/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id` | mediumint(8) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,UNIQUE,AI | identifiant |
| `misc` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `val` | text NOT NULL | non | — |  |  |
| `val_type` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 | UNIQUE |  |

## `contribution_area_datastore_o2val`

Domaine probable : espace de contribution OPAC (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 176/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id` | mediumint(8) unsigned NOT NULL | non | — | UNIQUE | identifiant |
| `misc` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `val_hash` | char(32) NOT NULL | non | — |  |  |
| `val` | text NOT NULL | non | — |  |  |

## `contribution_area_datastore_s2val`

Domaine probable : espace de contribution OPAC (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 177/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id` | mediumint(8) unsigned NOT NULL | non | — | UNIQUE | identifiant |
| `misc` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `val_hash` | char(32) NOT NULL | non | — |  |  |
| `val` | text NOT NULL | non | — |  |  |

## `contribution_area_datastore_setting`

Domaine probable : espace de contribution OPAC (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 178/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `k` | char(32) NOT NULL | non | — | UNIQUE |  |
| `val` | text NOT NULL | non | — |  |  |

## `contribution_area_datastore_triple`

Domaine probable : espace de contribution OPAC (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 179/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `t` | mediumint(8) unsigned NOT NULL | non | — | UNIQUE |  |
| `s` | mediumint(8) unsigned NOT NULL | non | — |  |  |
| `p` | mediumint(8) unsigned NOT NULL | non | — |  |  |
| `o` | mediumint(8) unsigned NOT NULL | non | — |  |  |
| `o_lang_dt` | mediumint(8) unsigned NOT NULL | non | — |  |  |
| `o_comp` | char(35) NOT NULL | non | — |  |  |
| `s_type` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `o_type` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `misc` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `contribution_area_equations`

Domaine probable : espace de contribution OPAC (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 180/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `contribution_area_equation_id` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `contribution_area_equation_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `contribution_area_equation_type` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `contribution_area_equation_query` | text NOT NULL | non | — |  |  |
| `contribution_area_equation_human_query` | text NOT NULL | non | — |  |  |

## `contribution_area_forms`

Domaine probable : espace de contribution OPAC (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 181/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_form` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `form_title` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `form_type` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `form_parameters` | blob NOT NULL | non | — |  |  |
| `form_comment` | text NOT NULL | non | — |  |  |

## `contribution_area_status`

Domaine probable : espace de contribution OPAC (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 2 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 182/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `contribution_area_status_id` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `contribution_area_status_gestion_libelle` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `contribution_area_status_opac_libelle` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `contribution_area_status_class_html` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `contribution_area_status_available_for` | text DEFAULT NULL | oui | NULL |  |  |

## `coordonnees`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 183/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_contact` | int(8) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `type_coord` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_entite` | int(5) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `libelle` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `contact` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `adr1` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `adr2` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `cp` | varchar(15) NOT NULL DEFAULT '' | non | '' |  |  |
| `ville` | varchar(100) NOT NULL DEFAULT '' | non | '' |  |  |
| `etat` | varchar(100) NOT NULL DEFAULT '' | non | '' |  |  |
| `pays` | varchar(100) NOT NULL DEFAULT '' | non | '' |  |  |
| `tel1` | varchar(100) NOT NULL DEFAULT '' | non | '' |  |  |
| `tel2` | varchar(100) NOT NULL DEFAULT '' | non | '' |  |  |
| `fax` | varchar(100) NOT NULL DEFAULT '' | non | '' |  |  |
| `email` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | donnee perso RGPD |
| `commentaires` | text DEFAULT NULL | oui | NULL |  |  |

## `custom_fields_groups`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 184/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_group` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `group_type` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `group_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `group_title` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `group_title_button_add` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `group_fields` | mediumtext DEFAULT NULL | oui | NULL |  |  |

## `dashboard`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 185/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_dashboard` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `dashboard_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `dashboard_editable` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_user` | int(5) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `dashboard_users_groups`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 186/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_dashboard` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `num_users_groups` | int(11) NOT NULL DEFAULT 0 | non | 0 | PK |  |

## `dashboard_widget`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 187/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_dashboard` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `num_widget` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `dashboard_widget_settings` | mediumblob NOT NULL | non | — |  |  |

## `db_update_logs`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 129 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 188/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_db_update_log` | int(11) NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `db_update_log_type` | varchar(10) NOT NULL DEFAULT '' | non | '' |  |  |
| `db_update_log_version` | varchar(50) NOT NULL DEFAULT '' | non | '' |  |  |
| `db_update_log_query` | text NOT NULL DEFAULT '' | non | '' |  |  |
| `db_update_log_message` | varchar(1000) NOT NULL DEFAULT '' | non | '' |  |  |
| `db_update_log_error` | int(10) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `db_update_log_result` | varchar(1000) NOT NULL DEFAULT '' | non | '' |  |  |
| `db_update_log_date` | datetime NOT NULL DEFAULT current_timestamp() | non | current_timestamp() |  | date |

## `demandes`

Demandes (numerisation, animation...).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 189/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_demande` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `num_demandeur` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `theme_demande` | int(3) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `type_demande` | int(3) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `etat_demande` | int(3) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `date_demande` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `date_prevue` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `deadline_demande` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE |  |
| `titre_demande` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `sujet_demande` | text NOT NULL | non | — |  |  |
| `progression` | mediumint(3) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_user_cloture` | mediumint(3) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_notice` | int(10) NOT NULL DEFAULT 0 | non | 0 |  | lien suppose -> notices.notice_id |
| `dmde_read_gestion` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `reponse_finale` | text DEFAULT NULL | oui | NULL |  |  |
| `dmde_read_opac` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `demande_note_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_linked_notice` | mediumint(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `demandes_actions`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 190/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_action` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `type_action` | int(3) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `statut_action` | int(3) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `sujet_action` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `detail_action` | text NOT NULL | non | — |  |  |
| `date_action` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `deadline_action` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE |  |
| `temps_passe` | float DEFAULT NULL | oui | NULL |  |  |
| `cout` | mediumint(3) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `progression_action` | mediumint(3) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `prive_action` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_demande` | int(10) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `actions_num_user` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `actions_type_user` | tinyint(4) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `actions_read_opac` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `actions_read_gestion` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `demandes_custom`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 191/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `idchamp` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI |  |
| `name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `titre` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `type` | varchar(10) NOT NULL DEFAULT 'text' | non | 'text' |  |  |
| `datatype` | varchar(10) NOT NULL DEFAULT '' | non | '' |  |  |
| `options` | text DEFAULT NULL | oui | NULL |  |  |
| `multiple` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `obligatoire` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `ordre` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `search` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `export` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `filters` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `exclusion_obligatoire` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `pond` | int(11) NOT NULL DEFAULT 100 | non | 100 |  |  |
| `opac_sort` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `comment` | blob NOT NULL | non | — |  |  |
| `custom_classement` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |

## `demandes_custom_dates`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 192/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `demandes_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `demandes_custom_origine` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `demandes_custom_date_type` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `demandes_custom_date_start` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `demandes_custom_date_end` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `demandes_custom_order` | int(11) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |

## `demandes_custom_lists`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 193/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_demandes_custom_list` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `demandes_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `demandes_custom_list_value` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `demandes_custom_list_lib` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `ordre` | int(11) DEFAULT NULL | oui | NULL |  |  |

## `demandes_custom_values`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 194/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `demandes_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `demandes_custom_origine` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `demandes_custom_small_text` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `demandes_custom_text` | text DEFAULT NULL | oui | NULL |  |  |
| `demandes_custom_integer` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `demandes_custom_date` | date DEFAULT NULL | oui | NULL |  | date |
| `demandes_custom_float` | float DEFAULT NULL | oui | NULL |  |  |
| `demandes_custom_order` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `demandes_notes`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 195/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_note` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `prive` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `rapport` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `contenu` | text NOT NULL | non | — |  |  |
| `date_note` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `num_action` | int(10) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_note_parent` | int(10) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `notes_num_user` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `notes_type_user` | tinyint(4) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `notes_read_gestion` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `notes_read_opac` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `demandes_theme`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 196/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_theme` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `libelle_theme` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `allowed_types` | text NOT NULL | non | — |  |  |

## `demandes_type`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 197/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_type` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `libelle_type` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `allowed_actions` | text NOT NULL | non | — |  |  |
| `allowed_pperso` | text NOT NULL DEFAULT '' | non | '' |  |  |

## `demandes_users`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 198/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_user` | int(10) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `num_demande` | int(10) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `date_creation` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `users_statut` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `digital_signature`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 199/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id` | int(11) NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `type` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `fields` | text NOT NULL | non | — |  |  |
| `upload_folder` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_cert` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `docs_codestat`

Referentiel : code statistique exemplaire.

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 73 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 200/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `idcode` | smallint(5) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI |  |
| `codestat_libelle` | varchar(255) DEFAULT NULL | oui | NULL |  | libelle |
| `statisdoc_codage_import` | char(2) NOT NULL DEFAULT '' | non | '' |  |  |
| `statisdoc_owner` | mediumint(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `docs_location`

Referentiel : sites du reseau (12).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 20 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 201/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `idlocation` | smallint(5) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI |  |
| `location_libelle` | varchar(255) DEFAULT NULL | oui | NULL |  | libelle |
| `locdoc_codage_import` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `locdoc_owner` | mediumint(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `location_pic` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `location_visible_opac` | tinyint(1) NOT NULL DEFAULT 1 | non | 1 |  |  |
| `name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `adr1` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `adr2` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `cp` | varchar(15) NOT NULL DEFAULT '' | non | '' |  |  |
| `town` | varchar(100) NOT NULL DEFAULT '' | non | '' |  |  |
| `state` | varchar(100) NOT NULL DEFAULT '' | non | '' |  |  |
| `country` | varchar(100) NOT NULL DEFAULT '' | non | '' |  |  |
| `phone` | varchar(100) NOT NULL DEFAULT '' | non | '' |  |  |
| `email` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | donnee perso RGPD |
| `website` | varchar(100) NOT NULL DEFAULT '' | non | '' |  |  |
| `logo` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `commentaire` | text NOT NULL | non | — |  |  |
| `transfert_ordre` | smallint(2) unsigned NOT NULL DEFAULT 9999 | non | 9999 |  |  |
| `transfert_statut_defaut` | smallint(5) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_infopage` | int(6) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `css_style` | varchar(100) NOT NULL DEFAULT '' | non | '' |  |  |
| `surloc_num` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `surloc_used` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `show_a2z` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `docs_section`

Referentiel : sections internes.

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 223 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 202/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `idsection` | smallint(5) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI |  |
| `section_libelle` | varchar(255) DEFAULT NULL | oui | NULL |  | libelle |
| `section_libelle_opac` | varchar(255) DEFAULT '' | oui | '' |  |  |
| `sdoc_codage_import` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `sdoc_owner` | mediumint(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `section_pic` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `section_visible_opac` | tinyint(1) NOT NULL DEFAULT 1 | non | 1 |  |  |

## `docs_statut`

Referentiel : statuts d'exemplaire.

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 24 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 203/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `idstatut` | smallint(5) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI |  |
| `statut_libelle` | varchar(255) DEFAULT NULL | oui | NULL |  | libelle |
| `statut_libelle_opac` | varchar(255) DEFAULT '' | oui | '' |  |  |
| `pret_flag` | tinyint(4) NOT NULL DEFAULT 1 | non | 1 |  | champ circulation |
| `statusdoc_codage_import` | char(2) NOT NULL DEFAULT '' | non | '' |  |  |
| `statusdoc_owner` | mediumint(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `transfert_flag` | tinyint(4) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |
| `statut_visible_opac` | tinyint(1) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |
| `statut_allow_resa` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `docs_type`

Referentiel : types de document (+ durees pret/resa).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 298 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 204/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `idtyp_doc` | int(5) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI |  |
| `tdoc_libelle` | varchar(255) DEFAULT NULL | oui | NULL |  | libelle |
| `duree_pret` | smallint(6) NOT NULL DEFAULT 31 | non | 31 |  |  |
| `duree_resa` | int(6) unsigned NOT NULL DEFAULT 15 | non | 15 |  |  |
| `tdoc_owner` | mediumint(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `tdoc_codage_import` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `tarif_pret` | decimal(16,2) NOT NULL DEFAULT 0.00 | non | 0.00 |  | montant |
| `short_loan_duration` | int(6) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |

## `docsloc_section`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 205/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_section` | int(5) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `num_location` | int(5) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `num_pclass` | int(10) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `docwatch_categories`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 12 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 206/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_category` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `category_title` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `category_num_parent` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `category_visible_opac` | int(11) DEFAULT 1 | oui | 1 |  |  |

## `docwatch_datasource_monitoring_website`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 207/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `datasource_monitoring_website_num_datasource` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `datasource_monitoring_website_upload_date` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `datasource_monitoring_website_content` | mediumtext NOT NULL | non | — |  |  |
| `datasource_monitoring_website_content_hash` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |

## `docwatch_datasources`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 49 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 208/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_datasource` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `datasource_type` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `datasource_title` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `datasource_ttl` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `datasource_last_date` | datetime DEFAULT NULL | oui | NULL |  | date |
| `datasource_parameters` | mediumtext NOT NULL | non | — |  |  |
| `datasource_num_category` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `datasource_default_interesting` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `datasource_clean_html` | int(10) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |
| `datasource_boolean_expression` | text DEFAULT NULL | oui | NULL |  |  |
| `datasource_num_watch` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `docwatch_items`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 808 (borne sup, pas effectif), instructions INSERT : 2, preuve : CREATE TABLE observe (bloc 209/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_item` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `item_type` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `item_title` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `item_summary` | mediumtext NOT NULL | non | — |  |  |
| `item_content` | mediumtext NOT NULL | non | — |  |  |
| `item_added_date` | datetime DEFAULT NULL | oui | NULL |  | date |
| `item_publication_date` | datetime DEFAULT NULL | oui | NULL |  | date |
| `item_hash` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `item_url` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `item_logo_url` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `item_status` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `item_interesting` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `item_num_article` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `item_num_section` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `item_num_notice` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `item_num_datasource` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `item_num_watch` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `item_index_sew` | mediumtext NOT NULL | non | — |  |  |
| `item_index_wew` | mediumtext NOT NULL | non | — |  |  |

## `docwatch_items_descriptors`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 210/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_item` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `num_noeud` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |

## `docwatch_items_tags`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 211/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_item` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `num_tag` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |

## `docwatch_selectors`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 45 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 212/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_selector` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `selector_type` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `selector_num_datasource` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `selector_parameters` | mediumtext NOT NULL | non | — |  |  |

## `docwatch_tags`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 213/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_tag` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `tag_title` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |

## `docwatch_watches`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 14 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 214/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_watch` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `watch_title` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `watch_owner` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `watch_allowed_users` | text NOT NULL | non | — |  |  |
| `watch_num_category` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `watch_last_date` | datetime DEFAULT NULL | oui | NULL |  | date |
| `watch_ttl` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `watch_desc` | text NOT NULL | non | — |  |  |
| `watch_logo` | mediumblob NOT NULL | non | — |  |  |
| `watch_logo_url` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `watch_record_default_type` | char(2) NOT NULL DEFAULT 'a' | non | 'a' |  |  |
| `watch_record_default_status` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `watch_record_default_index_lang` | varchar(20) NOT NULL DEFAULT '' | non | '' |  |  |
| `watch_record_default_lang` | varchar(20) NOT NULL DEFAULT '' | non | '' |  |  |
| `watch_record_default_is_new` | tinyint(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `watch_article_default_parent` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `watch_article_default_content_type` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `watch_article_default_publication_status` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `watch_section_default_parent` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `watch_section_default_content_type` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `watch_section_default_publication_status` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `watch_rss_link` | varchar(255) NOT NULL | non | — |  |  |
| `watch_rss_lang` | varchar(255) NOT NULL | non | — |  |  |
| `watch_rss_copyright` | varchar(255) NOT NULL | non | — |  |  |
| `watch_rss_editor` | varchar(255) NOT NULL | non | — |  |  |
| `watch_rss_webmaster` | varchar(255) NOT NULL | non | — |  |  |
| `watch_rss_image_title` | varchar(255) NOT NULL | non | — |  |  |
| `watch_rss_image_website` | varchar(255) NOT NULL | non | — |  |  |
| `watch_boolean_expression` | text DEFAULT NULL | oui | NULL |  |  |
| `watch_visible_opac` | int(11) DEFAULT 1 | oui | 1 |  |  |

## `dsi_archive`

Domaine probable : diffusion selective de l'information (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 215/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_banette_arc` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `num_notice_arc` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK | lien suppose -> notices.notice_id |
| `date_diff_arc` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | PK,DEFAUT MASQUE | date |

## `dsi_channel`

Domaine probable : diffusion selective de l'information (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 216/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_channel` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `settings` | mediumblob NOT NULL | non | — |  |  |
| `type` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `model` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_model` | int(10) unsigned DEFAULT NULL | oui | NULL |  |  |

## `dsi_content_buffer`

Domaine probable : diffusion selective de l'information (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 217/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_content_buffer` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `type` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `content` | longblob NOT NULL | non | — |  |  |
| `modified` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_diffusion_history` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `dsi_content_history`

Domaine probable : diffusion selective de l'information (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 218/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_content_history` | int(11) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `type` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `content` | longblob NOT NULL | non | — |  |  |
| `num_diffusion_history` | int(10) unsigned NOT NULL | non | — |  |  |

## `dsi_diffusion`

Domaine probable : diffusion selective de l'information (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 219/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_diffusion` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `settings` | mediumblob NOT NULL | non | — |  |  |
| `automatic` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_status` | int(10) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |
| `num_subscriber_list` | int(10) unsigned DEFAULT NULL | oui | NULL |  |  |
| `num_item` | int(10) unsigned NOT NULL | non | — |  |  |
| `num_view` | int(10) unsigned NOT NULL | non | — |  |  |
| `num_channel` | int(10) unsigned NOT NULL | non | — |  |  |

## `dsi_diffusion_descriptors`

Domaine probable : diffusion selective de l'information (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 220/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_diffusion` | int(11) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `num_noeud` | int(11) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `diffusion_descriptor_order` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `dsi_diffusion_history`

Domaine probable : diffusion selective de l'information (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 221/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_diffusion_history` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `date` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE |  |
| `total_recipients` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `state` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_diffusion` | int(10) unsigned NOT NULL | non | — |  |  |

## `dsi_diffusion_product`

Domaine probable : diffusion selective de l'information (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 222/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_diffusion` | int(10) unsigned NOT NULL | non | — | PK |  |
| `num_product` | int(10) unsigned NOT NULL | non | — | PK |  |
| `active` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `last_diffusion` | datetime DEFAULT NULL | oui | NULL |  |  |

## `dsi_diffusion_status`

Domaine probable : diffusion selective de l'information (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 2 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 223/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_diffusion_status` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `active` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `dsi_entities_tags`

Domaine probable : diffusion selective de l'information (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 224/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_tag` | int(11) unsigned NOT NULL | non | — | PK |  |
| `num_entity` | int(11) unsigned NOT NULL | non | — | PK |  |
| `type` | int(11) unsigned NOT NULL | non | — | PK |  |

## `dsi_event`

Domaine probable : diffusion selective de l'information (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 225/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_event` | int(11) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `model` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `settings` | mediumblob NOT NULL | non | — |  |  |
| `type` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_model` | int(10) unsigned DEFAULT NULL | oui | NULL |  |  |

## `dsi_event_diffusion`

Domaine probable : diffusion selective de l'information (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 226/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_event` | int(10) unsigned NOT NULL | non | — | PK |  |
| `num_diffusion` | int(10) unsigned NOT NULL | non | — | PK |  |

## `dsi_event_product`

Domaine probable : diffusion selective de l'information (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 227/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_event` | int(10) unsigned NOT NULL | non | — | PK |  |
| `num_product` | int(10) unsigned NOT NULL | non | — | PK |  |

## `dsi_item`

Domaine probable : diffusion selective de l'information (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 228/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_item` | int(11) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `model` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `settings` | mediumblob NOT NULL | non | — |  |  |
| `type` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_model` | int(10) unsigned DEFAULT NULL | oui | NULL |  |  |
| `num_parent` | int(10) unsigned DEFAULT NULL | oui | NULL |  |  |

## `dsi_product`

Domaine probable : diffusion selective de l'information (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 229/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_product` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `settings` | mediumblob NOT NULL | non | — |  |  |
| `num_subscriber_list` | int(10) unsigned DEFAULT NULL | oui | NULL |  |  |
| `num_status` | int(10) unsigned NOT NULL | non | — |  |  |

## `dsi_product_status`

Domaine probable : diffusion selective de l'information (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 2 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 230/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_product_status` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `active` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `dsi_send_queue`

Domaine probable : diffusion selective de l'information (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 231/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_send_queue` | int(11) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `channel_type` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `settings` | mediumblob NOT NULL | non | — |  |  |
| `num_subscriber_diffusion` | int(11) unsigned NOT NULL | non | — |  |  |
| `num_diffusion_history` | int(11) unsigned NOT NULL | non | — |  |  |
| `flag` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_subscriber_empr` | int(11) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `dsi_subscriber_list`

Domaine probable : diffusion selective de l'information (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 232/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_subscriber_list` | int(11) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `model` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `settings` | mediumblob NOT NULL | non | — |  |  |
| `num_parent` | int(10) unsigned DEFAULT NULL | oui | NULL |  |  |
| `num_model` | int(10) unsigned DEFAULT NULL | oui | NULL |  |  |

## `dsi_subscriber_list_content`

Domaine probable : diffusion selective de l'information (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 233/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_subscriber` | int(10) unsigned NOT NULL | non | — | PK |  |
| `num_subscriber_list` | int(10) unsigned NOT NULL | non | — | PK |  |

## `dsi_subscribers`

Domaine probable : diffusion selective de l'information (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 234/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_subscriber` | int(11) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `name` | varchar(255) NOT NULL | non | — |  |  |
| `settings` | mediumblob NOT NULL | non | — |  |  |
| `type` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `update_type` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `dsi_subscribers_diffusion`

Domaine probable : diffusion selective de l'information (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 235/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_subscriber_diffusion` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `settings` | mediumblob NOT NULL | non | — |  |  |
| `type` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `update_type` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_diffusion` | int(10) unsigned NOT NULL | non | — |  |  |

## `dsi_subscribers_product`

Domaine probable : diffusion selective de l'information (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 236/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_subscriber_product` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `settings` | mediumblob NOT NULL | non | — |  |  |
| `type` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `update_type` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_product` | int(10) unsigned NOT NULL | non | — |  |  |

## `dsi_tag`

Domaine probable : diffusion selective de l'information (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 237/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_tag` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |

## `dsi_view`

Domaine probable : diffusion selective de l'information (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 238/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_view` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `model` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `settings` | mediumblob NOT NULL | non | — |  |  |
| `type` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_model` | int(10) unsigned DEFAULT NULL | oui | NULL |  |  |
| `num_parent` | int(10) unsigned DEFAULT NULL | oui | NULL |  |  |

## `editions_states`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 2 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 239/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_editions_state` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `editions_state_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `editions_state_num_classement` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `editions_state_used_datasource` | varchar(50) NOT NULL DEFAULT '' | non | '' |  |  |
| `editions_state_comment` | text NOT NULL | non | — |  |  |
| `editions_state_fieldslist` | text NOT NULL | non | — |  |  |
| `editions_state_fieldsparams` | text NOT NULL | non | — |  |  |

## `empr`

Fiche lecteur (donnees perso RGPD). Futur modele Adherent.

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 9510 (borne sup, pas effectif), instructions INSERT : 2, preuve : CREATE TABLE observe (bloc 240/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_empr` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `empr_cb` | varchar(255) DEFAULT NULL | oui | NULL | UNIQUE | code-barres (unique observe) |
| `empr_nom` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | donnee perso RGPD |
| `empr_prenom` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | donnee perso RGPD |
| `empr_adr1` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | donnee perso RGPD |
| `empr_adr2` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | donnee perso RGPD |
| `empr_cp` | varchar(10) NOT NULL DEFAULT '' | non | '' |  | champ adherent |
| `empr_ville` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | donnee perso RGPD |
| `empr_pays` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | donnee perso RGPD |
| `empr_mail` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | donnee perso RGPD |
| `empr_tel1` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | donnee perso RGPD |
| `empr_tel2` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | donnee perso RGPD |
| `empr_prof` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | champ adherent |
| `empr_year` | int(4) unsigned NOT NULL DEFAULT 0 | non | 0 |  | champ adherent |
| `empr_categ` | smallint(5) unsigned NOT NULL DEFAULT 0 | non | 0 |  | champ adherent |
| `empr_codestat` | smallint(5) unsigned NOT NULL DEFAULT 0 | non | 0 |  | champ adherent |
| `empr_creation` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | champ adherent |
| `empr_modif` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | champ adherent |
| `empr_sexe` | tinyint(3) unsigned NOT NULL DEFAULT 0 | non | 0 |  | champ adherent |
| `empr_login` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | champ adherent |
| `empr_password` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | SECRET : ne pas reprendre (reinitialiser cote cible) |
| `empr_password_is_encrypted` | int(1) NOT NULL DEFAULT 0 | non | 0 |  | SECRET : ne pas reprendre (reinitialiser cote cible) |
| `empr_digest` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | SECRET : ne pas reprendre (reinitialiser cote cible) |
| `empr_date_adhesion` | date DEFAULT NULL | oui | NULL |  | champ adherent |
| `empr_date_expiration` | date DEFAULT NULL | oui | NULL |  | champ adherent |
| `empr_msg` | text DEFAULT NULL | oui | NULL |  | champ adherent |
| `empr_lang` | varchar(10) NOT NULL DEFAULT 'fr_FR' | non | 'fr_FR' |  | champ adherent |
| `empr_ldap` | tinyint(1) unsigned DEFAULT 0 | oui | 0 |  | champ adherent |
| `type_abt` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `last_loan_date` | date DEFAULT NULL | oui | NULL |  | date |
| `empr_location` | int(6) unsigned NOT NULL DEFAULT 1 | non | 1 |  | champ adherent |
| `date_fin_blocage` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `total_loans` | bigint(20) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `empr_statut` | bigint(20) unsigned NOT NULL DEFAULT 1 | non | 1 |  | champ adherent |
| `cle_validation` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `empr_sms` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  | champ adherent |
| `empr_subscription_action` | text DEFAULT NULL | oui | NULL |  | champ adherent |
| `empr_pnb_password` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | SECRET : ne pas reprendre (reinitialiser cote cible) |
| `empr_pnb_password_hint` | varchar(100) NOT NULL DEFAULT '' | non | '' |  | SECRET : ne pas reprendre (reinitialiser cote cible) |
| `mfa_secret_code` | varchar(255) DEFAULT NULL | oui | NULL |  | SECRET : ne pas reprendre (reinitialiser cote cible) |
| `mfa_favorite` | varchar(255) DEFAULT NULL | oui | NULL |  |  |

## `empr_caddie`

Paniers d'adherents.

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 28 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 241/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `idemprcaddie` | int(8) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | lien suppose -> empr.id_empr |
| `name` | varchar(100) DEFAULT NULL | oui | NULL |  |  |
| `comment` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `autorisations` | mediumtext DEFAULT NULL | oui | NULL |  |  |
| `autorisations_all` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `empr_caddie_classement` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | champ adherent |
| `acces_rapide` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `favorite_color` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `creation_user_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `creation_date` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |

## `empr_caddie_content`

Domaine probable : adherents / lecteurs (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 242/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `empr_caddie_id` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 | PK | identifiant |
| `object_id` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK | identifiant |
| `flag` | varchar(10) DEFAULT NULL | oui | NULL |  |  |

## `empr_caddie_procs`

Domaine probable : adherents / lecteurs (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 28 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 243/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `idproc` | smallint(5) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI |  |
| `type` | varchar(20) NOT NULL DEFAULT 'SELECT' | non | 'SELECT' |  |  |
| `name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `requete` | blob NOT NULL | non | — |  |  |
| `comment` | tinytext NOT NULL | non | — |  |  |
| `autorisations` | mediumtext DEFAULT NULL | oui | NULL |  |  |
| `autorisations_all` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `parameters` | text DEFAULT NULL | oui | NULL |  |  |

## `empr_categ`

Referentiel : categories d'adherents (voir libelles ci-dessous).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 14 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 244/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_categ_empr` | smallint(5) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `libelle` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `duree_adhesion` | int(10) unsigned DEFAULT 365 | oui | 365 |  |  |
| `tarif_abt` | decimal(16,2) NOT NULL DEFAULT 0.00 | non | 0.00 |  |  |
| `age_min` | int(3) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `age_max` | int(3) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `pret_already_loaned_active` | tinyint(3) unsigned NOT NULL DEFAULT 1 | non | 1 |  | champ circulation |

## `empr_codestat`

Referentiel : code statistique adherent.

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 11 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 245/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `idcode` | smallint(5) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI |  |
| `libelle` | varchar(255) NOT NULL DEFAULT 'DEFAULT' | non | 'DEFAULT' |  | libelle |

## `empr_custom`

Domaine probable : adherents / lecteurs (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 20 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 246/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `idchamp` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI |  |
| `name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `titre` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `type` | varchar(10) NOT NULL DEFAULT 'text' | non | 'text' |  |  |
| `datatype` | varchar(10) NOT NULL DEFAULT '' | non | '' |  |  |
| `options` | text DEFAULT NULL | oui | NULL |  |  |
| `multiple` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `obligatoire` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `ordre` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `search` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `export` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `filters` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `exclusion_obligatoire` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `pond` | int(11) NOT NULL DEFAULT 100 | non | 100 |  |  |
| `opac_sort` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `comment` | blob NOT NULL | non | — |  |  |
| `custom_classement` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |

## `empr_custom_dates`

Domaine probable : adherents / lecteurs (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 247/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `empr_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK | champ adherent |
| `empr_custom_origine` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK | champ adherent |
| `empr_custom_date_type` | int(11) DEFAULT NULL | oui | NULL |  | champ adherent |
| `empr_custom_date_start` | int(11) NOT NULL DEFAULT 0 | non | 0 |  | champ adherent |
| `empr_custom_date_end` | int(11) NOT NULL DEFAULT 0 | non | 0 |  | champ adherent |
| `empr_custom_order` | int(11) unsigned NOT NULL DEFAULT 0 | non | 0 | PK | champ adherent |

## `empr_custom_lists`

Domaine probable : adherents / lecteurs (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 5 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 248/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_empr_custom_list` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `empr_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  | champ adherent |
| `empr_custom_list_value` | varchar(255) DEFAULT NULL | oui | NULL |  | champ adherent |
| `empr_custom_list_lib` | varchar(255) DEFAULT NULL | oui | NULL |  | champ adherent |
| `ordre` | int(11) DEFAULT NULL | oui | NULL |  |  |

## `empr_custom_values`

Domaine probable : adherents / lecteurs (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 249/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `empr_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  | champ adherent |
| `empr_custom_origine` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  | champ adherent |
| `empr_custom_small_text` | varchar(255) DEFAULT NULL | oui | NULL |  | champ adherent |
| `empr_custom_text` | text DEFAULT NULL | oui | NULL |  | champ adherent |
| `empr_custom_integer` | int(11) DEFAULT NULL | oui | NULL |  | champ adherent |
| `empr_custom_date` | date DEFAULT NULL | oui | NULL |  | date |
| `empr_custom_float` | float DEFAULT NULL | oui | NULL |  | champ adherent |
| `empr_custom_order` | int(11) NOT NULL DEFAULT 0 | non | 0 |  | champ adherent |

## `empr_devices`

Domaine probable : adherents / lecteurs (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 250/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `empr_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK | champ adherent |
| `device_id` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK | identifiant |

## `empr_grilles`

Domaine probable : adherents / lecteurs (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 251/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `empr_grille_categ` | int(5) NOT NULL DEFAULT 0 | non | 0 | PK | champ adherent |
| `empr_grille_location` | int(5) NOT NULL DEFAULT 0 | non | 0 | PK | champ adherent |
| `empr_grille_format` | longtext DEFAULT NULL | oui | NULL |  | champ adherent |

## `empr_groupe`

Liaison adherent <-> groupe (familles, collectivites).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 252/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `empr_id` | int(6) unsigned NOT NULL DEFAULT 0 | non | 0 | PK | identifiant |
| `groupe_id` | int(6) unsigned NOT NULL DEFAULT 0 | non | 0 | PK | identifiant |

## `empr_renewal_form_fields`

Domaine probable : adherents / lecteurs (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 253/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `empr_renewal_form_field_code` | varchar(255) NOT NULL | non | — | PK | champ adherent |
| `empr_renewal_form_field_display` | tinyint(1) unsigned NOT NULL DEFAULT 1 | non | 1 |  | champ adherent |
| `empr_renewal_form_field_mandatory` | tinyint(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  | champ adherent |
| `empr_renewal_form_field_alterable` | tinyint(1) unsigned NOT NULL DEFAULT 1 | non | 1 |  | champ adherent |
| `empr_renewal_form_field_explanation` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | champ adherent |

## `empr_statut`

Referentiel : statut de fiche (Actif / Interdit).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 3 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 254/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `idstatut` | smallint(5) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI |  |
| `statut_libelle` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `allow_loan` | tinyint(4) NOT NULL DEFAULT 1 | non | 1 |  |  |
| `allow_loan_hist` | tinyint(4) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `allow_book` | tinyint(4) NOT NULL DEFAULT 1 | non | 1 |  |  |
| `allow_opac` | tinyint(4) NOT NULL DEFAULT 1 | non | 1 |  |  |
| `allow_dsi` | tinyint(4) NOT NULL DEFAULT 1 | non | 1 |  |  |
| `allow_dsi_priv` | tinyint(4) NOT NULL DEFAULT 1 | non | 1 |  |  |
| `allow_sugg` | tinyint(4) NOT NULL DEFAULT 1 | non | 1 |  |  |
| `allow_dema` | tinyint(4) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |
| `allow_prol` | tinyint(4) NOT NULL DEFAULT 1 | non | 1 |  |  |
| `allow_avis` | tinyint(4) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |
| `allow_tag` | tinyint(4) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |
| `allow_pwd` | tinyint(4) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |
| `allow_liste_lecture` | tinyint(4) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `allow_self_checkout` | tinyint(4) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `allow_self_checkin` | tinyint(4) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `allow_serialcirc` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `allow_scan_request` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `allow_contribution` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `allow_pnb` | tinyint(4) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `empr_temp`

Domaine probable : adherents / lecteurs (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 255/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `cb` | varchar(255) NOT NULL | non | — | UNIQUE |  |
| `sess` | varchar(12) NOT NULL | non | — |  |  |

## `empty_words_calculs`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 22 (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 256/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_calcul` | int(9) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `date_calcul` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `php_empty_words` | text NOT NULL | non | — |  |  |
| `nb_notices_calcul` | mediumint(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `archive_calcul` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `entites`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 257/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_entite` | int(5) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `type_entite` | int(3) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_bibli` | int(5) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `raison_sociale` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `commentaires` | text DEFAULT NULL | oui | NULL |  |  |
| `siret` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `naf` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `rcs` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `tva` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `num_cp_client` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `num_cp_compta` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `site_web` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `logo` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `autorisations` | mediumtext NOT NULL | non | — |  |  |
| `num_frais` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_paiement` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `index_entite` | text NOT NULL | non | — |  |  |

## `entities`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 258/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_entity` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `type_entity` | int(3) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `entity_isbd` | text NOT NULL | non | — |  |  |

## `entrepot_source_2`

Domaine probable : entrepot statistique (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 708, preuve : CREATE TABLE observe (bloc 259/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `connector_id` | varchar(20) NOT NULL DEFAULT '' | non | '' | PK | identifiant |
| `source_id` | int(11) unsigned NOT NULL DEFAULT 0 | non | 0 | PK | identifiant |
| `ref` | varchar(220) NOT NULL DEFAULT '' | non | '' | PK |  |
| `date_import` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `ufield` | char(3) NOT NULL DEFAULT '' | non | '' | PK |  |
| `field_ind` | char(2) NOT NULL DEFAULT '' | non | '' |  |  |
| `usubfield` | char(1) NOT NULL DEFAULT '' | non | '' | PK |  |
| `field_order` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `subfield_order` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `value` | text NOT NULL | non | — |  |  |
| `i_value` | text NOT NULL | non | — |  |  |
| `recid` | bigint(20) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `search_id` | varchar(32) NOT NULL DEFAULT '' | non | '' | PK | identifiant |

## `entrepot_source_5`

Domaine probable : entrepot statistique (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 260/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `connector_id` | varchar(20) NOT NULL DEFAULT '' | non | '' | PK | identifiant |
| `source_id` | int(11) unsigned NOT NULL DEFAULT 0 | non | 0 | PK | identifiant |
| `ref` | varchar(220) NOT NULL DEFAULT '' | non | '' | PK |  |
| `date_import` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `ufield` | char(3) NOT NULL DEFAULT '' | non | '' | PK |  |
| `field_ind` | char(2) NOT NULL DEFAULT '' | non | '' |  |  |
| `usubfield` | char(1) NOT NULL DEFAULT '' | non | '' | PK |  |
| `field_order` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `subfield_order` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `value` | text NOT NULL | non | — |  |  |
| `i_value` | text NOT NULL | non | — |  |  |
| `recid` | bigint(20) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `search_id` | varchar(32) NOT NULL DEFAULT '' | non | '' | PK | identifiant |

## `entrepot_source_6`

Domaine probable : entrepot statistique (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 21, preuve : CREATE TABLE observe (bloc 261/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `connector_id` | varchar(20) NOT NULL DEFAULT '' | non | '' | PK | identifiant |
| `source_id` | int(11) unsigned NOT NULL DEFAULT 0 | non | 0 | PK | identifiant |
| `ref` | varchar(220) NOT NULL DEFAULT '' | non | '' | PK |  |
| `date_import` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `ufield` | char(3) NOT NULL DEFAULT '' | non | '' | PK |  |
| `field_ind` | char(2) NOT NULL DEFAULT '' | non | '' |  |  |
| `usubfield` | char(1) NOT NULL DEFAULT '' | non | '' | PK |  |
| `field_order` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `subfield_order` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `value` | text NOT NULL | non | — |  |  |
| `i_value` | text NOT NULL | non | — |  |  |
| `recid` | bigint(20) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `search_id` | varchar(32) NOT NULL DEFAULT '' | non | '' | PK | identifiant |

## `entrepots_localisations`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 262/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `loc_id` | int(11) NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `loc_code` | varchar(255) NOT NULL DEFAULT '' | non | '' | UNIQUE |  |
| `loc_libelle` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `loc_visible` | tinyint(1) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |

## `equations`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 2 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 263/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_equation` | int(9) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `num_classement` | int(8) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |
| `nom_equation` | text NOT NULL | non | — |  |  |
| `comment_equation` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `requete` | blob NOT NULL | non | — |  |  |
| `proprio_equation` | int(9) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `error_log`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 264/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `error_date` | timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp() | non | current_timestamp() |  | date |
| `error_origin` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `error_text` | text DEFAULT NULL | oui | NULL |  |  |

## `es_cache`

Domaine probable : recherche externe / connecteurs (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 265/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `escache_groupname` | varchar(100) NOT NULL DEFAULT '' | non | '' | PK |  |
| `escache_unique_id` | varchar(100) NOT NULL DEFAULT '' | non | '' | PK | identifiant |
| `escache_value` | int(11) NOT NULL DEFAULT 0 | non | 0 | PK |  |

## `es_cache_blob`

Domaine probable : recherche externe / connecteurs (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 2, preuve : CREATE TABLE observe (bloc 266/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `es_cache_objectref` | varchar(100) NOT NULL DEFAULT '' | non | '' | PK |  |
| `es_cache_objecttype` | int(11) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `es_cache_objectformat` | varchar(100) NOT NULL DEFAULT '' | non | '' | PK |  |
| `es_cache_owner` | varchar(100) NOT NULL DEFAULT '' | non | '' | PK |  |
| `es_cache_creationdate` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE |  |
| `es_cache_expirationdate` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE |  |
| `es_cache_content` | mediumblob NOT NULL | non | — |  |  |

## `es_cache_int`

Domaine probable : recherche externe / connecteurs (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 267/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `es_cache_objectref` | varchar(100) NOT NULL DEFAULT '' | non | '' | PK |  |
| `es_cache_objecttype` | int(11) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `es_cache_objectformat` | varchar(100) NOT NULL DEFAULT '' | non | '' | PK |  |
| `es_cache_owner` | varchar(100) NOT NULL DEFAULT '' | non | '' | PK |  |
| `es_cache_creationdate` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE |  |
| `es_cache_expirationdate` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE |  |
| `es_cache_content` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `es_converted_cache`

Domaine probable : recherche externe / connecteurs (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 268/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `es_converted_cache_objecttype` | int(11) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `es_converted_cache_objectref` | int(11) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `es_converted_cache_format` | varchar(50) NOT NULL DEFAULT '' | non | '' | PK |  |
| `es_converted_cache_value` | text NOT NULL | non | — |  |  |
| `es_converted_cache_bestbefore` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE |  |

## `es_esgroup_esusers`

Domaine probable : recherche externe / connecteurs (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 269/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `esgroupuser_groupnum` | int(11) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `esgroupuser_usertype` | int(4) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `esgroupuser_usernum` | int(11) NOT NULL DEFAULT 0 | non | 0 | PK |  |

## `es_esgroups`

Domaine probable : recherche externe / connecteurs (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 2 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 270/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `esgroup_id` | int(11) NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `esgroup_name` | varchar(100) NOT NULL DEFAULT '' | non | '' | UNIQUE | libelle |
| `esgroup_fullname` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `esgroup_pmbusernum` | int(5) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `es_esusers`

Domaine probable : recherche externe / connecteurs (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 3 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 271/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `esuser_id` | int(11) NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `esuser_username` | varchar(100) NOT NULL DEFAULT '' | non | '' | UNIQUE |  |
| `esuser_password` | varchar(100) NOT NULL DEFAULT '' | non | '' |  | SECRET : ne pas reprendre (reinitialiser cote cible) |
| `esuser_fullname` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `esuser_groupnum` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `es_methods`

Domaine probable : recherche externe / connecteurs (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 4775 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 272/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_method` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `groupe` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `method` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `available` | smallint(5) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |

## `es_methods_users`

Domaine probable : recherche externe / connecteurs (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 273/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_method` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `num_user` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `anonymous` | smallint(6) DEFAULT 0 | oui | 0 |  |  |

## `es_searchcache`

Domaine probable : recherche externe / connecteurs (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 274/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `es_searchcache_searchid` | varchar(100) NOT NULL DEFAULT '' | non | '' | PK |  |
| `es_searchcache_date` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `es_searchcache_serializedsearch` | text NOT NULL | non | — |  |  |

## `es_searchsessions`

Domaine probable : recherche externe / connecteurs (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 275/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `es_searchsession_id` | varchar(100) NOT NULL DEFAULT '' | non | '' | PK | identifiant |
| `es_searchsession_searchnum` | varchar(100) NOT NULL DEFAULT '' | non | '' |  |  |
| `es_searchsession_searchrealm` | varchar(100) NOT NULL DEFAULT '' | non | '' |  |  |
| `es_searchsession_pmbuserid` | int(11) NOT NULL DEFAULT -1 | non | -1 |  |  |
| `es_searchsession_opacemprid` | int(11) NOT NULL DEFAULT -1 | non | -1 |  | lien suppose -> empr.id_empr |
| `es_searchsession_lastseendate` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE |  |

## `etagere`

Etageres virtuelles OPAC.

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 22 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 276/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `idetagere` | int(8) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI |  |
| `name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `comment` | blob NOT NULL | non | — |  |  |
| `validite` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `validite_date_deb` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE |  |
| `validite_date_fin` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE |  |
| `visible_accueil` | int(1) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |
| `autorisations` | mediumtext DEFAULT NULL | oui | NULL |  |  |
| `id_tri` | int(11) NOT NULL | non | — |  | identifiant |
| `thumbnail_url` | mediumblob NOT NULL | non | — |  |  |
| `etagere_classement` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `comment_gestion` | text NOT NULL | non | — |  |  |

## `etagere_caddie`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 277/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `etagere_id` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 | PK | identifiant |
| `caddie_id` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 | PK | identifiant |
| `etagere_caddie_filters` | mediumtext DEFAULT NULL | oui | NULL |  |  |

## `exemplaires`

Exemplaire physique rattache a une notice (ou un bulletin). Porte cote, section, statut, localisation, CB.

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 152278 (borne sup, pas effectif), instructions INSERT : 15, preuve : CREATE TABLE observe (bloc 278/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `expl_id` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `expl_cb` | varchar(255) DEFAULT NULL | oui | NULL | UNIQUE | code-barres (unique observe) |
| `expl_notice` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  | lien suppose -> notices.notice_id |
| `expl_bulletin` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  | lien suppose -> bulletins.bulletin_id |
| `expl_typdoc` | int(5) unsigned NOT NULL DEFAULT 0 | non | 0 |  | champ exemplaire |
| `expl_cote` | varchar(255) DEFAULT NULL | oui | NULL |  | cote |
| `expl_section` | smallint(5) unsigned NOT NULL DEFAULT 0 | non | 0 |  | champ exemplaire |
| `expl_statut` | smallint(5) unsigned NOT NULL DEFAULT 0 | non | 0 |  | champ exemplaire |
| `expl_location` | smallint(5) unsigned NOT NULL DEFAULT 0 | non | 0 |  | champ exemplaire |
| `expl_codestat` | smallint(5) unsigned NOT NULL DEFAULT 0 | non | 0 |  | champ exemplaire |
| `expl_date_depot` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | champ exemplaire |
| `expl_date_retour` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | champ exemplaire |
| `expl_note` | tinytext NOT NULL | non | — |  | champ exemplaire |
| `expl_prix` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | champ exemplaire |
| `expl_owner` | mediumint(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  | champ exemplaire |
| `expl_lastempr` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  | lien suppose -> empr.id_empr |
| `last_loan_date` | date DEFAULT NULL | oui | NULL |  | date |
| `create_date` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `update_date` | timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp() | non | current_timestamp() |  | date |
| `type_antivol` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `transfert_location_origine` | smallint(5) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `transfert_statut_origine` | smallint(5) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `expl_comment` | text DEFAULT NULL | oui | NULL |  | champ exemplaire |
| `expl_nbparts` | int(8) unsigned NOT NULL DEFAULT 1 | non | 1 |  | champ exemplaire |
| `expl_retloc` | smallint(5) unsigned NOT NULL DEFAULT 0 | non | 0 |  | champ exemplaire |
| `expl_abt_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  | champ exemplaire |
| `transfert_section_origine` | smallint(5) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `expl_ref_num` | int(10) NOT NULL DEFAULT 0 | non | 0 |  | champ exemplaire |
| `expl_pnb_flag` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  | champ exemplaire |

## `exemplaires_temp`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 279/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `cb` | varchar(50) NOT NULL DEFAULT '' | non | '' | UNIQUE |  |
| `sess` | varchar(12) NOT NULL DEFAULT '' | non | '' |  |  |

## `exercices`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 280/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_exercice` | int(8) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `num_entite` | int(5) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `libelle` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `date_debut` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `date_fin` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `statut` | int(3) unsigned NOT NULL DEFAULT 1 | non | 1 |  | metadonnee catalogue |

## `expl_custom`

Domaine probable : exemplaires / numerique (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 8 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 281/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `idchamp` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI |  |
| `name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `titre` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `type` | varchar(10) NOT NULL DEFAULT 'text' | non | 'text' |  |  |
| `datatype` | varchar(10) NOT NULL DEFAULT '' | non | '' |  |  |
| `options` | text DEFAULT NULL | oui | NULL |  |  |
| `multiple` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `obligatoire` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `ordre` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `search` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `export` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `filters` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `exclusion_obligatoire` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `pond` | int(11) NOT NULL DEFAULT 100 | non | 100 |  |  |
| `opac_sort` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `comment` | blob NOT NULL | non | — |  |  |
| `custom_classement` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |

## `expl_custom_dates`

Domaine probable : exemplaires / numerique (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 282/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `expl_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK | champ exemplaire |
| `expl_custom_origine` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK | champ exemplaire |
| `expl_custom_date_type` | int(11) DEFAULT NULL | oui | NULL |  | champ exemplaire |
| `expl_custom_date_start` | int(11) NOT NULL DEFAULT 0 | non | 0 |  | champ exemplaire |
| `expl_custom_date_end` | int(11) NOT NULL DEFAULT 0 | non | 0 |  | champ exemplaire |
| `expl_custom_order` | int(11) unsigned NOT NULL DEFAULT 0 | non | 0 | PK | champ exemplaire |

## `expl_custom_lists`

Domaine probable : exemplaires / numerique (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 7 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 283/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_expl_custom_list` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `expl_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  | champ exemplaire |
| `expl_custom_list_value` | varchar(255) DEFAULT NULL | oui | NULL |  | champ exemplaire |
| `expl_custom_list_lib` | varchar(255) DEFAULT NULL | oui | NULL |  | champ exemplaire |
| `ordre` | int(11) DEFAULT NULL | oui | NULL |  |  |

## `expl_custom_values`

Domaine probable : exemplaires / numerique (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 8, preuve : CREATE TABLE observe (bloc 284/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `expl_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  | champ exemplaire |
| `expl_custom_origine` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  | champ exemplaire |
| `expl_custom_small_text` | varchar(255) DEFAULT NULL | oui | NULL |  | champ exemplaire |
| `expl_custom_text` | text DEFAULT NULL | oui | NULL |  | champ exemplaire |
| `expl_custom_integer` | int(11) DEFAULT NULL | oui | NULL |  | champ exemplaire |
| `expl_custom_date` | date DEFAULT NULL | oui | NULL |  | date |
| `expl_custom_float` | float DEFAULT NULL | oui | NULL |  | champ exemplaire |
| `expl_custom_order` | int(11) NOT NULL DEFAULT 0 | non | 0 |  | champ exemplaire |

## `explnum`

Documents numeriques lies aux notices.

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 8117 (borne sup, pas effectif), instructions INSERT : 2, preuve : CREATE TABLE observe (bloc 285/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `explnum_id` | int(11) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `explnum_notice` | mediumint(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `explnum_bulletin` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  | lien suppose -> bulletins.bulletin_id |
| `explnum_nom` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `explnum_mimetype` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `explnum_url` | text NOT NULL | non | — |  |  |
| `explnum_data` | mediumblob DEFAULT NULL | oui | NULL |  |  |
| `explnum_vignette` | mediumblob DEFAULT NULL | oui | NULL |  |  |
| `explnum_extfichier` | varchar(20) DEFAULT '' | oui | '' |  |  |
| `explnum_nomfichier` | text DEFAULT NULL | oui | NULL |  |  |
| `explnum_statut` | int(5) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `explnum_index_sew` | mediumtext NOT NULL | non | — |  |  |
| `explnum_index_wew` | mediumtext NOT NULL | non | — |  |  |
| `explnum_repertoire` | int(8) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `explnum_path` | text NOT NULL | non | — |  |  |
| `explnum_docnum_statut` | smallint(5) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |
| `explnum_signature` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `explnum_create_date` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `explnum_update_date` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `explnum_file_size` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `explnum_custom`

Domaine probable : exemplaires / numerique (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 286/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `idchamp` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI |  |
| `num_type` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `titre` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `type` | varchar(10) NOT NULL DEFAULT 'text' | non | 'text' |  |  |
| `datatype` | varchar(10) NOT NULL DEFAULT '' | non | '' |  |  |
| `options` | text DEFAULT NULL | oui | NULL |  |  |
| `multiple` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `obligatoire` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `ordre` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `search` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `export` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `filters` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `exclusion_obligatoire` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `pond` | int(11) NOT NULL DEFAULT 100 | non | 100 |  |  |
| `opac_sort` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `comment` | blob NOT NULL | non | — |  |  |
| `custom_classement` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |

## `explnum_custom_dates`

Domaine probable : exemplaires / numerique (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 287/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `explnum_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `explnum_custom_origine` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `explnum_custom_date_type` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `explnum_custom_date_start` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `explnum_custom_date_end` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `explnum_custom_order` | int(11) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |

## `explnum_custom_lists`

Domaine probable : exemplaires / numerique (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 288/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_explnum_custom_list` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `explnum_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `explnum_custom_list_value` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `explnum_custom_list_lib` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `ordre` | int(11) DEFAULT NULL | oui | NULL |  |  |

## `explnum_custom_values`

Domaine probable : exemplaires / numerique (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 289/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `explnum_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `explnum_custom_origine` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `explnum_custom_small_text` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `explnum_custom_text` | text DEFAULT NULL | oui | NULL |  |  |
| `explnum_custom_integer` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `explnum_custom_date` | date DEFAULT NULL | oui | NULL |  | date |
| `explnum_custom_float` | float DEFAULT NULL | oui | NULL |  |  |
| `explnum_custom_order` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `explnum_doc`

Domaine probable : exemplaires / numerique (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 290/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_explnum_doc` | int(8) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `explnum_doc_nomfichier` | text NOT NULL | non | — |  |  |
| `explnum_doc_mimetype` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `explnum_doc_data` | mediumblob NOT NULL | non | — |  |  |
| `explnum_doc_extfichier` | varchar(20) NOT NULL DEFAULT '' | non | '' |  |  |
| `explnum_doc_url` | text NOT NULL | non | — |  |  |

## `explnum_doc_actions`

Domaine probable : exemplaires / numerique (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 291/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_explnum_doc` | int(10) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `num_action` | int(10) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `prive` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `rapport` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_explnum` | int(10) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `explnum_doc_sugg`

Domaine probable : exemplaires / numerique (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 292/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_explnum_doc` | int(10) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `num_suggestion` | int(10) NOT NULL DEFAULT 0 | non | 0 | PK |  |

## `explnum_lenders`

Domaine probable : exemplaires / numerique (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 293/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `explnum_lender_num_explnum` | int(11) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `explnum_lender_num_lender` | int(11) NOT NULL DEFAULT 0 | non | 0 | PK |  |

## `explnum_licence`

Domaine probable : exemplaires / numerique (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 294/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_explnum_licence` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `explnum_licence_label` | varchar(255) DEFAULT '' | oui | '' |  |  |
| `explnum_licence_uri` | varchar(255) DEFAULT '' | oui | '' |  |  |

## `explnum_licence_profile_explnums`

Domaine probable : exemplaires / numerique (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 295/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `explnum_licence_profile_explnums_explnum_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `explnum_licence_profile_explnums_profile_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |

## `explnum_licence_profile_rights`

Domaine probable : exemplaires / numerique (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 296/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `explnum_licence_profile_num` | int(11) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `explnum_licence_right_num` | int(11) NOT NULL DEFAULT 0 | non | 0 | PK |  |

## `explnum_licence_profiles`

Domaine probable : exemplaires / numerique (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 297/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_explnum_licence_profile` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `explnum_licence_profile_explnum_licence_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `explnum_licence_profile_label` | varchar(255) DEFAULT '' | oui | '' |  |  |
| `explnum_licence_profile_uri` | varchar(255) DEFAULT '' | oui | '' |  |  |
| `explnum_licence_profile_logo_url` | varchar(255) DEFAULT '' | oui | '' |  |  |
| `explnum_licence_profile_explanation` | text DEFAULT NULL | oui | NULL |  |  |
| `explnum_licence_profile_quotation_rights` | text DEFAULT NULL | oui | NULL |  |  |

## `explnum_licence_rights`

Domaine probable : exemplaires / numerique (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 298/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_explnum_licence_right` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `explnum_licence_right_explnum_licence_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `explnum_licence_right_label` | varchar(255) DEFAULT '' | oui | '' |  |  |
| `explnum_licence_right_type` | int(2) DEFAULT 0 | oui | 0 |  |  |
| `explnum_licence_right_logo_url` | varchar(255) DEFAULT '' | oui | '' |  |  |
| `explnum_licence_right_explanation` | text DEFAULT NULL | oui | NULL |  |  |

## `explnum_location`

Domaine probable : exemplaires / numerique (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 299/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_explnum` | int(10) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `num_location` | int(10) NOT NULL DEFAULT 0 | non | 0 | PK |  |

## `explnum_segments`

Domaine probable : exemplaires / numerique (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 300/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `explnum_segment_id` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `explnum_segment_explnum_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `explnum_segment_speaker_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `explnum_segment_start` | double NOT NULL DEFAULT 0 | non | 0 |  |  |
| `explnum_segment_duration` | double NOT NULL DEFAULT 0 | non | 0 |  |  |
| `explnum_segment_end` | double NOT NULL DEFAULT 0 | non | 0 |  |  |

## `explnum_speakers`

Domaine probable : exemplaires / numerique (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 301/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `explnum_speaker_id` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `explnum_speaker_explnum_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `explnum_speaker_speaker_num` | varchar(10) NOT NULL DEFAULT '' | non | '' |  |  |
| `explnum_speaker_gender` | varchar(1) DEFAULT '' | oui | '' |  |  |
| `explnum_speaker_author` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `explnum_statut`

Domaine probable : exemplaires / numerique (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 2 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 302/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_explnum_statut` | smallint(5) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `gestion_libelle` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `opac_libelle` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `class_html` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `explnum_visible_opac` | tinyint(1) NOT NULL DEFAULT 1 | non | 1 |  |  |
| `explnum_visible_opac_abon` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `explnum_consult_opac` | tinyint(1) NOT NULL DEFAULT 1 | non | 1 |  |  |
| `explnum_consult_opac_abon` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `explnum_download_opac` | tinyint(1) NOT NULL DEFAULT 1 | non | 1 |  |  |
| `explnum_download_opac_abon` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `explnum_thumbnail_visible_opac_override` | tinyint(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `external_count`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 84838 (borne sup, pas effectif), instructions INSERT : 5, preuve : CREATE TABLE observe (bloc 303/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `rid` | bigint(20) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI |  |
| `recid` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `source_id` | int(11) NOT NULL | non | — |  | identifiant |

## `facettes`

Domaine probable : recherche a facettes (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 5 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 304/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_facette` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `facette_type` | varchar(255) NOT NULL DEFAULT 'notices' | non | 'notices' |  |  |
| `facette_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `facette_critere` | int(5) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `facette_ss_critere` | int(5) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `facette_nb_result` | int(2) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `facette_visible_gestion` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `facette_visible` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `facette_type_sort` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `facette_order_sort` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `facette_datatype_sort` | varchar(255) NOT NULL DEFAULT 'alpha' | non | 'alpha' |  |  |
| `facette_order` | int(11) NOT NULL DEFAULT 1 | non | 1 |  |  |
| `facette_limit_plus` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `facette_opac_views_num` | text NOT NULL | non | — |  |  |
| `num_facettes_set` | int(10) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `facettes_external`

Domaine probable : recherche a facettes (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 305/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_facette` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `facette_type` | varchar(255) NOT NULL DEFAULT 'notices' | non | 'notices' |  |  |
| `facette_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `facette_critere` | int(5) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `facette_ss_critere` | int(5) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `facette_nb_result` | int(2) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `facette_visible_gestion` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `facette_visible` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `facette_type_sort` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `facette_order_sort` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `facette_datatype_sort` | varchar(255) NOT NULL DEFAULT 'alpha' | non | 'alpha' |  |  |
| `facette_order` | int(11) NOT NULL DEFAULT 1 | non | 1 |  |  |
| `facette_limit_plus` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `facette_opac_views_num` | text NOT NULL | non | — |  |  |
| `num_facettes_set` | int(10) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `facettes_sets`

Domaine probable : recherche a facettes (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 306/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_set` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `type` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `num_user` | int(5) unsigned NOT NULL | non | — |  |  |
| `users_groups` | mediumblob NOT NULL | non | — |  |  |

## `facettes_sets_users`

Domaine probable : recherche a facettes (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 307/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_set` | int(10) unsigned NOT NULL | non | — | PK |  |
| `num_user` | int(5) unsigned NOT NULL | non | — | PK |  |
| `visible` | int(1) unsigned NOT NULL | non | — |  |  |
| `ranking` | int(10) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `faq_questions`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 308/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_faq_question` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `faq_question_num_type` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `faq_question_num_theme` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `faq_question_num_demande` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `faq_question_question` | text NOT NULL | non | — |  |  |
| `faq_question_question_userdate` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `faq_question_question_date` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `faq_question_answer` | text NOT NULL | non | — |  |  |
| `faq_question_answer_userdate` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `faq_question_answer_date` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `faq_question_statut` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `faq_questions_categories`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 309/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_faq_question` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_categ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `categ_order` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `faq_questions_fields_global_index`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 310/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_faq_question` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK | identifiant |
| `code_champ` | int(3) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `code_ss_champ` | int(3) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `ordre` | int(4) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `value` | text NOT NULL | non | — |  |  |
| `pond` | int(4) unsigned NOT NULL DEFAULT 100 | non | 100 |  |  |
| `lang` | varchar(10) NOT NULL DEFAULT '' | non | '' | PK |  |
| `authority_num` | varchar(50) NOT NULL DEFAULT '0' | non | '0' |  |  |

## `faq_questions_words_global_index`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 311/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_faq_question` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK | identifiant |
| `code_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `code_ss_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `num_word` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `pond` | int(10) unsigned NOT NULL DEFAULT 100 | non | 100 |  |  |
| `position` | int(10) unsigned NOT NULL DEFAULT 1 | non | 1 | PK |  |
| `field_position` | int(10) unsigned NOT NULL DEFAULT 1 | non | 1 | PK |  |

## `faq_themes`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 312/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_theme` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `libelle_theme` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |

## `faq_types`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 313/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_type` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `libelle_type` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |

## `fiche`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 314/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_fiche` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `infos_global` | text NOT NULL | non | — |  |  |
| `index_infos_global` | text NOT NULL | non | — |  |  |

## `frais`

Frais annexes (inscription, reproduction...).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 315/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_frais` | int(8) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `libelle` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `condition_frais` | text NOT NULL | non | — |  |  |
| `montant` | double(12,2) NOT NULL DEFAULT 0.00 | non | 0.00 |  | montant |
| `num_cp_compta` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `num_tva_achat` | varchar(25) NOT NULL DEFAULT '0' | non | '0' |  |  |
| `index_libelle` | text DEFAULT NULL | oui | NULL |  | libelle |
| `add_to_new_order` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `frbr_cadres`

Domaine probable : modele FRBR (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 316/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_cadre` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `cadre_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `cadre_comment` | text NOT NULL | non | — |  |  |
| `cadre_object` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `cadre_css_class` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `cadre_num_datanode` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `cadre_num_page` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `cadre_visible_in_graph` | tinyint(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `cadre_datanodes_path` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `cadre_display_empty_template` | tinyint(1) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |

## `frbr_cadres_content`

Domaine probable : modele FRBR (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 317/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_cadre_content` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `cadre_content_type` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `cadre_content_object` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `cadre_content_num_cadre` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `cadre_content_data` | text NOT NULL | non | — |  |  |

## `frbr_cataloging_categories`

Domaine probable : modele FRBR (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 318/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_cataloging_category` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `cataloging_category_title` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `cataloging_category_num_parent` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `frbr_cataloging_datanodes`

Domaine probable : modele FRBR (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 319/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_cataloging_datanode` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `cataloging_datanode_title` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `cataloging_datanode_comment` | text NOT NULL | non | — |  |  |
| `cataloging_datanode_owner` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `cataloging_datanode_allowed_users` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `cataloging_datanode_num_category` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `frbr_cataloging_items`

Domaine probable : modele FRBR (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 320/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_cataloging_item` | int(10) unsigned NOT NULL | non | — | PK |  |
| `type_cataloging_item` | varchar(255) NOT NULL DEFAULT '' | non | '' | PK |  |
| `cataloging_item_num_user` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `cataloging_item_added_date` | datetime DEFAULT NULL | oui | NULL |  | date |
| `cataloging_item_num_datanode` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |

## `frbr_datanodes`

Domaine probable : modele FRBR (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 321/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_datanode` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `datanode_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `datanode_comment` | text NOT NULL | non | — |  |  |
| `datanode_object` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `datanode_num_page` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `datanode_num_parent` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `frbr_datanodes_content`

Domaine probable : modele FRBR (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 322/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_datanode_content` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `datanode_content_type` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `datanode_content_object` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `datanode_content_num_datanode` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `datanode_content_data` | text NOT NULL | non | — |  |  |

## `frbr_managed_entities`

Domaine probable : modele FRBR (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 323/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `managed_entity_name` | varchar(255) NOT NULL DEFAULT '' | non | '' | PK | libelle |
| `managed_entity_box` | text NOT NULL | non | — |  |  |

## `frbr_pages`

Domaine probable : modele FRBR (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 324/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_page` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `page_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `page_comment` | text NOT NULL | non | — |  |  |
| `page_entity` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `page_parameters` | text NOT NULL | non | — |  |  |
| `page_opac_views` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `page_order` | int(11) NOT NULL DEFAULT 1 | non | 1 |  |  |

## `frbr_pages_content`

Domaine probable : modele FRBR (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 325/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_page_content` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `page_content_type` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `page_content_object` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `page_content_num_page` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `page_content_data` | text NOT NULL | non | — |  |  |

## `frbr_place`

Domaine probable : modele FRBR (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 326/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `place_num_page` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `place_num_cadre` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `place_cadre_type` | varchar(255) NOT NULL DEFAULT '' | non | '' | PK |  |
| `place_visibility` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `place_order` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `gestfic0_custom`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 327/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `idchamp` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI |  |
| `name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `titre` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `type` | varchar(10) NOT NULL DEFAULT 'text' | non | 'text' |  |  |
| `datatype` | varchar(10) NOT NULL DEFAULT '' | non | '' |  |  |
| `options` | text DEFAULT NULL | oui | NULL |  |  |
| `multiple` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `obligatoire` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `ordre` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `search` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `export` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `filters` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `exclusion_obligatoire` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `pond` | int(11) NOT NULL DEFAULT 100 | non | 100 |  |  |
| `opac_sort` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `comment` | blob NOT NULL | non | — |  |  |
| `custom_classement` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |

## `gestfic0_custom_lists`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 328/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_gestfic0_custom_list` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `gestfic0_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `gestfic0_custom_list_value` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `gestfic0_custom_list_lib` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `ordre` | int(11) DEFAULT NULL | oui | NULL |  |  |

## `gestfic0_custom_values`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 329/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `gestfic0_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `gestfic0_custom_origine` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `gestfic0_custom_small_text` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `gestfic0_custom_text` | text DEFAULT NULL | oui | NULL |  |  |
| `gestfic0_custom_integer` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `gestfic0_custom_date` | date DEFAULT NULL | oui | NULL |  | date |
| `gestfic0_custom_float` | float DEFAULT NULL | oui | NULL |  |  |
| `gestfic0_custom_order` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `gestion_login_attempt`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 330/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_gestion_login_attempt` | int(11) NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `gestion_login_attempt_ip` | varchar(45) NOT NULL | non | — | UNIQUE |  |
| `gestion_login_attempt_login` | varchar(255) NOT NULL | non | — | UNIQUE |  |
| `gestion_login_attempt_time` | datetime NOT NULL DEFAULT current_timestamp() | non | current_timestamp() | UNIQUE |  |
| `gestion_login_attempt_success` | tinyint(4) NOT NULL | non | — |  |  |

## `grids_generic`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 331/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `grid_generic_type` | varchar(32) NOT NULL DEFAULT '' | non | '' | PK |  |
| `grid_generic_filter` | varchar(255) NOT NULL DEFAULT '' | non | '' | PK |  |
| `grid_generic_data` | mediumblob NOT NULL | non | — |  |  |

## `grilles`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 332/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `grille_typdoc` | char(2) NOT NULL DEFAULT 'a' | non | 'a' | PK |  |
| `grille_niveau_biblio` | char(1) NOT NULL DEFAULT 'm' | non | 'm' | PK |  |
| `grille_localisation` | mediumint(8) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `descr_format` | longtext DEFAULT NULL | oui | NULL |  |  |

## `groupe`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 75 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 333/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_groupe` | int(6) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `libelle_groupe` | varchar(255) NOT NULL | non | — | UNIQUE | libelle |
| `resp_groupe` | int(6) unsigned DEFAULT 0 | oui | 0 |  |  |
| `lettre_rappel` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `mail_rappel` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  | donnee perso RGPD |
| `lettre_rappel_show_nomgroup` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `comment_gestion` | text NOT NULL | non | — |  |  |
| `comment_opac` | text NOT NULL | non | — |  |  |
| `lettre_resa` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `mail_resa` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  | donnee perso RGPD |
| `lettre_resa_show_nomgroup` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `groupexpl`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 334/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_groupexpl` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `groupexpl_resp_expl_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `groupexpl_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `groupexpl_comment` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `groupexpl_location` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `groupexpl_statut_resp` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `groupexpl_statut_others` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `groupexpl_expl`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 335/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `groupexpl_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `groupexpl_expl_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `groupexpl_checked` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `harvest_field`

Domaine probable : moissonnage de reservoirs (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 336/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_harvest_field` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `num_harvest_profil` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `harvest_field_xml_id` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  | identifiant |
| `harvest_field_ufield` | varchar(100) DEFAULT NULL | oui | NULL |  |  |
| `harvest_field_first_flag` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `harvest_field_order` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `harvest_profil`

Domaine probable : moissonnage de reservoirs (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 337/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_harvest_profil` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `harvest_profil_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |

## `harvest_profil_import`

Domaine probable : moissonnage de reservoirs (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 338/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_harvest_profil_import` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `harvest_profil_import_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |

## `harvest_profil_import_field`

Domaine probable : moissonnage de reservoirs (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 339/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_harvest_profil_import` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `harvest_profil_import_field_xml_id` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK | identifiant |
| `harvest_profil_import_field_flag` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `harvest_profil_import_field_order` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `harvest_search_field`

Domaine probable : moissonnage de reservoirs (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 340/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_harvest_profil` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `num_source` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `num_field` | varchar(25) NOT NULL DEFAULT '' | non | '' |  |  |
| `num_ss_field` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `harvest_src`

Domaine probable : moissonnage de reservoirs (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 341/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_harvest_src` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `num_harvest_field` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_source` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `harvest_src_ufield` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `harvest_src_prec_flag` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `harvest_src_order` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `import_marc`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 452167 (borne sup, pas effectif), instructions INSERT : 2, preuve : CREATE TABLE observe (bloc 342/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_import` | bigint(5) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `notice` | longblob NOT NULL | non | — |  |  |
| `origine` | varchar(50) DEFAULT '' | oui | '' |  |  |
| `no_notice` | int(10) unsigned DEFAULT 0 | oui | 0 |  |  |
| `encoding` | varchar(50) NOT NULL DEFAULT '' | non | '' |  |  |

## `index_concept`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 343/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_object` | int(10) unsigned NOT NULL | non | — | PK |  |
| `type_object` | int(10) unsigned NOT NULL | non | — | PK |  |
| `num_concept` | int(10) unsigned NOT NULL | non | — | PK |  |
| `order_concept` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `comment` | text NOT NULL | non | — |  |  |
| `comment_visible_opac` | tinyint(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `indexation_stack`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 344/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `indexation_stack_entity_id` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 | PK | identifiant |
| `indexation_stack_entity_type` | int(3) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `indexation_stack_datatype` | varchar(255) NOT NULL DEFAULT '' | non | '' | PK |  |
| `indexation_stack_timestamp` | bigint(20) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `indexation_stack_parent_id` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  | identifiant |
| `indexation_stack_parent_type` | int(3) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `indexation_stack_informations` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |

## `indexint`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 20491 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 345/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `indexint_id` | mediumint(8) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `indexint_name` | varchar(255) NOT NULL DEFAULT '' | non | '' | UNIQUE | libelle |
| `indexint_comment` | text NOT NULL | non | — |  |  |
| `index_indexint` | text DEFAULT NULL | oui | NULL |  |  |
| `num_pclass` | int(11) NOT NULL DEFAULT 1 | non | 1 | UNIQUE |  |

## `indexint_custom`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 346/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `idchamp` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI |  |
| `num_type` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `titre` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `type` | varchar(10) NOT NULL DEFAULT 'text' | non | 'text' |  |  |
| `datatype` | varchar(10) NOT NULL DEFAULT '' | non | '' |  |  |
| `options` | text DEFAULT NULL | oui | NULL |  |  |
| `multiple` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `obligatoire` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `ordre` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `search` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `export` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `filters` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `exclusion_obligatoire` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `pond` | int(11) NOT NULL DEFAULT 100 | non | 100 |  |  |
| `opac_sort` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `comment` | blob NOT NULL | non | — |  |  |
| `custom_classement` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |

## `indexint_custom_dates`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 347/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `indexint_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `indexint_custom_origine` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `indexint_custom_date_type` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `indexint_custom_date_start` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `indexint_custom_date_end` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `indexint_custom_order` | int(11) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |

## `indexint_custom_lists`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 348/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_indexint_custom_list` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `indexint_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `indexint_custom_list_value` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `indexint_custom_list_lib` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `ordre` | int(11) DEFAULT NULL | oui | NULL |  |  |

## `indexint_custom_values`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 349/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `indexint_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `indexint_custom_origine` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `indexint_custom_small_text` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `indexint_custom_text` | text DEFAULT NULL | oui | NULL |  |  |
| `indexint_custom_integer` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `indexint_custom_date` | date DEFAULT NULL | oui | NULL |  | date |
| `indexint_custom_float` | float DEFAULT NULL | oui | NULL |  |  |
| `indexint_custom_order` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `infopages`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 16 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 350/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_infopage` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `content_infopage` | longblob NOT NULL | non | — |  |  |
| `title_infopage` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `valid_infopage` | tinyint(1) NOT NULL DEFAULT 1 | non | 1 |  |  |
| `restrict_infopage` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `infopage_classement` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |

## `ip_blacklist`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 351/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_ip_blacklist` | int(11) NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `ip_blacklist_time` | datetime NOT NULL DEFAULT current_timestamp() | non | current_timestamp() |  |  |
| `ip_blacklist_ip` | varchar(45) NOT NULL | non | — | UNIQUE |  |

## `ip_whitelist`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 352/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_ip_whitelist` | int(11) NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `ip_whitelist_time` | datetime NOT NULL DEFAULT current_timestamp() | non | current_timestamp() |  |  |
| `ip_whitelist_ip` | varchar(45) NOT NULL | non | — | UNIQUE |  |

## `lenders`

Preteurs du reseau (dont MDN).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 16 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 353/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `idlender` | smallint(5) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI |  |
| `lender_libelle` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |

## `liens_actes`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 354/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_acte` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `num_acte_lie` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |

## `lignes_actes`

Domaine probable : acquisitions : lignes d'actes (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 355/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_ligne` | int(15) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `type_ligne` | int(3) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_acte` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `lig_ref` | int(15) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_acquisition` | int(12) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_rubrique` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_produit` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_type` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `libelle` | text NOT NULL | non | — |  | libelle |
| `code` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | metadonnee catalogue |
| `prix` | double(12,2) NOT NULL DEFAULT 0.00 | non | 0.00 |  | montant |
| `tva` | float(8,2) unsigned NOT NULL DEFAULT 0.00 | non | 0.00 |  |  |
| `nb` | int(5) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |
| `date_ech` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `date_cre` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `statut` | int(3) unsigned NOT NULL DEFAULT 0 | non | 0 |  | metadonnee catalogue |
| `remise` | float(8,2) NOT NULL DEFAULT 0.00 | non | 0.00 |  |  |
| `index_ligne` | text NOT NULL | non | — |  |  |
| `ligne_ordre` | smallint(2) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `debit_tva` | smallint(2) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `commentaires_gestion` | text NOT NULL | non | — |  |  |
| `commentaires_opac` | text NOT NULL | non | — |  |  |

## `lignes_actes_applicants`

Domaine probable : acquisitions : lignes d'actes (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 356/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `ligne_acte_num` | int(11) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `empr_num` | int(11) NOT NULL DEFAULT 0 | non | 0 | PK | champ adherent |

## `lignes_actes_relances`

Domaine probable : acquisitions : lignes d'actes (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 357/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_ligne` | int(10) unsigned NOT NULL | non | — | PK |  |
| `date_relance` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | PK,DEFAUT MASQUE | date |
| `type_ligne` | int(3) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_acte` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `lig_ref` | int(15) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_acquisition` | int(12) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_rubrique` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_produit` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_type` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `libelle` | text NOT NULL | non | — |  | libelle |
| `code` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | metadonnee catalogue |
| `prix` | float(8,2) NOT NULL DEFAULT 0.00 | non | 0.00 |  | montant |
| `tva` | float(8,2) unsigned NOT NULL DEFAULT 0.00 | non | 0.00 |  |  |
| `nb` | int(5) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |
| `date_ech` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `date_cre` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `statut` | int(3) unsigned NOT NULL DEFAULT 1 | non | 1 |  | metadonnee catalogue |
| `remise` | float(8,2) NOT NULL DEFAULT 0.00 | non | 0.00 |  |  |
| `index_ligne` | text NOT NULL | non | — |  |  |
| `ligne_ordre` | smallint(2) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `debit_tva` | smallint(2) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `commentaires_gestion` | text NOT NULL | non | — |  |  |
| `commentaires_opac` | text NOT NULL | non | — |  |  |

## `lignes_actes_statuts`

Domaine probable : acquisitions : lignes d'actes (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 2 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 358/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_statut` | int(3) NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `libelle` | text NOT NULL | non | — |  | libelle |
| `relance` | int(3) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `linked_mots`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 359/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_mot` | mediumint(8) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `num_linked_mot` | mediumint(8) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `type_lien` | tinyint(1) NOT NULL DEFAULT 1 | non | 1 | PK |  |
| `ponderation` | float NOT NULL DEFAULT 1 | non | 1 |  |  |

## `lists`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 360/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_list` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `list_num_user` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `list_objects_type` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `list_label` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `list_selected_columns` | text DEFAULT NULL | oui | NULL |  |  |
| `list_filters` | text DEFAULT NULL | oui | NULL |  |  |
| `list_applied_group` | text DEFAULT NULL | oui | NULL |  |  |
| `list_applied_sort` | text DEFAULT NULL | oui | NULL |  |  |
| `list_pager` | text DEFAULT NULL | oui | NULL |  |  |
| `list_selected_filters` | text DEFAULT NULL | oui | NULL |  |  |
| `list_settings` | mediumtext DEFAULT NULL | oui | NULL |  |  |
| `list_autorisations` | mediumtext DEFAULT NULL | oui | NULL |  |  |
| `list_default_selected` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `list_num_ranking` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `list_order` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `locked_entities`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 361/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_entity` | int(10) unsigned NOT NULL | non | — | PK | identifiant |
| `type` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `date` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE |  |
| `parent_id` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  | identifiant |
| `parent_type` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `user_id` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  | identifiant |
| `empr_id` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  | identifiant |

## `log_expl_retard`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 5275 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 362/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_log` | int(11) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `date_log` | timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp() | non | current_timestamp() |  | date |
| `titre` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `expl_id` | int(11) NOT NULL DEFAULT 0 | non | 0 |  | identifiant |
| `expl_cb` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | code-barres (unique observe) |
| `date_pret` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `date_retour` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `amende` | decimal(16,2) NOT NULL DEFAULT 0.00 | non | 0.00 |  |  |
| `num_log_retard` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `log_retard`

Journal des passages de relance.

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 1422 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 363/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_log` | int(11) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `date_log` | timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp() | non | current_timestamp() |  | date |
| `niveau_reel` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `niveau_suppose` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `amende_totale` | decimal(16,2) NOT NULL DEFAULT 0.00 | non | 0.00 |  |  |
| `frais` | decimal(16,2) NOT NULL DEFAULT 0.00 | non | 0.00 |  |  |
| `idempr` | int(11) NOT NULL DEFAULT 0 | non | 0 |  | lien suppose -> empr.id_empr |
| `log_printed` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `log_mail` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  | donnee perso RGPD |

## `logopac`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 357 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 364/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_log` | int(8) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `date_log` | timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp() | non | current_timestamp() |  | date |
| `url_demandee` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `url_referente` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `get_log` | blob NOT NULL | non | — |  |  |
| `post_log` | blob NOT NULL | non | — |  |  |
| `num_session` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `server_log` | blob NOT NULL | non | — |  |  |
| `empr_carac` | blob NOT NULL | non | — |  | champ adherent |
| `empr_doc` | blob NOT NULL | non | — |  | champ adherent |
| `empr_expl` | mediumblob NOT NULL | non | — |  | champ adherent |
| `nb_result` | blob NOT NULL | non | — |  |  |
| `gen_stat` | blob NOT NULL | non | — |  |  |
| `validated` | tinyint(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `logs`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 365/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `uniqid_log` | varchar(13) NOT NULL DEFAULT '' | non | '' | PK |  |
| `log_service` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `log_type` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `log_module` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `log_label` | mediumtext DEFAULT NULL | oui | NULL |  |  |
| `log_message` | mediumtext DEFAULT NULL | oui | NULL |  |  |
| `log_date` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `log_url` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `log_num_user` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `log_type_user` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `log_data` | mediumtext DEFAULT NULL | oui | NULL |  |  |

## `mails`

Domaine probable : e-mails / files d'attente (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 113214 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 366/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_mail` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `mail_type` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | donnee perso RGPD |
| `mail_to_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `mail_to_mail` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | donnee perso RGPD |
| `mail_object` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | donnee perso RGPD |
| `mail_content` | mediumtext NOT NULL | non | — |  | donnee perso RGPD |
| `mail_from_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `mail_from_mail` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | donnee perso RGPD |
| `mail_headers` | text NOT NULL | non | — |  | donnee perso RGPD |
| `mail_copy_cc` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | donnee perso RGPD |
| `mail_copy_bcc` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | donnee perso RGPD |
| `mail_do_nl2br` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  | donnee perso RGPD |
| `mail_attachments` | text NOT NULL | non | — |  | donnee perso RGPD |
| `mail_reply_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `mail_reply_mail` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | donnee perso RGPD |
| `mail_date` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `mail_sended` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  | donnee perso RGPD |
| `mail_error` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | donnee perso RGPD |
| `mail_from_uri` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | donnee perso RGPD |
| `mail_num_campaign` | int(11) NOT NULL DEFAULT 0 | non | 0 |  | donnee perso RGPD |

## `mails_configuration`

Domaine probable : e-mails / files d'attente (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 24 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 367/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_mail_configuration` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `name_mail_configuration` | varchar(255) NOT NULL DEFAULT '' | non | '' | UNIQUE | donnee perso RGPD |
| `mail_configuration_type` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | donnee perso RGPD |
| `mail_configuration_protocol` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | donnee perso RGPD |
| `mail_configuration_hote` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | donnee perso RGPD |
| `mail_configuration_port` | int(11) NOT NULL DEFAULT 0 | non | 0 |  | donnee perso RGPD |
| `mail_configuration_authentication` | int(1) NOT NULL DEFAULT 0 | non | 0 |  | donnee perso RGPD |
| `mail_configuration_user` | mediumtext DEFAULT NULL | oui | NULL |  | donnee perso RGPD |
| `mail_configuration_password` | mediumtext DEFAULT NULL | oui | NULL |  | SECRET : ne pas reprendre (reinitialiser cote cible) |
| `mail_configuration_secure_protocol` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | donnee perso RGPD |
| `mail_configuration_authentification_type` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | donnee perso RGPD |
| `mail_configuration_authentification_type_settings` | mediumtext DEFAULT NULL | oui | NULL |  | donnee perso RGPD |
| `mail_configuration_allowed_hote_override` | int(1) NOT NULL DEFAULT 0 | non | 0 |  | donnee perso RGPD |
| `mail_configuration_allowed_authentification_override` | int(1) NOT NULL DEFAULT 0 | non | 0 |  | donnee perso RGPD |
| `mail_configuration_validated` | int(1) NOT NULL DEFAULT 0 | non | 0 |  | donnee perso RGPD |
| `mail_configuration_informations` | text NOT NULL | non | — |  | donnee perso RGPD |

## `mails_settings`

Domaine probable : e-mails / files d'attente (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 368/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_mail_setting` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `mail_setting_classname` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | donnee perso RGPD |
| `mail_setting_sender` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | donnee perso RGPD |
| `mail_setting_copy_cc` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | donnee perso RGPD |
| `mail_setting_copy_bcc` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | donnee perso RGPD |
| `mail_setting_reply` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | donnee perso RGPD |
| `mail_setting_associated_campaign` | int(1) NOT NULL DEFAULT 0 | non | 0 |  | donnee perso RGPD |

## `mails_waiting`

Domaine probable : e-mails / files d'attente (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 369/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_mail` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `mail_waiting_type` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | donnee perso RGPD |
| `mail_waiting_to_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `mail_waiting_to_mail` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | donnee perso RGPD |
| `mail_waiting_object` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | donnee perso RGPD |
| `mail_waiting_content` | mediumtext NOT NULL | non | — |  | donnee perso RGPD |
| `mail_waiting_from_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `mail_waiting_from_mail` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | donnee perso RGPD |
| `mail_waiting_headers` | text NOT NULL | non | — |  | donnee perso RGPD |
| `mail_waiting_copy_cc` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | donnee perso RGPD |
| `mail_waiting_copy_bcc` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | donnee perso RGPD |
| `mail_waiting_do_nl2br` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  | donnee perso RGPD |
| `mail_waiting_attachments` | text NOT NULL | non | — |  | donnee perso RGPD |
| `mail_waiting_reply_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `mail_waiting_reply_mail` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | donnee perso RGPD |
| `mail_waiting_date` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `mail_waiting_from_uri` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | donnee perso RGPD |
| `mail_waiting_num_campaign` | int(11) NOT NULL DEFAULT 0 | non | 0 |  | donnee perso RGPD |

## `mailtpl`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 4 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 370/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_mailtpl` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `mailtpl_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `mailtpl_objet` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | donnee perso RGPD |
| `mailtpl_tpl` | mediumtext NOT NULL | non | — |  | donnee perso RGPD |
| `mailtpl_users` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | donnee perso RGPD |

## `map_echelles`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 371/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `map_echelle_id` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `map_echelle_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |

## `map_emprises`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 372/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `map_emprise_id` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `map_emprise_type` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `map_emprise_obj_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `map_emprise_data` | geometry NOT NULL | non | — |  |  |
| `map_emprise_order` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `map_hold_areas`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 373/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_obj` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK | identifiant |
| `type_obj` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `area` | double DEFAULT NULL | oui | NULL |  |  |
| `bbox_area` | double DEFAULT NULL | oui | NULL |  |  |
| `center` | longtext CHARACTER SET latin1 COLLATE latin1_swedish_ci DEFAULT NULL | oui | NULL |  |  |

## `map_projections`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 374/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `map_projection_id` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `map_projection_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |

## `map_refs`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 375/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `map_ref_id` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `map_ref_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |

## `mfa_mail`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 376/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id` | int(11) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `context` | varchar(255) NOT NULL DEFAULT '' | non | '' | UNIQUE |  |
| `object` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `content` | mediumtext DEFAULT NULL | oui | NULL |  |  |

## `mfa_otp`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 377/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id` | int(11) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `context` | varchar(255) NOT NULL DEFAULT '' | non | '' | UNIQUE |  |
| `hash_method` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `lifetime` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `length_code` | int(2) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `mfa_services`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 378/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id` | int(11) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `context` | varchar(255) NOT NULL DEFAULT '' | non | '' | UNIQUE |  |
| `application` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `mail` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  | donnee perso RGPD |
| `sms` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `required` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `suggest_message` | mediumtext DEFAULT NULL | oui | NULL |  |  |

## `mfa_sms`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 379/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id` | int(11) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `context` | varchar(255) NOT NULL DEFAULT '' | non | '' | UNIQUE |  |
| `content` | mediumtext DEFAULT NULL | oui | NULL |  |  |

## `modules`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 380/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `module_name` | varchar(255) NOT NULL DEFAULT '' | non | '' | PK | libelle |
| `module_destination_link` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |

## `mots`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 39 (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 381/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_mot` | mediumint(8) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `mot` | varchar(100) NOT NULL DEFAULT '' | non | '' | UNIQUE |  |

## `noeuds`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 19098 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 382/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_noeud` | int(9) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `autorite` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `num_parent` | int(9) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_renvoi_voir` | int(9) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `visible` | char(1) NOT NULL DEFAULT '1' | non | '1' |  |  |
| `num_thesaurus` | int(3) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `path` | text NOT NULL | non | — |  |  |
| `authority_import_denied` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `not_use_in_indexation` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `nomenclature_children_records`

Domaine probable : musique : nomenclatures (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 383/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `child_record_num_record` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `child_record_num_formation` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `child_record_num_type` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `child_record_num_musicstand` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `child_record_num_instrument` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `child_record_effective` | varchar(10) NOT NULL DEFAULT '0' | non | '0' |  |  |
| `child_record_order` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `child_record_other` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `child_record_num_voice` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `child_record_num_workshop` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `child_record_num_nomenclature` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `nomenclature_exotic_instruments`

Domaine probable : musique : nomenclatures (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 384/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_exotic_instrument` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `exotic_instrument_num_nomenclature` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `exotic_instrument_num_instrument` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `exotic_instrument_number` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `exotic_instrument_order` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `nomenclature_exotic_other_instruments`

Domaine probable : musique : nomenclatures (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 385/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_exotic_other_instrument` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `exotic_other_instrument_num_exotic_instrument` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `exotic_other_instrument_num_instrument` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `exotic_other_instrument_order` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `nomenclature_families`

Domaine probable : musique : nomenclatures (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 386/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_family` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `family_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `family_order` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `nomenclature_formations`

Domaine probable : musique : nomenclatures (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 387/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_formation` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `formation_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `formation_nature` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `formation_order` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `nomenclature_instruments`

Domaine probable : musique : nomenclatures (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 388/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_instrument` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `instrument_code` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `instrument_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `instrument_musicstand_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `instrument_standard` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `nomenclature_musicstands`

Domaine probable : musique : nomenclatures (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 389/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_musicstand` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `musicstand_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `musicstand_famille_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `musicstand_division` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `musicstand_order` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `musicstand_workshop` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `nomenclature_notices_nomenclatures`

Domaine probable : musique : nomenclatures (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 390/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_notice_nomenclature` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `notice_nomenclature_num_notice` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `notice_nomenclature_num_formation` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `notice_nomenclature_num_type` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `notice_nomenclature_label` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `notice_nomenclature_abbreviation` | text NOT NULL | non | — |  |  |
| `notice_nomenclature_notes` | text NOT NULL | non | — |  |  |
| `notice_nomenclature_families_notes` | mediumtext NOT NULL | non | — |  |  |
| `notice_nomenclature_exotic_instruments_note` | text NOT NULL | non | — |  |  |
| `notice_nomenclature_order` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `nomenclature_types`

Domaine probable : musique : nomenclatures (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 391/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_type` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `type_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `type_formation_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `type_order` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `nomenclature_voices`

Domaine probable : musique : nomenclatures (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 392/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_voice` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `voice_code` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `voice_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `voice_order` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `nomenclature_workshops`

Domaine probable : musique : nomenclatures (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 393/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_workshop` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `workshop_label` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `workshop_num_nomenclature` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `workshop_order` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `workshop_defined` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `nomenclature_workshops_instruments`

Domaine probable : musique : nomenclatures (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 394/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_workshop_instrument` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `workshop_instrument_num_workshop` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `workshop_instrument_num_instrument` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `workshop_instrument_number` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `workshop_instrument_order` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `notice_onglet`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 395/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_onglet` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `onglet_name` | varchar(255) DEFAULT NULL | oui | NULL |  | libelle |

## `notice_statut`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 8 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 396/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_notice_statut` | smallint(5) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `gestion_libelle` | varchar(255) DEFAULT NULL | oui | NULL |  | libelle |
| `opac_libelle` | varchar(255) DEFAULT NULL | oui | NULL |  | libelle |
| `notice_visible_opac` | tinyint(1) NOT NULL DEFAULT 1 | non | 1 |  |  |
| `notice_visible_gestion` | tinyint(1) NOT NULL DEFAULT 1 | non | 1 |  |  |
| `expl_visible_opac` | tinyint(1) NOT NULL DEFAULT 1 | non | 1 |  | champ exemplaire |
| `class_html` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `notice_visible_opac_abon` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `expl_visible_opac_abon` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  | champ exemplaire |
| `explnum_visible_opac` | int(1) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |
| `explnum_visible_opac_abon` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `notice_scan_request_opac` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `notice_scan_request_opac_abon` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `notice_tpl`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 13 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 397/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `notpl_id` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `notpl_name` | varchar(256) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `notpl_code` | text NOT NULL | non | — |  |  |
| `notpl_comment` | varchar(256) NOT NULL DEFAULT '' | non | '' |  |  |
| `notpl_id_test` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `notpl_show_opac` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `notice_tplcode`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 398/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_notpl` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `notplcode_localisation` | mediumint(8) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `notplcode_typdoc` | char(2) NOT NULL DEFAULT 'a' | non | 'a' | PK |  |
| `notplcode_niveau_biblio` | char(1) NOT NULL DEFAULT 'm' | non | 'm' | PK |  |
| `notplcode_niveau_hierar` | char(1) NOT NULL DEFAULT '0' | non | '0' |  |  |
| `nottplcode_code` | text NOT NULL | non | — |  |  |

## `notice_usage`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 399/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_usage` | int(8) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `usage_libelle` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |

## `notices`

Notice bibliographique (livre, periodique, partition...). Coeur du catalogue.

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 140577 (borne sup, pas effectif), instructions INSERT : 107, preuve : CREATE TABLE observe (bloc 400/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `notice_id` | mediumint(8) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `typdoc` | char(2) NOT NULL DEFAULT 'a' | non | 'a' |  | metadonnee catalogue |
| `tit1` | text DEFAULT NULL | oui | NULL |  | titre |
| `tit2` | text DEFAULT NULL | oui | NULL |  | titre |
| `tit3` | text DEFAULT NULL | oui | NULL |  | titre |
| `tit4` | text DEFAULT NULL | oui | NULL |  | titre |
| `tparent_id` | mediumint(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  | identifiant |
| `tnvol` | varchar(100) NOT NULL DEFAULT '' | non | '' |  |  |
| `ed1_id` | mediumint(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  | identifiant |
| `ed2_id` | mediumint(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  | identifiant |
| `coll_id` | mediumint(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  | identifiant |
| `subcoll_id` | mediumint(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  | identifiant |
| `year` | varchar(50) DEFAULT NULL | oui | NULL |  | metadonnee catalogue |
| `nocoll` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `mention_edition` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `code` | varchar(50) NOT NULL DEFAULT '' | non | '' |  | metadonnee catalogue |
| `npages` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `ill` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `size` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `accomp` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `n_gen` | text NOT NULL | non | — |  |  |
| `n_contenu` | text NOT NULL | non | — |  |  |
| `n_resume` | text NOT NULL | non | — |  |  |
| `lien` | text NOT NULL | non | — |  |  |
| `eformat` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `index_l` | text NOT NULL | non | — |  |  |
| `indexint` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `index_serie` | tinytext DEFAULT NULL | oui | NULL |  |  |
| `index_matieres` | text NOT NULL | non | — |  |  |
| `niveau_biblio` | char(1) NOT NULL DEFAULT 'm' | non | 'm' |  | metadonnee catalogue |
| `niveau_hierar` | char(1) NOT NULL DEFAULT '0' | non | '0' |  | metadonnee catalogue |
| `origine_catalogage` | int(8) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |
| `prix` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | montant |
| `index_n_gen` | text DEFAULT NULL | oui | NULL |  |  |
| `index_n_contenu` | text DEFAULT NULL | oui | NULL |  |  |
| `index_n_resume` | text DEFAULT NULL | oui | NULL |  |  |
| `index_sew` | text DEFAULT NULL | oui | NULL |  |  |
| `index_wew` | text DEFAULT NULL | oui | NULL |  |  |
| `statut` | int(5) NOT NULL DEFAULT 1 | non | 1 |  | metadonnee catalogue |
| `commentaire_gestion` | text NOT NULL | non | — |  |  |
| `create_date` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `update_date` | timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp() | non | current_timestamp() |  | date |
| `signature` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `thumbnail_url` | mediumblob NOT NULL | non | — |  |  |
| `date_parution` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `opac_visible_bulletinage` | tinyint(3) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |
| `indexation_lang` | varchar(20) NOT NULL DEFAULT '' | non | '' |  |  |
| `opac_serialcirc_demande` | tinyint(3) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |
| `map_echelle_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `map_projection_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `map_ref_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `map_equinoxe` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `notice_is_new` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `notice_date_is_new` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE |  |
| `num_notice_usage` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  | lien suppose -> notices.notice_id |
| `is_numeric` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `notices_authorities_sources`

Domaine probable : catalogue : notices et liaisons (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 401/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_authority_source` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `num_notice` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK | lien suppose -> notices.notice_id |

## `notices_authperso`

Domaine probable : catalogue : notices et liaisons (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 402/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `notice_authperso_notice_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `notice_authperso_authority_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `notice_authperso_order` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `notices_categories`

Liaison notices <-> categories matiere.

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 403/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `notcateg_notice` | int(9) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `num_noeud` | int(9) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `num_vedette` | int(3) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `ordre_vedette` | int(3) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |
| `ordre_categorie` | smallint(2) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `notices_custom`

Domaine probable : catalogue : notices et liaisons (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 10 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 404/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `idchamp` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI |  |
| `name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `titre` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `type` | varchar(10) NOT NULL DEFAULT 'text' | non | 'text' |  |  |
| `datatype` | varchar(10) NOT NULL DEFAULT '' | non | '' |  |  |
| `options` | text DEFAULT NULL | oui | NULL |  |  |
| `multiple` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `obligatoire` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `ordre` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `search` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `export` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `filters` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `exclusion_obligatoire` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `pond` | int(11) NOT NULL DEFAULT 100 | non | 100 |  |  |
| `opac_sort` | int(11) NOT NULL DEFAULT 1 | non | 1 |  |  |
| `comment` | blob NOT NULL | non | — |  |  |
| `custom_classement` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `import` | int(1) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |

## `notices_custom_dates`

Domaine probable : catalogue : notices et liaisons (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 405/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `notices_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `notices_custom_origine` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `notices_custom_date_type` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `notices_custom_date_start` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `notices_custom_date_end` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `notices_custom_order` | int(11) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |

## `notices_custom_lists`

Domaine probable : catalogue : notices et liaisons (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 76 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 406/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_notices_custom_list` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `notices_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `notices_custom_list_value` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `notices_custom_list_lib` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `ordre` | int(11) DEFAULT NULL | oui | NULL |  |  |

## `notices_custom_values`

Domaine probable : catalogue : notices et liaisons (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 2, preuve : CREATE TABLE observe (bloc 407/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `notices_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `notices_custom_origine` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `notices_custom_small_text` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `notices_custom_text` | text DEFAULT NULL | oui | NULL |  |  |
| `notices_custom_integer` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `notices_custom_date` | date DEFAULT NULL | oui | NULL |  | date |
| `notices_custom_float` | float DEFAULT NULL | oui | NULL |  |  |
| `notices_custom_order` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `notices_externes`

Domaine probable : catalogue : notices et liaisons (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 408/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_notice` | int(11) NOT NULL DEFAULT 0 | non | 0 | PK | lien suppose -> notices.notice_id |
| `recid` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |

## `notices_fields_global_index`

Domaine probable : catalogue : notices et liaisons (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 276, preuve : CREATE TABLE observe (bloc 409/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_notice` | mediumint(8) NOT NULL DEFAULT 0 | non | 0 | PK | identifiant |
| `code_champ` | int(3) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `code_ss_champ` | int(3) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `ordre` | int(4) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `value` | text NOT NULL | non | — |  |  |
| `pond` | int(4) NOT NULL DEFAULT 100 | non | 100 |  |  |
| `lang` | varchar(10) NOT NULL DEFAULT '' | non | '' | PK |  |
| `authority_num` | varchar(50) NOT NULL DEFAULT '0' | non | '0' |  |  |

## `notices_global_index`

Domaine probable : catalogue : notices et liaisons (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 74, preuve : CREATE TABLE observe (bloc 410/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_notice` | mediumint(8) NOT NULL DEFAULT 0 | non | 0 | PK | lien suppose -> notices.notice_id |
| `no_index` | mediumint(8) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `infos_global` | text NOT NULL | non | — |  |  |
| `index_infos_global` | text NOT NULL | non | — |  |  |

## `notices_langues`

Domaine probable : catalogue : notices et liaisons (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 2, preuve : CREATE TABLE observe (bloc 411/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_notice` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 | PK | lien suppose -> notices.notice_id |
| `type_langue` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `code_langue` | char(3) NOT NULL DEFAULT '' | non | '' | PK |  |
| `ordre_langue` | smallint(2) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `notices_mots_global_index`

Domaine probable : catalogue : notices et liaisons (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 294, preuve : CREATE TABLE observe (bloc 412/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_notice` | mediumint(8) NOT NULL DEFAULT 0 | non | 0 | PK | identifiant |
| `code_champ` | int(3) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `code_ss_champ` | int(3) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `num_word` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `pond` | int(4) NOT NULL DEFAULT 100 | non | 100 |  |  |
| `position` | int(11) NOT NULL DEFAULT 1 | non | 1 | PK |  |
| `field_position` | int(11) NOT NULL DEFAULT 1 | non | 1 | PK |  |

## `notices_relations`

Liaisons entre notices (autres editions, suites...).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 7368 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 413/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_notices_relations` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `num_notice` | bigint(20) unsigned NOT NULL DEFAULT 0 | non | 0 |  | lien suppose -> notices.notice_id |
| `linked_notice` | bigint(20) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `relation_type` | char(1) NOT NULL DEFAULT '' | non | '' |  |  |
| `ranking` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `direction` | varchar(4) NOT NULL DEFAULT '' | non | '' |  |  |
| `num_reverse_link` | int(10) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `notices_titres_uniformes`

Domaine probable : catalogue : notices et liaisons (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 414/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `ntu_num_notice` | int(9) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `ntu_num_tu` | int(9) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `ntu_titre` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `ntu_date` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | date |
| `ntu_sous_vedette` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `ntu_langue` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `ntu_version` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `ntu_mention` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `ntu_ordre` | smallint(5) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `offres_remises`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 415/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_fournisseur` | int(5) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `num_produit` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `remise` | float(4,2) unsigned NOT NULL DEFAULT 0.00 | non | 0.00 |  |  |
| `condition_remise` | text DEFAULT NULL | oui | NULL |  |  |

## `onto_files`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 416/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_onto_file` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `onto_file_title` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `onto_file_description` | text NOT NULL | non | — |  |  |
| `onto_file_filename` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `onto_file_mimetype` | varchar(100) NOT NULL DEFAULT '' | non | '' |  |  |
| `onto_file_filesize` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `onto_file_vignette` | mediumblob NOT NULL | non | — |  |  |
| `onto_file_url` | text NOT NULL | non | — |  |  |
| `onto_file_path` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `onto_file_create_date` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `onto_file_num_storage` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `onto_file_type_object` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `onto_file_num_object` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `onto_uri`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 417/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `uri_id` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `uri` | varchar(255) NOT NULL DEFAULT '' | non | '' | UNIQUE |  |

## `ontodemo_g2t`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 418/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `g` | mediumint(8) unsigned NOT NULL | non | — | UNIQUE |  |
| `t` | mediumint(8) unsigned NOT NULL | non | — | UNIQUE |  |

## `ontodemo_id2val`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 731 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 419/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id` | mediumint(8) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,UNIQUE,AI | identifiant |
| `misc` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `val` | text NOT NULL | non | — |  |  |
| `val_type` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 | UNIQUE |  |

## `ontodemo_o2val`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 420/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id` | mediumint(8) unsigned NOT NULL | non | — | UNIQUE | identifiant |
| `misc` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `val_hash` | char(32) NOT NULL | non | — |  |  |
| `val` | text NOT NULL | non | — |  |  |

## `ontodemo_s2val`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 421/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id` | mediumint(8) unsigned NOT NULL | non | — | UNIQUE | identifiant |
| `misc` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `val_hash` | char(32) NOT NULL | non | — |  |  |
| `val` | text NOT NULL | non | — |  |  |

## `ontodemo_setting`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 422/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `k` | char(32) NOT NULL | non | — | UNIQUE |  |
| `val` | text NOT NULL | non | — |  |  |

## `ontodemo_triple`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 423/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `t` | mediumint(8) unsigned NOT NULL | non | — | UNIQUE |  |
| `s` | mediumint(8) unsigned NOT NULL | non | — |  |  |
| `p` | mediumint(8) unsigned NOT NULL | non | — |  |  |
| `o` | mediumint(8) unsigned NOT NULL | non | — |  |  |
| `o_lang_dt` | mediumint(8) unsigned NOT NULL | non | — |  |  |
| `o_comp` | char(35) NOT NULL | non | — |  |  |
| `s_type` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `o_type` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `misc` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `ontologies`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 424/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_ontology` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `ontology_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `ontology_description` | text NOT NULL | non | — |  |  |
| `ontology_creation_date` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `ontology_storage_id` | int(11) NOT NULL DEFAULT 0 | non | 0 |  | identifiant |
| `ontology_pmb_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |

## `ontology_g2t`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 425/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `g` | mediumint(8) unsigned NOT NULL | non | — | UNIQUE |  |
| `t` | mediumint(8) unsigned NOT NULL | non | — | UNIQUE |  |

## `ontology_id2val`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 426/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id` | mediumint(8) unsigned NOT NULL | non | — | UNIQUE | identifiant |
| `misc` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `val` | text NOT NULL | non | — |  |  |
| `val_type` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 | UNIQUE |  |

## `ontology_o2val`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 427/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id` | mediumint(8) unsigned NOT NULL | non | — | UNIQUE | identifiant |
| `misc` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `val_hash` | char(32) NOT NULL | non | — |  |  |
| `val` | text NOT NULL | non | — |  |  |

## `ontology_s2val`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 428/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id` | mediumint(8) unsigned NOT NULL | non | — | UNIQUE | identifiant |
| `misc` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `val_hash` | char(32) NOT NULL | non | — |  |  |
| `val` | text NOT NULL | non | — |  |  |

## `ontology_setting`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 429/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `k` | char(32) NOT NULL | non | — | UNIQUE |  |
| `val` | text NOT NULL | non | — |  |  |

## `ontology_triple`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 430/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `t` | mediumint(8) unsigned NOT NULL | non | — | UNIQUE |  |
| `s` | mediumint(8) unsigned NOT NULL | non | — |  |  |
| `p` | mediumint(8) unsigned NOT NULL | non | — |  |  |
| `o` | mediumint(8) unsigned NOT NULL | non | — |  |  |
| `o_lang_dt` | mediumint(8) unsigned NOT NULL | non | — |  |  |
| `o_comp` | char(35) NOT NULL | non | — |  |  |
| `s_type` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `o_type` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `misc` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `opac_filters`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 431/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `opac_filter_view_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `opac_filter_path` | varchar(20) NOT NULL DEFAULT '' | non | '' | PK |  |
| `opac_filter_param` | text NOT NULL | non | — |  |  |

## `opac_liste_lecture`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 432/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_liste` | int(8) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `nom_liste` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `description` | text DEFAULT NULL | oui | NULL |  |  |
| `public` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_empr` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `read_only` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `confidential` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `tag` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `allow_add_records` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `allow_remove_records` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `opac_liste_lecture_notices`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 433/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `opac_liste_lecture_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `opac_liste_lecture_notice_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `opac_liste_lecture_create_date` | timestamp NOT NULL DEFAULT current_timestamp() | non | current_timestamp() |  | date |
| `opac_liste_lecture_flag_ia` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `opac_login_attempt`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 434/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_opac_login_attempt` | int(11) NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `opac_login_attempt_ip` | varchar(45) NOT NULL | non | — | UNIQUE |  |
| `opac_login_attempt_login` | varchar(255) NOT NULL | non | — | UNIQUE |  |
| `opac_login_attempt_time` | datetime NOT NULL DEFAULT current_timestamp() | non | current_timestamp() | UNIQUE |  |
| `opac_login_attempt_success` | tinyint(4) NOT NULL | non | — |  |  |

## `opac_sessions`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 69, preuve : CREATE TABLE observe (bloc 435/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `empr_id` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK | identifiant |
| `session` | mediumblob DEFAULT NULL | oui | NULL |  |  |
| `date_rec` | timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp() | non | current_timestamp() |  | date |

## `opac_views`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 436/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `opac_view_id` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `opac_view_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `opac_view_query` | text NOT NULL | non | — |  |  |
| `opac_view_human_query` | text NOT NULL | non | — |  |  |
| `opac_view_param` | text NOT NULL | non | — |  |  |
| `opac_view_visible` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `opac_view_comment` | text NOT NULL | non | — |  |  |
| `opac_view_last_gen` | datetime DEFAULT NULL | oui | NULL |  |  |
| `opac_view_ttl` | int(11) NOT NULL DEFAULT 86400 | non | 86400 |  |  |

## `opac_views_empr`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 437/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `emprview_view_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `emprview_empr_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `emprview_default` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `origin_authorities`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 8 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 438/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_origin_authorities` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `origin_authorities_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `origin_authorities_country` | varchar(10) NOT NULL DEFAULT '' | non | '' |  |  |
| `origin_authorities_diffusible` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `origine_notice`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 110 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 439/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `orinot_id` | int(8) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `orinot_nom` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `orinot_pays` | varchar(255) NOT NULL DEFAULT 'FR' | non | 'FR' |  |  |
| `orinot_diffusion` | int(1) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |

## `ouvertures`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 440/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `date_ouverture` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | PK,DEFAUT MASQUE | date |
| `ouvert` | int(1) NOT NULL DEFAULT 1 | non | 1 |  |  |
| `commentaire` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `num_location` | int(3) unsigned NOT NULL DEFAULT 1 | non | 1 | PK |  |

## `paiements`

Referentiel : modes de paiement.

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 441/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_paiement` | int(8) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `libelle` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `commentaire` | text NOT NULL | non | — |  |  |

## `param_subst`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 442/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `subst_module_param` | varchar(20) NOT NULL DEFAULT '' | non | '' | PK |  |
| `subst_module_num` | int(2) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `subst_type_param` | varchar(20) NOT NULL DEFAULT '' | non | '' | PK |  |
| `subst_sstype_param` | varchar(255) NOT NULL DEFAULT '' | non | '' | PK |  |
| `subst_valeur_param` | text NOT NULL | non | — |  |  |
| `subst_comment_param` | longtext NOT NULL | non | — |  |  |

## `parametres`

Parametres generaux PMB (dont regles relance/amendes).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 1284 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 443/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_param` | int(6) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `type_param` | varchar(20) DEFAULT NULL | oui | NULL | UNIQUE |  |
| `sstype_param` | varchar(255) DEFAULT NULL | oui | NULL | UNIQUE |  |
| `valeur_param` | text DEFAULT NULL | oui | NULL |  |  |
| `comment_param` | longtext DEFAULT NULL | oui | NULL |  |  |
| `section_param` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `gestion` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `parametres2`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 934 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 444/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_param` | int(6) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `type_param` | varchar(20) DEFAULT NULL | oui | NULL | UNIQUE |  |
| `sstype_param` | varchar(255) DEFAULT NULL | oui | NULL | UNIQUE |  |
| `valeur_param` | text DEFAULT NULL | oui | NULL |  |  |
| `comment_param` | longtext DEFAULT NULL | oui | NULL |  |  |
| `section_param` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `gestion` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `parametres_uncached`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 2 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 445/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_param` | int(6) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `type_param` | varchar(20) DEFAULT NULL | oui | NULL | UNIQUE |  |
| `sstype_param` | varchar(255) DEFAULT NULL | oui | NULL | UNIQUE |  |
| `valeur_param` | text DEFAULT NULL | oui | NULL |  |  |
| `comment_param` | longtext DEFAULT NULL | oui | NULL |  |  |
| `section_param` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `gestion` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `payment_organization`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 446/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id` | int(11) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `name` | varchar(255) NOT NULL | non | — |  |  |
| `data` | mediumblob DEFAULT NULL | oui | NULL |  |  |

## `pclassement`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 103 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 447/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_pclass` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `name_pclass` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `typedoc` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `locations` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |

## `perio_relance`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 448/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `rel_id` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `rel_abt_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `rel_date_parution` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE |  |
| `rel_libelle_numero` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `rel_comment_gestion` | text NOT NULL | non | — |  |  |
| `rel_comment_opac` | text NOT NULL | non | — |  |  |
| `rel_nb` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `rel_date` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |

## `planificateur`

Domaine probable : taches planifiees (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 13 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 449/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_planificateur` | int(11) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `num_type_tache` | int(11) NOT NULL | non | — |  |  |
| `libelle_tache` | varchar(255) NOT NULL | non | — |  | libelle |
| `desc_tache` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `num_user` | int(11) NOT NULL | non | — |  |  |
| `param` | text DEFAULT NULL | oui | NULL |  |  |
| `statut` | tinyint(1) unsigned DEFAULT 0 | oui | 0 |  | metadonnee catalogue |
| `rep_upload` | int(8) DEFAULT NULL | oui | NULL |  |  |
| `path_upload` | text DEFAULT NULL | oui | NULL |  |  |
| `perio_heure` | varchar(28) DEFAULT NULL | oui | NULL |  |  |
| `perio_minute` | varchar(28) DEFAULT '01' | oui | '01' |  |  |
| `perio_jour_mois` | varchar(128) DEFAULT '*' | oui | '*' |  |  |
| `perio_jour` | varchar(128) DEFAULT NULL | oui | NULL |  |  |
| `perio_mois` | varchar(128) DEFAULT NULL | oui | NULL |  |  |
| `calc_next_heure_deb` | varchar(28) DEFAULT NULL | oui | NULL |  |  |
| `calc_next_date_deb` | date DEFAULT NULL | oui | NULL |  |  |

## `plugins`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 450/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_plugin` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `plugin_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `plugin_settings` | text NOT NULL | non | — |  |  |

## `pnb_loans`

Domaine probable : Pret Numerique en Bibliotheque (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 451/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_pnb_loan` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `pnb_loan_order_line_id` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | identifiant |
| `pnb_loan_link` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `pnb_loan_request_id` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | identifiant |
| `pnb_loan_num_expl` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `pnb_loan_num_loaner` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `pnb_loan_drm` | varchar(100) NOT NULL DEFAULT '' | non | '' |  |  |
| `pnb_loan_loanid` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |

## `pnb_orders`

Domaine probable : Pret Numerique en Bibliotheque (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 452/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_pnb_order` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `pnb_order_id_order` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `pnb_order_line_id` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | identifiant |
| `pnb_order_num_notice` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `pnb_order_loan_max_duration` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `pnb_order_nb_loans` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `pnb_order_nb_simultaneous_loans` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `pnb_order_nb_consult_in_situ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `pnb_order_nb_consult_ex_situ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `pnb_order_offer_date` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `pnb_order_offer_date_end` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE |  |
| `pnb_order_offer_duration` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `pnb_current_nta` | int(10) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `pnb_order_data` | blob NOT NULL | non | — |  |  |

## `pnb_orders_expl`

Domaine probable : Pret Numerique en Bibliotheque (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 453/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `pnb_order_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `pnb_order_expl_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |

## `portal_portal`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 454/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id` | int(11) NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `name` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `is_default` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `version_num` | int(11) DEFAULT NULL | oui | NULL |  |  |

## `portal_version`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 455/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id` | int(11) NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `name` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `portal_num` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `last_version_num` | int(11) DEFAULT 0 | oui | 0 |  |  |
| `create_at` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE |  |
| `properties` | mediumblob DEFAULT NULL | oui | NULL |  |  |

## `pret`

Prets en cours (cle = exemplaire). Retard si pret_retour < aujourd'hui.

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 456/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `pret_idempr` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  | lien suppose -> empr.id_empr |
| `pret_idexpl` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK | lien suppose -> exemplaires.expl_id |
| `pret_date` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `pret_retour` | date DEFAULT NULL | oui | NULL |  | champ circulation |
| `pret_arc_id` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  | identifiant |
| `niveau_relance` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `date_relance` | date DEFAULT '[masque: voir dump local]' | oui | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `printed` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `retour_initial` | date DEFAULT '[masque: voir dump local]' | oui | '[masque: voir dump local]' | DEFAUT MASQUE |  |
| `cpt_prolongation` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `pret_temp` | varchar(50) NOT NULL DEFAULT '' | non | '' |  | champ circulation |
| `short_loan_flag` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `pret_pnb_flag` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  | champ circulation |

## `pret_archive`

Historique des prets (denormalise arc_*). Volume le plus gros.

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 622242 (borne sup, pas effectif), instructions INSERT : 112, preuve : CREATE TABLE observe (bloc 457/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `arc_id` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `arc_debut` | datetime DEFAULT '[masque: voir dump local]' | oui | '[masque: voir dump local]' | DEFAUT MASQUE | champ circulation |
| `arc_fin` | datetime DEFAULT NULL | oui | NULL |  | champ circulation |
| `arc_id_empr` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  | lien suppose -> empr.id_empr |
| `arc_empr_cp` | varchar(10) NOT NULL DEFAULT '' | non | '' |  | champ circulation |
| `arc_empr_ville` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | champ circulation |
| `arc_empr_prof` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | champ circulation |
| `arc_empr_year` | int(4) unsigned DEFAULT 0 | oui | 0 |  | champ circulation |
| `arc_empr_categ` | smallint(5) unsigned DEFAULT 0 | oui | 0 |  | champ circulation |
| `arc_empr_codestat` | smallint(5) unsigned DEFAULT 0 | oui | 0 |  | champ circulation |
| `arc_empr_sexe` | tinyint(3) unsigned DEFAULT 0 | oui | 0 |  | champ circulation |
| `arc_empr_statut` | int(10) unsigned NOT NULL DEFAULT 1 | non | 1 |  | champ circulation |
| `arc_empr_location` | int(6) unsigned NOT NULL DEFAULT 0 | non | 0 |  | champ circulation |
| `arc_type_abt` | int(6) unsigned NOT NULL DEFAULT 0 | non | 0 |  | champ circulation |
| `arc_expl_typdoc` | int(5) unsigned DEFAULT 0 | oui | 0 |  | champ exemplaire |
| `arc_expl_cote` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | cote |
| `arc_expl_statut` | smallint(5) unsigned DEFAULT 0 | oui | 0 |  | champ exemplaire |
| `arc_expl_location` | smallint(5) unsigned DEFAULT 0 | oui | 0 |  | champ exemplaire |
| `arc_expl_location_origine` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  | champ exemplaire |
| `arc_expl_location_retour` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  | champ exemplaire |
| `arc_expl_codestat` | smallint(5) unsigned DEFAULT 0 | oui | 0 |  | champ exemplaire |
| `arc_expl_owner` | mediumint(8) unsigned DEFAULT 0 | oui | 0 |  | champ exemplaire |
| `arc_expl_section` | int(5) unsigned NOT NULL DEFAULT 0 | non | 0 |  | champ exemplaire |
| `arc_expl_id` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  | identifiant |
| `arc_expl_notice` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  | lien suppose -> notices.notice_id |
| `arc_expl_bulletin` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  | lien suppose -> bulletins.bulletin_id |
| `arc_groupe` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | champ circulation |
| `arc_niveau_relance` | int(1) unsigned DEFAULT 0 | oui | 0 |  | champ circulation |
| `arc_date_relance` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | champ circulation |
| `arc_printed` | int(1) unsigned DEFAULT 0 | oui | 0 |  | champ circulation |
| `arc_cpt_prolongation` | int(1) unsigned DEFAULT 0 | oui | 0 |  | champ circulation |
| `arc_short_loan_flag` | int(1) NOT NULL DEFAULT 0 | non | 0 |  | champ circulation |
| `arc_pnb_flag` | int(1) NOT NULL DEFAULT 0 | non | 0 |  | champ circulation |
| `arc_pret_source_device` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | champ circulation |
| `arc_retour_source_device` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | champ circulation |

## `pret_custom`

Domaine probable : circulation : prets (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 458/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `idchamp` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI |  |
| `name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `titre` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `type` | varchar(10) NOT NULL DEFAULT 'text' | non | 'text' |  |  |
| `datatype` | varchar(10) NOT NULL DEFAULT '' | non | '' |  |  |
| `options` | text DEFAULT NULL | oui | NULL |  |  |
| `multiple` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `obligatoire` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `ordre` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `search` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `export` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `filters` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `exclusion_obligatoire` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `pond` | int(11) NOT NULL DEFAULT 100 | non | 100 |  |  |
| `opac_sort` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `comment` | blob NOT NULL | non | — |  |  |
| `custom_classement` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |

## `pret_custom_dates`

Domaine probable : circulation : prets (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 459/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `pret_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK | champ circulation |
| `pret_custom_origine` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK | champ circulation |
| `pret_custom_date_type` | int(11) DEFAULT NULL | oui | NULL |  | champ circulation |
| `pret_custom_date_start` | int(11) NOT NULL DEFAULT 0 | non | 0 |  | champ circulation |
| `pret_custom_date_end` | int(11) NOT NULL DEFAULT 0 | non | 0 |  | champ circulation |
| `pret_custom_order` | int(11) unsigned NOT NULL DEFAULT 0 | non | 0 | PK | champ circulation |

## `pret_custom_lists`

Domaine probable : circulation : prets (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 460/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_pret_custom_list` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `pret_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  | champ circulation |
| `pret_custom_list_value` | varchar(255) DEFAULT NULL | oui | NULL |  | champ circulation |
| `pret_custom_list_lib` | varchar(255) DEFAULT NULL | oui | NULL |  | champ circulation |
| `ordre` | int(11) DEFAULT NULL | oui | NULL |  |  |

## `pret_custom_values`

Domaine probable : circulation : prets (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 461/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `pret_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  | champ circulation |
| `pret_custom_origine` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  | champ circulation |
| `pret_custom_small_text` | varchar(255) DEFAULT NULL | oui | NULL |  | champ circulation |
| `pret_custom_text` | text DEFAULT NULL | oui | NULL |  | champ circulation |
| `pret_custom_integer` | int(11) DEFAULT NULL | oui | NULL |  | champ circulation |
| `pret_custom_date` | date DEFAULT NULL | oui | NULL |  | date |
| `pret_custom_float` | float DEFAULT NULL | oui | NULL |  | champ circulation |
| `pret_custom_order` | int(11) NOT NULL DEFAULT 0 | non | 0 |  | champ circulation |

## `print_cart_tpl`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 2 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 462/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_print_cart_tpl` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `print_cart_tpl_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `print_cart_tpl_header` | text NOT NULL | non | — |  |  |
| `print_cart_tpl_footer` | text NOT NULL | non | — |  |  |

## `procs`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 398 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 463/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `idproc` | smallint(5) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI |  |
| `name` | varchar(255) NOT NULL | non | — |  |  |
| `requete` | blob NOT NULL | non | — |  |  |
| `comment` | tinytext NOT NULL | non | — |  |  |
| `autorisations` | mediumtext DEFAULT NULL | oui | NULL |  |  |
| `autorisations_all` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `parameters` | text DEFAULT NULL | oui | NULL |  |  |
| `num_classement` | int(5) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `proc_notice_tpl` | int(2) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `proc_notice_tpl_field` | varchar(255) NOT NULL | non | — |  |  |

## `procs_classements`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 26 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 464/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `idproc_classement` | smallint(5) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI |  |
| `libproc_classement` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |

## `publisher_custom`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 465/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `idchamp` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI |  |
| `num_type` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `titre` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `type` | varchar(10) NOT NULL DEFAULT 'text' | non | 'text' |  |  |
| `datatype` | varchar(10) NOT NULL DEFAULT '' | non | '' |  |  |
| `options` | text DEFAULT NULL | oui | NULL |  |  |
| `multiple` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `obligatoire` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `ordre` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `search` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `export` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `filters` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `exclusion_obligatoire` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `pond` | int(11) NOT NULL DEFAULT 100 | non | 100 |  |  |
| `opac_sort` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `comment` | blob NOT NULL | non | — |  |  |
| `custom_classement` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |

## `publisher_custom_dates`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 466/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `publisher_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `publisher_custom_origine` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `publisher_custom_date_type` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `publisher_custom_date_start` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `publisher_custom_date_end` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `publisher_custom_order` | int(11) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |

## `publisher_custom_lists`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 467/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_publisher_custom_list` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `publisher_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `publisher_custom_list_value` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `publisher_custom_list_lib` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `ordre` | int(11) DEFAULT NULL | oui | NULL |  |  |

## `publisher_custom_values`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 468/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `publisher_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `publisher_custom_origine` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `publisher_custom_small_text` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `publisher_custom_text` | text DEFAULT NULL | oui | NULL |  |  |
| `publisher_custom_integer` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `publisher_custom_date` | date DEFAULT NULL | oui | NULL |  | date |
| `publisher_custom_float` | float DEFAULT NULL | oui | NULL |  |  |
| `publisher_custom_order` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `publishers`

Autorite : editeurs.

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 12828 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 469/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `ed_id` | mediumint(8) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `ed_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `ed_adr1` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `ed_adr2` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `ed_cp` | varchar(10) NOT NULL DEFAULT '' | non | '' |  |  |
| `ed_ville` | varchar(96) NOT NULL DEFAULT '' | non | '' |  |  |
| `ed_pays` | varchar(96) NOT NULL DEFAULT '' | non | '' |  |  |
| `ed_web` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `index_publisher` | text DEFAULT NULL | oui | NULL |  |  |
| `ed_comment` | text DEFAULT NULL | oui | NULL |  |  |
| `ed_num_entite` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `quotas`

Quotas de pret par categorie/type.

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 470/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `quota_type` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `constraint_type` | varchar(255) NOT NULL DEFAULT '' | non | '' | PK |  |
| `elements` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `value` | float DEFAULT NULL | oui | NULL |  |  |

## `quotas_finance`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 471/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `quota_type` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `constraint_type` | varchar(255) NOT NULL DEFAULT '' | non | '' | PK |  |
| `elements` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `value` | float DEFAULT NULL | oui | NULL |  |  |

## `quotas_opac_views`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 472/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `quota_type` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `constraint_type` | varchar(255) NOT NULL DEFAULT '' | non | '' | PK |  |
| `elements` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `value` | text NOT NULL | non | — |  |  |

## `rapport_demandes`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 473/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_item` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `contenu` | text NOT NULL | non | — |  |  |
| `num_note` | int(10) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_demande` | int(10) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `ordre` | mediumint(3) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `type` | mediumint(2) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `rdfstore_g2t`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 474/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `g` | mediumint(8) unsigned NOT NULL | non | — | UNIQUE |  |
| `t` | mediumint(8) unsigned NOT NULL | non | — | UNIQUE |  |

## `rdfstore_id2val`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 475/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id` | mediumint(8) unsigned NOT NULL | non | — | UNIQUE | identifiant |
| `misc` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `val` | text NOT NULL | non | — |  |  |
| `val_type` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 | UNIQUE |  |

## `rdfstore_index`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 476/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_triple` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `subject_uri` | text NOT NULL | non | — |  |  |
| `subject_type` | text NOT NULL | non | — |  |  |
| `predicat_uri` | text NOT NULL | non | — |  |  |
| `num_object` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `object_val` | text NOT NULL | non | — |  |  |
| `object_index` | text NOT NULL | non | — |  |  |
| `object_lang` | char(5) NOT NULL DEFAULT '' | non | '' |  |  |

## `rdfstore_o2val`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 477/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id` | mediumint(8) unsigned NOT NULL | non | — | UNIQUE | identifiant |
| `misc` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `val_hash` | char(32) NOT NULL | non | — |  |  |
| `val` | text NOT NULL | non | — |  |  |

## `rdfstore_s2val`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 478/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id` | mediumint(8) unsigned NOT NULL | non | — | UNIQUE | identifiant |
| `misc` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `val_hash` | char(32) NOT NULL | non | — |  |  |
| `val` | text NOT NULL | non | — |  |  |

## `rdfstore_setting`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 479/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `k` | char(32) NOT NULL | non | — | UNIQUE |  |
| `val` | text NOT NULL | non | — |  |  |

## `rdfstore_triple`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 480/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `t` | mediumint(8) unsigned NOT NULL | non | — | UNIQUE |  |
| `s` | mediumint(8) unsigned NOT NULL | non | — |  |  |
| `p` | mediumint(8) unsigned NOT NULL | non | — |  |  |
| `o` | mediumint(8) unsigned NOT NULL | non | — |  |  |
| `o_lang_dt` | mediumint(8) unsigned NOT NULL | non | — |  |  |
| `o_comp` | char(35) NOT NULL | non | — |  |  |
| `s_type` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `o_type` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `misc` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `recouvrements`

Recouvrements (perdus, reclamations).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 95 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 481/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `recouvr_id` | int(16) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `empr_id` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  | identifiant |
| `id_expl` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  | identifiant |
| `date_rec` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `libelle` | varchar(255) DEFAULT NULL | oui | NULL |  | libelle |
| `montant` | decimal(16,2) DEFAULT 0.00 | oui | 0.00 |  | montant |
| `recouvr_type` | int(2) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `date_pret` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `date_relance1` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `date_relance2` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `date_relance3` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |

## `rent_account_types_sections`

Domaine probable : locations (comptes, facturation) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 482/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `account_type_num_exercice` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `account_type_num_section` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `account_type_marclist` | varchar(10) NOT NULL DEFAULT '' | non | '' | PK |  |

## `rent_accounts`

Domaine probable : locations (comptes, facturation) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 483/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_account` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `account_num_user` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `account_num_exercice` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `account_request_type` | varchar(3) NOT NULL DEFAULT '' | non | '' |  |  |
| `account_type` | varchar(3) NOT NULL DEFAULT '' | non | '' |  |  |
| `account_desc` | text DEFAULT NULL | oui | NULL |  |  |
| `account_date` | datetime DEFAULT NULL | oui | NULL |  | date |
| `account_receipt_limit_date` | datetime DEFAULT NULL | oui | NULL |  | date |
| `account_receipt_effective_date` | datetime DEFAULT NULL | oui | NULL |  | date |
| `account_return_date` | datetime DEFAULT NULL | oui | NULL |  | date |
| `account_num_uniform_title` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `account_title` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `account_event_date` | datetime DEFAULT NULL | oui | NULL |  | date |
| `account_event_formation` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `account_event_orchestra` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `account_event_place` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `account_num_publisher` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `account_num_supplier` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `account_num_author` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `account_num_pricing_system` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `account_time` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `account_percent` | float(8,2) unsigned NOT NULL DEFAULT 0.00 | non | 0.00 |  |  |
| `account_price` | float(12,2) unsigned NOT NULL DEFAULT 0.00 | non | 0.00 |  |  |
| `account_web` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `account_web_percent` | float(8,2) unsigned NOT NULL DEFAULT 0.00 | non | 0.00 |  |  |
| `account_web_price` | float(12,2) unsigned NOT NULL DEFAULT 0.00 | non | 0.00 |  |  |
| `account_comment` | text DEFAULT NULL | oui | NULL |  |  |
| `account_request_status` | int(1) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |
| `account_num_acte` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `account_diffusion_date` | datetime DEFAULT NULL | oui | NULL |  | date |
| `account_rights_date` | datetime DEFAULT NULL | oui | NULL |  | date |
| `account_unlimited_rights` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `rent_accounts_invoices`

Domaine probable : locations (comptes, facturation) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 484/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `account_invoice_num_account` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `account_invoice_num_invoice` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |

## `rent_invoices`

Domaine probable : locations (comptes, facturation) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 485/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_invoice` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `invoice_num_user` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `invoice_date` | datetime DEFAULT NULL | oui | NULL |  | date |
| `invoice_status` | int(10) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |
| `invoice_valid_date` | datetime DEFAULT NULL | oui | NULL |  | date |
| `invoice_destination` | varchar(10) NOT NULL DEFAULT '' | non | '' |  |  |
| `invoice_num_acte` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `rent_pricing_system_grids`

Domaine probable : locations (comptes, facturation) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 486/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_pricing_system_grid` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `pricing_system_grid_num_system` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `pricing_system_grid_time_start` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `pricing_system_grid_time_end` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `pricing_system_grid_price` | float(12,2) unsigned NOT NULL DEFAULT 0.00 | non | 0.00 |  |  |
| `pricing_system_grid_type` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `rent_pricing_systems`

Domaine probable : locations (comptes, facturation) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 487/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_pricing_system` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `pricing_system_label` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `pricing_system_desc` | text DEFAULT NULL | oui | NULL |  |  |
| `pricing_system_percents` | text DEFAULT NULL | oui | NULL |  |  |
| `pricing_system_num_exercice` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `resa`

Reservations en cours.

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 19270 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 488/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_resa` | mediumint(8) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `resa_idempr` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  | lien suppose -> empr.id_empr |
| `resa_idnotice` | mediumint(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  | lien suppose -> notices.notice_id |
| `resa_idbulletin` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  | lien suppose -> bulletins.bulletin_id |
| `resa_date` | datetime DEFAULT NULL | oui | NULL |  | date |
| `resa_date_debut` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | champ reservation |
| `resa_date_fin` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | champ reservation |
| `resa_cb` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | code-barres (unique observe) |
| `resa_confirmee` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  | champ reservation |
| `resa_loc_retrait` | smallint(5) unsigned NOT NULL DEFAULT 0 | non | 0 |  | champ reservation |
| `resa_arc` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  | champ reservation |
| `resa_planning_id_resa` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  | champ reservation |
| `resa_pnb_flag` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  | champ reservation |

## `resa_archive`

Historique des reservations.

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 19270 (borne sup, pas effectif), instructions INSERT : 4, preuve : CREATE TABLE observe (bloc 489/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `resarc_id` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `resarc_date` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `resarc_debut` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | champ reservation |
| `resarc_fin` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | champ reservation |
| `resarc_idnotice` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  | champ reservation |
| `resarc_idbulletin` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  | lien suppose -> bulletins.bulletin_id |
| `resarc_confirmee` | int(1) unsigned DEFAULT 0 | oui | 0 |  | champ reservation |
| `resarc_cb` | varchar(14) NOT NULL DEFAULT '' | non | '' |  | code-barres (unique observe) |
| `resarc_loc_retrait` | smallint(5) unsigned DEFAULT 0 | oui | 0 |  | champ reservation |
| `resarc_from_opac` | int(1) unsigned DEFAULT 0 | oui | 0 |  | champ reservation |
| `resarc_anulee` | int(1) unsigned DEFAULT 0 | oui | 0 |  | champ reservation |
| `resarc_pretee` | int(1) unsigned DEFAULT 0 | oui | 0 |  | champ reservation |
| `resarc_arcpretid` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  | champ reservation |
| `resarc_id_empr` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  | lien suppose -> empr.id_empr |
| `resarc_empr_cp` | varchar(10) NOT NULL DEFAULT '' | non | '' |  | champ reservation |
| `resarc_empr_ville` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | champ reservation |
| `resarc_empr_prof` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | champ reservation |
| `resarc_empr_year` | int(4) unsigned DEFAULT 0 | oui | 0 |  | champ reservation |
| `resarc_empr_categ` | smallint(5) unsigned DEFAULT 0 | oui | 0 |  | champ reservation |
| `resarc_empr_codestat` | smallint(5) unsigned DEFAULT 0 | oui | 0 |  | champ reservation |
| `resarc_empr_sexe` | tinyint(3) unsigned DEFAULT 0 | oui | 0 |  | champ reservation |
| `resarc_empr_location` | int(6) unsigned NOT NULL DEFAULT 1 | non | 1 |  | champ reservation |
| `resarc_expl_nb` | int(5) unsigned DEFAULT 0 | oui | 0 |  | champ reservation |
| `resarc_expl_typdoc` | int(5) unsigned DEFAULT 0 | oui | 0 |  | champ reservation |
| `resarc_expl_cote` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | champ reservation |
| `resarc_expl_statut` | smallint(5) unsigned DEFAULT 0 | oui | 0 |  | champ reservation |
| `resarc_expl_location` | smallint(5) unsigned DEFAULT 0 | oui | 0 |  | champ reservation |
| `resarc_expl_codestat` | smallint(5) unsigned DEFAULT 0 | oui | 0 |  | champ reservation |
| `resarc_expl_owner` | mediumint(8) unsigned DEFAULT 0 | oui | 0 |  | champ reservation |
| `resarc_expl_section` | int(5) unsigned NOT NULL DEFAULT 0 | non | 0 |  | champ reservation |
| `resarc_resa_planning_id_resa` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  | champ reservation |
| `resarc_pnb_flag` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  | champ reservation |

## `resa_loc`

Domaine probable : circulation : reservations (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 490/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `resa_loc` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 | PK | champ reservation |
| `resa_emprloc` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 | PK | champ reservation |

## `resa_planning`

Domaine probable : circulation : reservations (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 491/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_resa` | mediumint(8) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `resa_idempr` | mediumint(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  | lien suppose -> empr.id_empr |
| `resa_idnotice` | mediumint(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  | lien suppose -> notices.notice_id |
| `resa_idbulletin` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  | lien suppose -> bulletins.bulletin_id |
| `resa_date` | datetime DEFAULT NULL | oui | NULL |  | date |
| `resa_date_debut` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | champ reservation |
| `resa_date_fin` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | champ reservation |
| `resa_validee` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  | champ reservation |
| `resa_confirmee` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  | champ reservation |
| `resa_loc_retrait` | int(5) unsigned NOT NULL DEFAULT 0 | non | 0 |  | champ reservation |
| `resa_qty` | int(5) unsigned NOT NULL DEFAULT 1 | non | 1 |  | champ reservation |
| `resa_remaining_qty` | int(5) unsigned NOT NULL DEFAULT 1 | non | 1 |  | champ reservation |

## `resa_ranger`

Domaine probable : circulation : reservations (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 492/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `resa_cb` | varchar(255) NOT NULL DEFAULT '' | non | '' | PK | code-barres (unique observe) |

## `responsability`

Liaison notices <-> auteurs + fonction et ordre.

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 303151 (borne sup, pas effectif), instructions INSERT : 5, preuve : CREATE TABLE observe (bloc 493/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_responsability` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `responsability_author` | mediumint(8) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `responsability_notice` | mediumint(8) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `responsability_fonction` | varchar(4) NOT NULL DEFAULT '' | non | '' | PK |  |
| `responsability_type` | mediumint(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `responsability_ordre` | smallint(2) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `responsability_authperso`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 494/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_responsability_authperso` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `responsability_authperso_author` | mediumint(8) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `responsability_authperso_num` | mediumint(8) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `responsability_authperso_fonction` | varchar(4) NOT NULL DEFAULT '' | non | '' | PK |  |
| `responsability_authperso_type` | mediumint(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `responsability_authperso_ordre` | smallint(2) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `responsability_tu`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 495/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_responsability_tu` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `responsability_tu_author_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `responsability_tu_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `responsability_tu_fonction` | char(4) NOT NULL DEFAULT '' | non | '' | PK |  |
| `responsability_tu_type` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `responsability_tu_ordre` | smallint(2) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `rss_content`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 496/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `rss_id` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK | identifiant |
| `rss_content` | longblob NOT NULL | non | — |  |  |
| `rss_content_parse` | longblob NOT NULL | non | — |  |  |
| `rss_last` | timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp() | non | current_timestamp() |  |  |

## `rss_flux`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 5 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 497/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_rss_flux` | int(9) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `nom_rss_flux` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `link_rss_flux` | blob NOT NULL | non | — |  |  |
| `descr_rss_flux` | blob NOT NULL | non | — |  |  |
| `metadata_rss_flux` | int(1) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |
| `lang_rss_flux` | varchar(255) NOT NULL DEFAULT 'fr' | non | 'fr' |  |  |
| `copy_rss_flux` | blob NOT NULL | non | — |  |  |
| `editor_rss_flux` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `webmaster_rss_flux` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `ttl_rss_flux` | int(9) unsigned NOT NULL DEFAULT 60 | non | 60 |  |  |
| `img_url_rss_flux` | blob NOT NULL | non | — |  |  |
| `img_title_rss_flux` | blob NOT NULL | non | — |  |  |
| `img_link_rss_flux` | blob NOT NULL | non | — |  |  |
| `format_flux` | blob NOT NULL | non | — |  |  |
| `rss_flux_content` | longblob NOT NULL | non | — |  |  |
| `rss_flux_last` | timestamp NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE |  |
| `export_court_flux` | tinyint(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `tpl_title_rss_flux` | varchar(255) DEFAULT '0' | oui | '0' |  |  |
| `tpl_rss_flux` | varchar(255) DEFAULT '0' | oui | '0' |  |  |
| `tpl_link_rss_flux` | varchar(255) DEFAULT '0' | oui | '0' |  |  |
| `id_tri_rss_flux` | int(11) NOT NULL DEFAULT 0 | non | 0 |  | identifiant |

## `rss_flux_content`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 498/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_rss_flux` | int(9) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `type_contenant` | char(3) NOT NULL DEFAULT 'BAN' | non | 'BAN' | PK |  |
| `num_contenant` | int(9) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |

## `rubriques`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 499/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_rubrique` | int(8) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `num_budget` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_parent` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `libelle` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `commentaires` | text NOT NULL | non | — |  |  |
| `montant` | float(12,2) unsigned NOT NULL DEFAULT 0.00 | non | 0.00 |  | montant |
| `num_cp_compta` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `autorisations` | mediumtext NOT NULL | non | — |  |  |

## `sauv_lieux`

Domaine probable : sauvegardes internes PMB (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 2 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 500/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `sauv_lieu_id` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `sauv_lieu_nom` | varchar(50) DEFAULT NULL | oui | NULL |  |  |
| `sauv_lieu_url` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `sauv_lieu_protocol` | varchar(10) DEFAULT 'file' | oui | 'file' |  |  |
| `sauv_lieu_host` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `sauv_lieu_login` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `sauv_lieu_password` | varchar(255) DEFAULT NULL | oui | NULL |  | SECRET : ne pas reprendre (reinitialiser cote cible) |

## `sauv_log`

Domaine probable : sauvegardes internes PMB (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 12 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 501/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `sauv_log_id` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `sauv_log_start_date` | date DEFAULT NULL | oui | NULL |  | date |
| `sauv_log_file` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `sauv_log_succeed` | int(11) DEFAULT 0 | oui | 0 |  |  |
| `sauv_log_messages` | mediumtext DEFAULT NULL | oui | NULL |  |  |
| `sauv_log_userid` | int(11) DEFAULT NULL | oui | NULL |  |  |

## `sauv_sauvegardes`

Domaine probable : sauvegardes internes PMB (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 3 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 502/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `sauv_sauvegarde_id` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `sauv_sauvegarde_nom` | varchar(50) DEFAULT NULL | oui | NULL |  |  |
| `sauv_sauvegarde_file_prefix` | varchar(20) DEFAULT NULL | oui | NULL |  |  |
| `sauv_sauvegarde_tables` | mediumtext DEFAULT NULL | oui | NULL |  |  |
| `sauv_sauvegarde_lieux` | mediumtext DEFAULT NULL | oui | NULL |  |  |
| `sauv_sauvegarde_users` | mediumtext DEFAULT NULL | oui | NULL |  |  |
| `sauv_sauvegarde_compress` | int(11) DEFAULT 0 | oui | 0 |  |  |
| `sauv_sauvegarde_compress_command` | mediumtext DEFAULT NULL | oui | NULL |  |  |
| `sauv_sauvegarde_crypt` | int(11) DEFAULT 0 | oui | 0 |  |  |
| `sauv_sauvegarde_key1` | varchar(32) DEFAULT NULL | oui | NULL |  |  |
| `sauv_sauvegarde_key2` | varchar(32) DEFAULT NULL | oui | NULL |  |  |

## `sauv_tables`

Domaine probable : sauvegardes internes PMB (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 3 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 503/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `sauv_table_id` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `sauv_table_nom` | varchar(50) DEFAULT NULL | oui | NULL | UNIQUE |  |
| `sauv_table_tables` | text DEFAULT NULL | oui | NULL |  |  |

## `scan_request_explnum`

Domaine probable : numerisation a la demande (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 504/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `scan_request_explnum_num_request` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `scan_request_explnum_num_notice` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `scan_request_explnum_num_bulletin` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  | lien suppose -> bulletins.bulletin_id |
| `scan_request_explnum_num_explnum` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |

## `scan_request_linked_records`

Domaine probable : numerisation a la demande (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 505/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `scan_request_linked_record_num_request` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `scan_request_linked_record_num_notice` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `scan_request_linked_record_num_bulletin` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `scan_request_linked_record_comment` | text DEFAULT NULL | oui | NULL |  |  |
| `scan_request_linked_record_order` | int(3) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `scan_request_priorities`

Domaine probable : numerisation a la demande (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 506/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_scan_request_priority` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `scan_request_priority_label` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `scan_request_priority_weight` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `scan_request_status`

Domaine probable : numerisation a la demande (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 2 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 507/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_scan_request_status` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `scan_request_status_label` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `scan_request_status_opac_show` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `scan_request_status_cancelable` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `scan_request_status_infos_editable` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `scan_request_status_class_html` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `scan_request_status_is_closed` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `scan_request_status_workflow`

Domaine probable : numerisation a la demande (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 508/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `scan_request_status_workflow_from_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `scan_request_status_workflow_to_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |

## `scan_requests`

Domaine probable : numerisation a la demande (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 509/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_scan_request` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `scan_request_title` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `scan_request_desc` | text DEFAULT NULL | oui | NULL |  |  |
| `scan_request_num_status` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `scan_request_num_priority` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `scan_request_create_date` | datetime DEFAULT NULL | oui | NULL |  | date |
| `scan_request_update_date` | datetime DEFAULT NULL | oui | NULL |  | date |
| `scan_request_date` | datetime DEFAULT NULL | oui | NULL |  | date |
| `scan_request_wish_date` | datetime DEFAULT NULL | oui | NULL |  | date |
| `scan_request_deadline_date` | datetime DEFAULT NULL | oui | NULL |  | date |
| `scan_request_comment` | text DEFAULT NULL | oui | NULL |  |  |
| `scan_request_elapsed_time` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `scan_request_num_dest_empr` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `scan_request_num_creator` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `scan_request_type_creator` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `scan_request_num_last_user` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `scan_request_state` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `scan_request_as_folder` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `scan_request_folder_num_notice` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `scan_request_concept_uri` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `scan_request_nb_scanned_pages` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `scan_request_num_location` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `search_cache`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 510/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `object_id` | varchar(255) NOT NULL DEFAULT '' | non | '' | PK | identifiant |
| `delete_on_date` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `value` | mediumblob NOT NULL | non | — |  |  |

## `search_perso`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 75 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 511/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `search_id` | int(8) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `search_type` | varchar(255) NOT NULL DEFAULT 'RECORDS' | non | 'RECORDS' |  |  |
| `num_user` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `search_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `search_shortname` | varchar(50) NOT NULL DEFAULT '' | non | '' |  |  |
| `search_query` | text NOT NULL | non | — |  |  |
| `search_human` | text NOT NULL | non | — |  |  |
| `search_directlink` | tinyint(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `autorisations` | mediumtext DEFAULT NULL | oui | NULL |  |  |
| `search_order` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `search_comment` | text NOT NULL | non | — |  |  |

## `search_persopac`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 6 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 512/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `search_id` | int(8) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `num_empr` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `search_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `search_shortname` | varchar(50) NOT NULL DEFAULT '' | non | '' |  |  |
| `search_button_label` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `search_query` | text NOT NULL | non | — |  |  |
| `search_human` | text NOT NULL | non | — |  |  |
| `search_directlink` | tinyint(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `search_limitsearch` | tinyint(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `search_order` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `search_type` | varchar(255) NOT NULL DEFAULT 'record' | non | 'record' |  |  |
| `search_opac_views_num` | text NOT NULL | non | — |  |  |

## `search_persopac_empr_categ`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 513/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_categ_empr` | int(11) NOT NULL DEFAULT 0 | non | 0 |  | identifiant |
| `id_search_persopac` | int(11) NOT NULL DEFAULT 0 | non | 0 |  | identifiant |

## `search_segments`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 514/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_search_segment` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `search_segment_label` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `search_segment_description` | text DEFAULT NULL | oui | NULL |  |  |
| `search_segment_template_directory` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `search_segment_num_universe` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `search_segment_type` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `search_segment_order` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `search_segment_set` | text DEFAULT NULL | oui | NULL |  |  |
| `search_segment_logo` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `search_segment_sort` | text NOT NULL | non | — |  |  |
| `search_segment_rmc_enabled` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `search_segment_data` | varchar(255) DEFAULT NULL | oui | NULL |  |  |

## `search_segments_associated_universes`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 515/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_segment` | int(10) NOT NULL | non | — | PK |  |
| `num_universe` | int(10) NOT NULL | non | — | PK |  |

## `search_segments_facets`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 516/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_search_segment` | int(11) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `num_facet` | int(11) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `search_segment_facet_order` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `search_segments_search_perso`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 517/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_search_segment` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `num_search_perso` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `search_segment_search_perso_opac` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `search_segment_search_perso_order` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `search_universes`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 518/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_search_universe` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `search_universe_label` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `search_universe_description` | text DEFAULT NULL | oui | NULL |  |  |
| `search_universe_template_directory` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `search_universe_opac_views` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `search_universe_default_segment` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `search_universe_rmc_enabled` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `search_universe_settings` | text DEFAULT NULL | oui | NULL |  |  |

## `selectors`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 519/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `selector_name` | varchar(255) NOT NULL DEFAULT '' | non | '' | PK | libelle |
| `selector_parameters_tabs` | mediumtext DEFAULT NULL | oui | NULL |  |  |
| `selector_display_modes` | mediumtext DEFAULT NULL | oui | NULL |  |  |

## `serialcirc`

Domaine probable : circulation des periodiques (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 520/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_serialcirc` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `num_serialcirc_abt` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `serialcirc_type` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `serialcirc_virtual` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `serialcirc_duration` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `serialcirc_checked` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `serialcirc_retard_mode` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `serialcirc_allow_resa` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `serialcirc_allow_copy` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `serialcirc_allow_send_ask` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `serialcirc_allow_subscription` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `serialcirc_duration_before_send` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `serialcirc_expl_statut_circ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `serialcirc_expl_statut_circ_after` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `serialcirc_state` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `serialcirc_tpl` | text NOT NULL | non | — |  |  |
| `serialcirc_piedpage` | text NOT NULL | non | — |  |  |
| `serialcirc_no_ret` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `serialcirc_sort_diff` | text NOT NULL | non | — |  |  |
| `serialcirc_simple` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `serialcirc_ask`

Domaine probable : circulation des periodiques (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 521/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_serialcirc_ask` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `num_serialcirc_ask_perio` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_serialcirc_ask_serialcirc` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_serialcirc_ask_empr` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `serialcirc_ask_type` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `serialcirc_ask_statut` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `serialcirc_ask_date` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `serialcirc_ask_comment` | text NOT NULL | non | — |  |  |

## `serialcirc_circ`

Domaine probable : circulation des periodiques (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 522/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_serialcirc_circ` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `num_serialcirc_circ_diff` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_serialcirc_circ_expl` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_serialcirc_circ_empr` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_serialcirc_circ_serialcirc` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `serialcirc_circ_order` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `serialcirc_circ_subscription` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `serialcirc_circ_hold_asked` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `serialcirc_circ_ret_asked` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `serialcirc_circ_trans_asked` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `serialcirc_circ_trans_doc_asked` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `serialcirc_circ_expected_date` | datetime DEFAULT NULL | oui | NULL |  | date |
| `serialcirc_circ_pointed_date` | datetime DEFAULT NULL | oui | NULL |  | date |
| `serialcirc_circ_group_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |

## `serialcirc_copy`

Domaine probable : circulation des periodiques (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 523/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_serialcirc_copy` | int(11) NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `num_serialcirc_copy_empr` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_serialcirc_copy_bulletin` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `serialcirc_copy_analysis` | text DEFAULT NULL | oui | NULL |  |  |
| `serialcirc_copy_date` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `serialcirc_copy_state` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `serialcirc_copy_comment` | text NOT NULL | non | — |  |  |

## `serialcirc_diff`

Domaine probable : circulation des periodiques (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 524/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_serialcirc_diff` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `num_serialcirc_diff_serialcirc` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `serialcirc_diff_empr_type` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `serialcirc_diff_type_diff` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_serialcirc_diff_empr` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `serialcirc_diff_group_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `serialcirc_diff_duration` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `serialcirc_diff_order` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `serialcirc_expl`

Domaine probable : circulation des periodiques (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 525/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_serialcirc_expl` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `num_serialcirc_expl_id` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  | identifiant |
| `num_serialcirc_expl_serialcirc` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `serialcirc_expl_bulletine_date` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | lien suppose -> bulletins.bulletin_id |
| `serialcirc_expl_state_circ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_serialcirc_expl_serialcirc_diff` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `serialcirc_expl_ret_asked` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `serialcirc_expl_trans_asked` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `serialcirc_expl_trans_doc_asked` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_serialcirc_expl_current_empr` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `serialcirc_expl_start_date` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |

## `serialcirc_group`

Domaine probable : circulation des periodiques (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 526/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_serialcirc_group` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `num_serialcirc_group_diff` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_serialcirc_group_empr` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `serialcirc_group_responsable` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `serialcirc_group_order` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `serialcirc_tpl`

Domaine probable : circulation des periodiques (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 2 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 527/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `serialcirctpl_id` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `serialcirctpl_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `serialcirctpl_comment` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `serialcirctpl_tpl` | text NOT NULL | non | — |  |  |
| `serialcirctpl_piedpage` | text NOT NULL | non | — |  |  |

## `serie_custom`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 528/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `idchamp` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI |  |
| `num_type` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `titre` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `type` | varchar(10) NOT NULL DEFAULT 'text' | non | 'text' |  |  |
| `datatype` | varchar(10) NOT NULL DEFAULT '' | non | '' |  |  |
| `options` | text DEFAULT NULL | oui | NULL |  |  |
| `multiple` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `obligatoire` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `ordre` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `search` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `export` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `filters` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `exclusion_obligatoire` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `pond` | int(11) NOT NULL DEFAULT 100 | non | 100 |  |  |
| `opac_sort` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `comment` | blob NOT NULL | non | — |  |  |
| `custom_classement` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |

## `serie_custom_dates`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 529/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `serie_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `serie_custom_origine` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `serie_custom_date_type` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `serie_custom_date_start` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `serie_custom_date_end` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `serie_custom_order` | int(11) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |

## `serie_custom_lists`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 530/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_serie_custom_list` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `serie_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `serie_custom_list_value` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `serie_custom_list_lib` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `ordre` | int(11) DEFAULT NULL | oui | NULL |  |  |

## `serie_custom_values`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 531/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `serie_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `serie_custom_origine` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `serie_custom_small_text` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `serie_custom_text` | text DEFAULT NULL | oui | NULL |  |  |
| `serie_custom_integer` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `serie_custom_date` | date DEFAULT NULL | oui | NULL |  | date |
| `serie_custom_float` | float DEFAULT NULL | oui | NULL |  |  |
| `serie_custom_order` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `series`

Autorite : series.

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 5102 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 532/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `serie_id` | mediumint(8) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `serie_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `serie_index` | text DEFAULT NULL | oui | NULL |  |  |

## `sessions`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 533/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `SESSID` | varchar(12) NOT NULL DEFAULT '' | non | '' | PK |  |
| `login` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `IP` | varchar(20) NOT NULL DEFAULT '' | non | '' |  |  |
| `SESSstart` | varchar(12) NOT NULL DEFAULT '' | non | '' |  |  |
| `LastOn` | varchar(12) NOT NULL DEFAULT '' | non | '' |  |  |
| `SESSNAME` | varchar(25) NOT NULL DEFAULT '' | non | '' |  |  |
| `notifications` | text DEFAULT NULL | oui | NULL |  |  |

## `sessions_tokens`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 534/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `sessions_tokens_SESSID` | varchar(12) NOT NULL DEFAULT '' | non | '' | PK | SECRET : ne pas reprendre (reinitialiser cote cible) |
| `sessions_tokens_token` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | SECRET : ne pas reprendre (reinitialiser cote cible) |
| `sessions_tokens_type` | varchar(255) NOT NULL DEFAULT '' | non | '' | PK | SECRET : ne pas reprendre (reinitialiser cote cible) |

## `shorturls`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 178687 (borne sup, pas effectif), instructions INSERT : 126, preuve : CREATE TABLE observe (bloc 535/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_shorturl` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `shorturl_hash` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `shorturl_last_access` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE |  |
| `shorturl_context` | text NOT NULL | non | — |  |  |
| `shorturl_type` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `shorturl_action` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |

## `skos_custom`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 536/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `idchamp` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI |  |
| `name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `titre` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `type` | varchar(10) NOT NULL DEFAULT 'text' | non | 'text' |  |  |
| `datatype` | varchar(10) NOT NULL DEFAULT '' | non | '' |  |  |
| `options` | text DEFAULT NULL | oui | NULL |  |  |
| `multiple` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `obligatoire` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `ordre` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `search` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `export` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `filters` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `exclusion_obligatoire` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `pond` | int(11) NOT NULL DEFAULT 100 | non | 100 |  |  |
| `opac_sort` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `comment` | blob NOT NULL | non | — |  |  |
| `custom_classement` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |

## `skos_custom_dates`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 537/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `skos_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `skos_custom_origine` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `skos_custom_date_type` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `skos_custom_date_start` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `skos_custom_date_end` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `skos_custom_order` | int(11) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |

## `skos_custom_lists`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 538/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_skos_custom_list` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `skos_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `skos_custom_list_value` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `skos_custom_list_lib` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `ordre` | int(11) DEFAULT NULL | oui | NULL |  |  |

## `skos_custom_values`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 539/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `skos_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `skos_custom_origine` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `skos_custom_small_text` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `skos_custom_text` | text DEFAULT NULL | oui | NULL |  |  |
| `skos_custom_integer` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `skos_custom_date` | date DEFAULT NULL | oui | NULL |  | date |
| `skos_custom_float` | float DEFAULT NULL | oui | NULL |  |  |
| `skos_custom_order` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `skos_fields_global_index`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 540/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_item` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK | identifiant |
| `code_champ` | int(3) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `code_ss_champ` | int(3) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `ordre` | int(4) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `value` | text NOT NULL | non | — |  |  |
| `pond` | int(4) unsigned NOT NULL DEFAULT 100 | non | 100 |  |  |
| `lang` | varchar(10) NOT NULL DEFAULT '' | non | '' | PK |  |
| `authority_num` | varchar(50) NOT NULL DEFAULT '0' | non | '0' |  |  |

## `skos_words_global_index`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 541/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_item` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK | identifiant |
| `code_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `code_ss_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `num_word` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `pond` | int(10) unsigned NOT NULL DEFAULT 100 | non | 100 |  |  |
| `position` | int(10) unsigned NOT NULL DEFAULT 1 | non | 1 | PK |  |
| `field_position` | int(10) unsigned NOT NULL DEFAULT 1 | non | 1 | PK |  |

## `source_sync`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 542/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `source_id` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK | identifiant |
| `nrecu` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `ntotal` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `message` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `date_sync` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `percent` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `env` | text NOT NULL | non | — |  |  |
| `cancel` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `sources_enrichment`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 543/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `source_enrichment_num` | int(11) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `source_enrichment_typnotice` | varchar(2) NOT NULL DEFAULT '' | non | '' | PK |  |
| `source_enrichment_typdoc` | varchar(2) NOT NULL DEFAULT '' | non | '' | PK |  |
| `source_enrichment_params` | text NOT NULL | non | — |  |  |

## `statopac`

Domaine probable : statistiques OPAC (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 2890167 (borne sup, pas effectif), instructions INSERT : 13, preuve : CREATE TABLE observe (bloc 544/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_log` | int(8) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `date_log` | timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp() | non | current_timestamp() |  | date |
| `url_demandee` | varchar(255) NOT NULL | non | — |  |  |
| `url_referente` | varchar(255) NOT NULL | non | — |  |  |
| `get_log` | blob NOT NULL | non | — |  |  |
| `post_log` | blob NOT NULL | non | — |  |  |
| `num_session` | varchar(255) NOT NULL DEFAULT '0' | non | '0' |  |  |
| `server_log` | blob NOT NULL | non | — |  |  |
| `empr_carac` | blob NOT NULL | non | — |  | champ adherent |
| `empr_doc` | blob NOT NULL | non | — |  | champ adherent |
| `empr_expl` | mediumblob NOT NULL | non | — |  | champ adherent |
| `nb_result` | blob NOT NULL | non | — |  |  |
| `gen_stat` | blob NOT NULL | non | — |  |  |

## `statopac_request`

Domaine probable : statistiques OPAC (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 14 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 545/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `idproc` | int(8) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI |  |
| `name` | varchar(255) NOT NULL | non | — |  |  |
| `requete` | blob NOT NULL | non | — |  |  |
| `comment` | tinytext NOT NULL | non | — |  |  |
| `parameters` | text NOT NULL | non | — |  |  |
| `num_vue` | mediumint(8) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `autorisations` | mediumtext NOT NULL | non | — |  |  |
| `autorisations_all` | int(1) NOT NULL DEFAULT 1 | non | 1 |  |  |

## `statopac_vue_1`

Domaine probable : statistiques OPAC (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 2887579 (borne sup, pas effectif), instructions INSERT : 387, preuve : CREATE TABLE observe (bloc 546/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_ligne` | int(8) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `id_session` | varchar(255) NOT NULL | non | — |  | identifiant |
| `date` | date NOT NULL | non | — |  |  |
| `adresse_IP` | varchar(255) NOT NULL | non | — |  |  |
| `url_asked` | varchar(255) NOT NULL | non | — |  |  |

## `statopac_vue_2`

Domaine probable : statistiques OPAC (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 2887579 (borne sup, pas effectif), instructions INSERT : 322, preuve : CREATE TABLE observe (bloc 547/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_ligne` | int(8) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `date` | date NOT NULL | non | — |  |  |
| `mots_saisis` | varchar(255) NOT NULL | non | — |  |  |
| `page_subtype` | int(11) NOT NULL | non | — |  |  |
| `pages_subtype_txt` | varchar(255) NOT NULL | non | — |  |  |
| `page_type` | int(11) NOT NULL | non | — |  |  |
| `nb_result` | int(11) NOT NULL | non | — |  |  |
| `multi_label` | varchar(255) NOT NULL | non | — |  |  |
| `multi_content` | varchar(255) NOT NULL | non | — |  |  |
| `multi_title` | varchar(255) NOT NULL | non | — |  |  |

## `statopac_vue_3`

Domaine probable : statistiques OPAC (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 2887579 (borne sup, pas effectif), instructions INSERT : 608, preuve : CREATE TABLE observe (bloc 548/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_ligne` | int(8) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `num_session` | varchar(255) NOT NULL | non | — |  |  |
| `timestamp` | datetime NOT NULL | non | — |  |  |
| `date` | date NOT NULL | non | — |  |  |
| `url_target` | text NOT NULL | non | — |  |  |
| `url_origine` | text NOT NULL | non | — |  |  |
| `page_subtype` | int(11) NOT NULL | non | — |  |  |
| `page_subtype_text` | varchar(255) NOT NULL | non | — |  |  |
| `page_type` | int(11) NOT NULL | non | — |  |  |
| `page_type_text` | varchar(255) NOT NULL | non | — |  |  |
| `location` | varchar(255) NOT NULL | non | — |  |  |

## `statopac_vue_4`

Domaine probable : statistiques OPAC (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 549/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_ligne` | int(8) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `location` | varchar(255) NOT NULL | non | — |  |  |
| `page_subtype` | int(11) NOT NULL | non | — |  |  |
| `pages_subtype_txt` | varchar(255) NOT NULL | non | — |  |  |
| `date` | date NOT NULL | non | — |  |  |
| `num_session` | varchar(255) NOT NULL | non | — |  |  |
| `age` | int(11) NOT NULL | non | — |  |  |
| `groupe` | varchar(255) NOT NULL | non | — |  |  |
| `statut` | varchar(255) NOT NULL | non | — |  | metadonnee catalogue |
| `ville` | varchar(255) NOT NULL | non | — |  |  |

## `statopac_vue_5`

Domaine probable : statistiques OPAC (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 2887579 (borne sup, pas effectif), instructions INSERT : 228, preuve : CREATE TABLE observe (bloc 550/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_ligne` | int(8) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `Infopage` | varchar(255) NOT NULL | non | — |  |  |

## `statopac_vues`

Domaine probable : statistiques OPAC (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 6 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 551/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_vue` | int(8) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `date_consolidation` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `nom_vue` | varchar(255) NOT NULL | non | — |  |  |
| `comment` | tinytext NOT NULL | non | — |  |  |
| `date_debut_log` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `date_fin_log` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |

## `statopac_vues_col`

Domaine probable : statistiques OPAC (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 35 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 552/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_col` | int(8) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `nom_col` | varchar(255) NOT NULL | non | — |  |  |
| `expression` | varchar(255) NOT NULL | non | — |  |  |
| `num_vue` | mediumint(8) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `ordre` | mediumint(8) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `filtre` | varchar(255) NOT NULL | non | — |  |  |
| `datatype` | varchar(10) NOT NULL | non | — |  |  |
| `maj_flag` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `sticks_sheets`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 553/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_sticks_sheet` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `sticks_sheet_label` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `sticks_sheet_data` | text NOT NULL | non | — |  |  |
| `sticks_sheet_order` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `storages`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 2 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 554/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_storage` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `storage_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `storage_class` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `storage_params` | text NOT NULL | non | — |  |  |

## `sub_collections`

Autorite : sous-collections editoriales.

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 1372 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 555/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `sub_coll_id` | mediumint(8) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `sub_coll_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `sub_coll_parent` | mediumint(9) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `sub_coll_issn` | varchar(12) NOT NULL DEFAULT '' | non | '' |  |  |
| `index_sub_coll` | text DEFAULT NULL | oui | NULL |  |  |
| `subcollection_web` | text NOT NULL | non | — |  |  |
| `subcollection_comment` | text NOT NULL | non | — |  |  |
| `authority_import_denied` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `subcollection_custom`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 556/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `idchamp` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI |  |
| `num_type` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `titre` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `type` | varchar(10) NOT NULL DEFAULT 'text' | non | 'text' |  |  |
| `datatype` | varchar(10) NOT NULL DEFAULT '' | non | '' |  |  |
| `options` | text DEFAULT NULL | oui | NULL |  |  |
| `multiple` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `obligatoire` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `ordre` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `search` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `export` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `filters` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `exclusion_obligatoire` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `pond` | int(11) NOT NULL DEFAULT 100 | non | 100 |  |  |
| `opac_sort` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `comment` | blob NOT NULL | non | — |  |  |
| `custom_classement` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |

## `subcollection_custom_dates`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 557/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `subcollection_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `subcollection_custom_origine` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `subcollection_custom_date_type` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `subcollection_custom_date_start` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `subcollection_custom_date_end` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `subcollection_custom_order` | int(11) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |

## `subcollection_custom_lists`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 558/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_subcollection_custom_list` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `subcollection_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `subcollection_custom_list_value` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `subcollection_custom_list_lib` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `ordre` | int(11) DEFAULT NULL | oui | NULL |  |  |

## `subcollection_custom_values`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 559/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `subcollection_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `subcollection_custom_origine` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `subcollection_custom_small_text` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `subcollection_custom_text` | text DEFAULT NULL | oui | NULL |  |  |
| `subcollection_custom_integer` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `subcollection_custom_date` | date DEFAULT NULL | oui | NULL |  | date |
| `subcollection_custom_float` | float DEFAULT NULL | oui | NULL |  |  |
| `subcollection_custom_order` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `subst_files`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 560/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_subst_file` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `subst_file_path` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `subst_file_filename` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `subst_file_data` | mediumtext NOT NULL | non | — |  |  |

## `suggestions`

Suggestions d'achat des lecteurs.

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 561/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_suggestion` | int(12) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `titre` | tinytext NOT NULL | non | — |  |  |
| `editeur` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `auteur` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `code` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | metadonnee catalogue |
| `prix` | float(8,2) unsigned NOT NULL DEFAULT 0.00 | non | 0.00 |  | montant |
| `commentaires` | text DEFAULT NULL | oui | NULL |  |  |
| `commentaires_gestion` | text DEFAULT NULL | oui | NULL |  |  |
| `statut` | int(3) unsigned NOT NULL DEFAULT 0 | non | 0 |  | metadonnee catalogue |
| `num_produit` | int(8) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_entite` | int(5) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `index_suggestion` | text NOT NULL | non | — |  |  |
| `nb` | int(5) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |
| `date_creation` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `date_decision` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `num_rubrique` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_fournisseur` | int(5) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_notice` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  | lien suppose -> notices.notice_id |
| `url_suggestion` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `num_categ` | int(12) NOT NULL DEFAULT 1 | non | 1 |  |  |
| `sugg_location` | smallint(5) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `sugg_source` | int(8) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `date_publication` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | date |
| `notice_unimarc` | blob NOT NULL | non | — |  |  |

## `suggestions_categ`

Domaine probable : suggestions d'acquisition (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 2 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 562/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_categ` | int(12) NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `libelle_categ` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |

## `suggestions_origine`

Domaine probable : suggestions d'acquisition (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 563/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `origine` | varchar(100) NOT NULL DEFAULT '' | non | '' | PK |  |
| `num_suggestion` | int(12) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `type_origine` | int(3) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `date_suggestion` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |

## `suggestions_source`

Domaine probable : suggestions d'acquisition (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 564/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_source` | int(8) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `libelle_source` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |

## `sur_location`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 565/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `surloc_id` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `surloc_libelle` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `surloc_pic` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `surloc_visible_opac` | tinyint(1) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |
| `surloc_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `surloc_adr1` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `surloc_adr2` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `surloc_cp` | varchar(15) NOT NULL DEFAULT '' | non | '' |  |  |
| `surloc_town` | varchar(100) NOT NULL DEFAULT '' | non | '' |  |  |
| `surloc_state` | varchar(100) NOT NULL DEFAULT '' | non | '' |  |  |
| `surloc_country` | varchar(100) NOT NULL DEFAULT '' | non | '' |  |  |
| `surloc_phone` | varchar(100) NOT NULL DEFAULT '' | non | '' |  |  |
| `surloc_email` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | donnee perso RGPD |
| `surloc_website` | varchar(100) NOT NULL DEFAULT '' | non | '' |  |  |
| `surloc_logo` | varchar(100) NOT NULL DEFAULT '' | non | '' |  |  |
| `surloc_comment` | text NOT NULL | non | — |  |  |
| `surloc_num_infopage` | int(6) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `surloc_css_style` | varchar(100) NOT NULL DEFAULT '' | non | '' |  |  |

## `tabs`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 566/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_tab` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `tab_module` | varchar(50) NOT NULL DEFAULT '' | non | '' | UNIQUE |  |
| `tab_categ` | varchar(50) NOT NULL DEFAULT '' | non | '' | UNIQUE |  |
| `tab_sub` | varchar(50) NOT NULL DEFAULT '' | non | '' | UNIQUE |  |
| `tab_visible` | int(1) NOT NULL DEFAULT 1 | non | 1 |  |  |
| `tab_autorisations` | mediumtext DEFAULT NULL | oui | NULL |  |  |
| `tab_autorisations_all` | int(1) NOT NULL DEFAULT 1 | non | 1 |  |  |
| `tab_shortcut` | char(1) NOT NULL DEFAULT '' | non | '' |  |  |
| `tab_order` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `taches`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 8993 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 567/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_tache` | int(11) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `num_planificateur` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `start_at` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE |  |
| `end_at` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE |  |
| `status` | varchar(128) DEFAULT NULL | oui | NULL |  |  |
| `msg_statut` | text DEFAULT NULL | oui | NULL |  |  |
| `commande` | int(8) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `next_state` | int(8) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `msg_commande` | blob DEFAULT NULL | oui | NULL |  |  |
| `indicat_progress` | float(5,2) NOT NULL DEFAULT 0.00 | non | 0.00 |  |  |
| `rapport` | mediumtext DEFAULT NULL | oui | NULL |  |  |
| `id_process` | int(8) DEFAULT NULL | oui | NULL |  | identifiant |
| `host_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `alive_at` | timestamp NULL DEFAULT NULL | oui | NULL |  |  |

## `taches_docnum`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 568/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_tache_docnum` | int(11) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `tache_docnum_nomfichier` | varchar(255) NOT NULL | non | — |  |  |
| `tache_docnum_mimetype` | varchar(255) NOT NULL | non | — |  |  |
| `tache_docnum_data` | mediumblob NOT NULL | non | — |  |  |
| `tache_docnum_extfichier` | varchar(20) DEFAULT NULL | oui | NULL |  |  |
| `tache_docnum_repertoire` | int(8) DEFAULT NULL | oui | NULL |  |  |
| `tache_docnum_path` | text NOT NULL | non | — |  |  |
| `num_tache` | int(11) NOT NULL | non | — |  |  |

## `taches_type`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 569/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_type_tache` | int(11) unsigned NOT NULL | non | — | PK | identifiant |
| `parameters` | text NOT NULL | non | — |  |  |
| `timeout` | int(11) NOT NULL DEFAULT 5 | non | 5 |  |  |
| `histo_day` | int(11) NOT NULL DEFAULT 7 | non | 7 |  |  |
| `histo_number` | int(11) NOT NULL DEFAULT 3 | non | 3 |  |  |
| `restart_on_failure` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `alert_mail_on_failure` | varchar(255) DEFAULT '' | oui | '' |  | donnee perso RGPD |

## `tags`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 570/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_tag` | mediumint(8) NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `libelle` | varchar(200) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `num_notice` | mediumint(8) NOT NULL DEFAULT 0 | non | 0 |  | lien suppose -> notices.notice_id |
| `user_code` | varchar(50) NOT NULL DEFAULT '' | non | '' |  |  |
| `dateajout` | timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp() | non | current_timestamp() |  |  |

## `thesaurus`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 3 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 571/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_thesaurus` | int(3) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `libelle_thesaurus` | varchar(255) NOT NULL DEFAULT '' | non | '' | UNIQUE | libelle |
| `langue_defaut` | varchar(5) NOT NULL DEFAULT 'fr_FR' | non | 'fr_FR' |  |  |
| `active` | char(1) NOT NULL DEFAULT '1' | non | '1' |  |  |
| `opac_active` | char(1) NOT NULL DEFAULT '1' | non | '1' |  |  |
| `num_noeud_racine` | int(9) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `thesaurus_order` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `thresholds`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 572/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_threshold` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `threshold_label` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `threshold_amount` | float NOT NULL DEFAULT 0 | non | 0 |  |  |
| `threshold_amount_tax_included` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `threshold_footer` | text NOT NULL | non | — |  |  |
| `threshold_num_entity` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `thumbnail_sources`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 2 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 573/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `class` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `settings` | mediumblob NOT NULL | non | — |  |  |
| `active` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `thumbnail_sources_entities`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 5 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 574/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `source_class` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `pivot_class` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `type` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `pivot` | longtext DEFAULT NULL | oui | NULL |  |  |
| `ranking` | int(10) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `titres_uniformes`

Autorite : titres uniformes (musique surtout).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 19 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 575/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `tu_id` | int(9) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `tu_name` | text DEFAULT NULL | oui | NULL |  | libelle |
| `tu_tonalite` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `tu_comment` | text NOT NULL | non | — |  |  |
| `index_tu` | text NOT NULL | non | — |  |  |
| `tu_import_denied` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `tu_num_author` | bigint(11) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `tu_forme` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `tu_date` | varchar(50) NOT NULL DEFAULT '' | non | '' |  | date |
| `tu_date_date` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `tu_sujet` | text NOT NULL | non | — |  |  |
| `tu_lieu` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `tu_histoire` | text DEFAULT NULL | oui | NULL |  |  |
| `tu_caracteristique` | text DEFAULT NULL | oui | NULL |  |  |
| `tu_public` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `tu_contexte` | text DEFAULT NULL | oui | NULL |  |  |
| `tu_coordonnees` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `tu_equinoxe` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `tu_completude` | int(2) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `tu_tonalite_marclist` | varchar(5) NOT NULL DEFAULT '' | non | '' |  |  |
| `tu_forme_marclist` | varchar(5) NOT NULL DEFAULT '' | non | '' |  |  |
| `tu_oeuvre_nature` | varchar(3) NOT NULL DEFAULT 'a' | non | 'a' |  |  |
| `tu_oeuvre_type` | varchar(3) NOT NULL DEFAULT 'a' | non | 'a' |  |  |
| `tu_oeuvre_nature_nature` | varchar(255) NOT NULL DEFAULT 'original' | non | 'original' |  |  |

## `transacash`

Passages en caisse (encaisse, rendu).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 332 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 576/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `transacash_id` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `transacash_empr_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `transacash_desk_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `transacash_user_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `transacash_date` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `transacash_sold` | float NOT NULL DEFAULT 0 | non | 0 |  |  |
| `transacash_collected` | float NOT NULL DEFAULT 0 | non | 0 |  |  |
| `transacash_rendering` | float NOT NULL DEFAULT 0 | non | 0 |  |  |

## `transaction_compte_payments`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 577/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id` | int(11) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `transaction_num` | int(11) NOT NULL | non | — |  |  |
| `compte_num` | int(11) NOT NULL | non | — |  |  |
| `amount` | int(11) NOT NULL | non | — |  |  |

## `transaction_payment_methods`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 578/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `transaction_payment_method_id` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `transaction_payment_method_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |

## `transaction_payments`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 579/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id` | int(11) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `order_number` | int(11) NOT NULL | non | — | UNIQUE |  |
| `payment_date` | datetime NOT NULL | non | — |  | date |
| `payment_status` | int(1) NOT NULL | non | — |  |  |
| `payment_organization_status` | varchar(10) DEFAULT NULL | oui | NULL |  |  |
| `num_user` | int(11) NOT NULL | non | — |  |  |
| `num_organization` | int(1) NOT NULL | non | — |  |  |

## `transactions`

Transactions sur comptes (montant, sens, caisse).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 817 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 580/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_transaction` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `compte_id` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  | identifiant |
| `user_id` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  | identifiant |
| `user_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `machine` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `date_enrgt` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `date_prevue` | date DEFAULT NULL | oui | NULL |  | date |
| `date_effective` | date DEFAULT NULL | oui | NULL |  | date |
| `montant` | decimal(16,2) NOT NULL DEFAULT 0.00 | non | 0.00 |  | montant |
| `sens` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `realisee` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `commentaire` | text DEFAULT NULL | oui | NULL |  |  |
| `encaissement` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `transactype_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `cashdesk_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `transacash_num` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `transaction_payment_method_num` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `transactype`

Referentiel : types de transactions tarifees.

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 581/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `transactype_id` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `transactype_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `transactype_quick_allowed` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `transactype_unit_price` | float NOT NULL DEFAULT 0 | non | 0 |  |  |

## `transferts`

Transferts d'exemplaires entre sites (constats).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 39043 (borne sup, pas effectif), instructions INSERT : 5, preuve : CREATE TABLE observe (bloc 582/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_transfert` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `num_notice` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  | lien suppose -> notices.notice_id |
| `num_bulletin` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `date_creation` | date NOT NULL | non | — |  | date |
| `type_transfert` | int(5) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `etat_transfert` | tinyint(3) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `origine` | int(5) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `origine_comp` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `source` | smallint(5) unsigned DEFAULT NULL | oui | NULL |  |  |
| `destinations` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `date_retour` | date DEFAULT NULL | oui | NULL |  | date |
| `motif` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `transfert_ask_user_num` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `transfert_send_user_num` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `transfert_ask_date` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |

## `transferts_demande`

Demandes de transfert / navette entre sites.

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 39362 (borne sup, pas effectif), instructions INSERT : 4, preuve : CREATE TABLE observe (bloc 583/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_transfert_demande` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `num_transfert` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `date_creation` | date NOT NULL | non | — |  | date |
| `sens_transfert` | tinyint(3) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_location_source` | smallint(5) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_location_dest` | smallint(5) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_expl` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `etat_demande` | tinyint(3) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `date_visualisee` | date DEFAULT NULL | oui | NULL |  | date |
| `date_envoyee` | date DEFAULT NULL | oui | NULL |  | date |
| `date_reception` | date DEFAULT NULL | oui | NULL |  | date |
| `motif_refus` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `statut_origine` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `section_origine` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `resa_trans` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  | champ reservation |
| `resa_arc_trans` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  | champ reservation |

## `transferts_source`

Domaine probable : navette / transferts reseau (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 584/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `trans_source_numexpl` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `trans_source_numloc` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `translation`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 585/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `trans_table` | varchar(100) NOT NULL DEFAULT '' | non | '' | PK |  |
| `trans_field` | varchar(100) NOT NULL DEFAULT '' | non | '' | PK |  |
| `trans_lang` | varchar(5) NOT NULL DEFAULT '' | non | '' | PK |  |
| `trans_num` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `trans_small_text` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `trans_text` | text DEFAULT NULL | oui | NULL |  |  |

## `tris`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 9 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 586/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_tri` | int(4) NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `tri_par` | varchar(100) NOT NULL DEFAULT '' | non | '' |  |  |
| `nom_tri` | varchar(100) NOT NULL DEFAULT '' | non | '' |  |  |
| `tri_reference` | varchar(40) NOT NULL DEFAULT 'notices' | non | 'notices' |  |  |

## `tu_custom`

Domaine probable : titres uniformes (musique) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 587/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `idchamp` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI |  |
| `num_type` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `titre` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `type` | varchar(10) NOT NULL DEFAULT 'text' | non | 'text' |  |  |
| `datatype` | varchar(10) NOT NULL DEFAULT '' | non | '' |  |  |
| `options` | text DEFAULT NULL | oui | NULL |  |  |
| `multiple` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `obligatoire` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `ordre` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `search` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `export` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `filters` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `exclusion_obligatoire` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `pond` | int(11) NOT NULL DEFAULT 100 | non | 100 |  |  |
| `opac_sort` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `comment` | blob NOT NULL | non | — |  |  |
| `custom_classement` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |

## `tu_custom_dates`

Domaine probable : titres uniformes (musique) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 588/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `tu_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `tu_custom_origine` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `tu_custom_date_type` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `tu_custom_date_start` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `tu_custom_date_end` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `tu_custom_order` | int(11) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |

## `tu_custom_lists`

Domaine probable : titres uniformes (musique) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 589/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_tu_custom_list` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `tu_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `tu_custom_list_value` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `tu_custom_list_lib` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `ordre` | int(11) DEFAULT NULL | oui | NULL |  |  |

## `tu_custom_values`

Domaine probable : titres uniformes (musique) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 590/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `tu_custom_champ` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `tu_custom_origine` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `tu_custom_small_text` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `tu_custom_text` | text DEFAULT NULL | oui | NULL |  |  |
| `tu_custom_integer` | int(11) DEFAULT NULL | oui | NULL |  |  |
| `tu_custom_date` | date DEFAULT NULL | oui | NULL |  | date |
| `tu_custom_float` | float DEFAULT NULL | oui | NULL |  |  |
| `tu_custom_order` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `tu_distrib`

Domaine probable : titres uniformes (musique) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 591/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `distrib_num_tu` | int(9) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `distrib_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `distrib_ordre` | smallint(5) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |

## `tu_oeuvres_events`

Domaine probable : titres uniformes (musique) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 592/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `oeuvre_event_tu_num` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `oeuvre_event_authperso_authority_num` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `oeuvre_event_order` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `tu_oeuvres_links`

Domaine probable : titres uniformes (musique) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 593/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `oeuvre_link_from` | int(11) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `oeuvre_link_to` | int(11) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `oeuvre_link_type` | varchar(3) NOT NULL DEFAULT '' | non | '' | PK |  |
| `oeuvre_link_expression` | int(11) NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `oeuvre_link_other_link` | int(11) NOT NULL DEFAULT 1 | non | 1 | PK |  |
| `oeuvre_link_order` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `tu_ref`

Domaine probable : titres uniformes (musique) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 594/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `ref_num_tu` | int(9) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `ref_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `ref_ordre` | smallint(5) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |

## `tu_subdiv`

Domaine probable : titres uniformes (musique) (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 595/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `subdiv_num_tu` | int(9) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `subdiv_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `subdiv_ordre` | smallint(5) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |

## `tva_achats`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 596/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_tva` | int(8) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `libelle` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `taux_tva` | float(4,2) unsigned NOT NULL DEFAULT 0.00 | non | 0.00 |  |  |
| `num_cp_compta` | varchar(25) NOT NULL DEFAULT '0' | non | '0' |  |  |

## `type_abts`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 6 (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 597/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_type_abt` | int(5) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `type_abt_libelle` | varchar(255) DEFAULT NULL | oui | NULL |  | libelle |
| `prepay` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `prepay_deflt_mnt` | decimal(16,2) NOT NULL DEFAULT 0.00 | non | 0.00 |  |  |
| `tarif` | decimal(16,2) NOT NULL DEFAULT 0.00 | non | 0.00 |  |  |
| `commentaire` | text NOT NULL | non | — |  |  |
| `caution` | decimal(16,2) NOT NULL DEFAULT 0.00 | non | 0.00 |  |  |
| `localisations` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |

## `type_comptes`

Referentiel : types de comptes financiers.

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 598/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_type_compte` | int(8) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `libelle` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `type_acces` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `acces_id` | text NOT NULL | non | — |  | identifiant |

## `types_produits`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 599/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_produit` | int(8) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `libelle` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `num_cp_compta` | varchar(25) NOT NULL DEFAULT '0' | non | '0' |  |  |
| `num_tva_achat` | varchar(25) NOT NULL DEFAULT '0' | non | '0' |  |  |

## `upload_repertoire`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 4 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 600/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `repertoire_id` | int(8) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `repertoire_nom` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `repertoire_url` | text NOT NULL | non | — |  |  |
| `repertoire_path` | text NOT NULL | non | — |  |  |
| `repertoire_navigation` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `repertoire_hachage` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `repertoire_subfolder` | int(8) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `repertoire_utf8` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `users`

Comptes professionnels (bibliothecaires).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 34 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 601/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `userid` | int(5) NOT NULL AUTO_INCREMENT | non | — | PK,AI |  |
| `create_dt` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE |  |
| `last_updated_dt` | date NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE |  |
| `username` | varchar(100) NOT NULL DEFAULT '' | non | '' |  |  |
| `pwd` | varchar(50) NOT NULL DEFAULT '' | non | '' |  |  |
| `user_digest` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | SECRET : ne pas reprendre (reinitialiser cote cible) |
| `nom` | varchar(30) NOT NULL DEFAULT '' | non | '' |  |  |
| `prenom` | varchar(30) DEFAULT NULL | oui | NULL |  |  |
| `rights` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `user_lang` | varchar(5) NOT NULL DEFAULT 'fr_FR' | non | 'fr_FR' |  |  |
| `nb_per_page_search` | int(10) unsigned NOT NULL DEFAULT 4 | non | 4 |  |  |
| `nb_per_page_select` | int(10) unsigned NOT NULL DEFAULT 10 | non | 10 |  |  |
| `nb_per_page_gestion` | int(10) unsigned NOT NULL DEFAULT 20 | non | 20 |  |  |
| `param_popup_ticket` | smallint(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `param_sounds` | smallint(1) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |
| `param_rfid_activate` | int(1) NOT NULL DEFAULT 1 | non | 1 |  |  |
| `param_chat_activate` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `param_licence` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `deflt_notice_statut` | int(6) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |
| `deflt_notice_statut_analysis` | int(6) unsigned DEFAULT 0 | oui | 0 |  |  |
| `deflt_integration_notice_statut` | int(6) NOT NULL DEFAULT 1 | non | 1 |  |  |
| `xmlta_indexation_lang` | varchar(10) NOT NULL DEFAULT '' | non | '' |  |  |
| `deflt_docs_type` | int(6) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |
| `deflt_serials_docs_type` | int(6) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |
| `deflt_lenders` | int(6) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `deflt_styles` | varchar(20) NOT NULL DEFAULT 'default' | non | 'default' |  |  |
| `deflt_docs_statut` | int(6) unsigned DEFAULT 0 | oui | 0 |  |  |
| `deflt_docs_codestat` | int(6) unsigned DEFAULT 0 | oui | 0 |  |  |
| `value_deflt_lang` | varchar(20) DEFAULT 'fre' | oui | 'fre' |  |  |
| `value_deflt_fonction` | varchar(20) DEFAULT '070' | oui | '070' |  |  |
| `value_deflt_relation` | varchar(20) NOT NULL DEFAULT 'a' | non | 'a' |  |  |
| `value_deflt_relation_serial` | varchar(20) NOT NULL DEFAULT '' | non | '' |  |  |
| `value_deflt_relation_bulletin` | varchar(20) NOT NULL DEFAULT '' | non | '' |  |  |
| `value_deflt_relation_analysis` | varchar(20) NOT NULL DEFAULT '' | non | '' |  |  |
| `deflt_docs_location` | int(6) unsigned DEFAULT 0 | oui | 0 |  |  |
| `deflt_collstate_location` | int(6) unsigned DEFAULT 0 | oui | 0 |  |  |
| `deflt_bulletinage_location` | int(6) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `deflt_resas_location` | int(6) unsigned DEFAULT 0 | oui | 0 |  |  |
| `deflt_docs_section` | int(6) unsigned DEFAULT 0 | oui | 0 |  |  |
| `value_deflt_module` | varchar(30) DEFAULT 'circu' | oui | 'circu' |  |  |
| `user_email` | varchar(255) DEFAULT '' | oui | '' |  | donnee perso RGPD |
| `user_alert_resamail` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  | donnee perso RGPD |
| `user_alert_contribmail` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  | donnee perso RGPD |
| `user_alert_demandesmail` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  | donnee perso RGPD |
| `user_alert_subscribemail` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  | donnee perso RGPD |
| `user_alert_serialcircmail` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  | donnee perso RGPD |
| `deflt2docs_location` | int(6) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `deflt_empr_statut` | bigint(20) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |
| `deflt_empr_categ` | int(10) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |
| `deflt_empr_codestat` | int(10) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |
| `deflt_thesaurus` | int(3) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |
| `deflt_concept_scheme` | int(3) NOT NULL DEFAULT -1 | non | -1 |  |  |
| `deflt_import_thesaurus` | int(11) NOT NULL DEFAULT 1 | non | 1 |  |  |
| `value_prefix_cote` | tinyblob NOT NULL | non | — |  |  |
| `xmlta_doctype` | char(2) NOT NULL DEFAULT 'a' | non | 'a' |  |  |
| `xmlta_doctype_serial` | varchar(2) NOT NULL DEFAULT '' | non | '' |  |  |
| `xmlta_doctype_bulletin` | varchar(2) NOT NULL DEFAULT '' | non | '' |  |  |
| `xmlta_doctype_analysis` | varchar(2) NOT NULL DEFAULT '' | non | '' |  |  |
| `speci_coordonnees_etab` | mediumtext NOT NULL | non | — |  |  |
| `value_email_bcc` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | donnee perso RGPD |
| `value_deflt_antivol` | varchar(50) NOT NULL DEFAULT '0' | non | '0' |  |  |
| `explr_invisible` | text DEFAULT NULL | oui | NULL |  |  |
| `explr_visible_mod` | text DEFAULT NULL | oui | NULL |  |  |
| `explr_visible_unmod` | text DEFAULT NULL | oui | NULL |  |  |
| `deflt3bibli` | int(5) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `deflt3exercice` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `deflt3rubrique` | int(8) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `deflt3type_produit` | int(8) unsigned DEFAULT 0 | oui | 0 |  |  |
| `deflt3dev_statut` | int(3) NOT NULL DEFAULT -1 | non | -1 |  |  |
| `deflt3cde_statut` | int(3) NOT NULL DEFAULT -1 | non | -1 |  |  |
| `deflt3liv_statut` | int(3) NOT NULL DEFAULT -1 | non | -1 |  |  |
| `deflt3fac_statut` | int(3) NOT NULL DEFAULT -1 | non | -1 |  |  |
| `deflt3sug_statut` | int(3) NOT NULL DEFAULT -1 | non | -1 |  |  |
| `environnement` | mediumblob NOT NULL | non | — |  |  |
| `param_allloc` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `grp_num` | int(10) unsigned DEFAULT 0 | oui | 0 |  |  |
| `deflt_arch_statut` | int(6) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `deflt_arch_emplacement` | int(6) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `deflt_arch_type` | int(6) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `deflt_upload_repertoire` | int(8) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `deflt_short_loan_activate` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `deflt3lgstatdev` | int(3) NOT NULL DEFAULT 1 | non | 1 |  |  |
| `deflt3lgstatcde` | int(3) NOT NULL DEFAULT 1 | non | 1 |  |  |
| `deflt3receptsugstat` | int(3) NOT NULL DEFAULT 32 | non | 32 |  |  |
| `deflt_cashdesk` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `user_alert_suggmail` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  | donnee perso RGPD |
| `deflt_explnum_statut` | int(6) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |
| `deflt_explnum_location` | int(6) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |
| `deflt_explnum_lenders` | int(6) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |
| `deflt_notice_replace_keep_categories` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `deflt_notice_is_new` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `deflt_agnostic_warehouse` | int(6) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `deflt_cms_article_statut` | int(6) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `deflt_cms_article_type` | int(6) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `deflt_cms_section_type` | int(6) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `deflt_catalog_expanded_caddies` | int(1) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |
| `deflt_scan_request_status` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `xmlta_doctype_scan_request_folder_record` | varchar(2) NOT NULL DEFAULT 'a' | non | 'a' |  |  |
| `deflt_camera_empr` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `deflt_notice_replace_links` | int(1) unsigned DEFAULT 0 | oui | 0 |  |  |
| `deflt_printer` | int(3) unsigned DEFAULT 0 | oui | 0 |  |  |
| `deflt_opac_visible_bulletinage` | int(11) NOT NULL DEFAULT 1 | non | 1 |  |  |
| `deflt_scan_request_explnum_status` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `deflt_type_abts` | int(5) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `deflt_docwatch_watch_filter_deleted` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `deflt_pclassement` | int(3) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |
| `deflt_associated_campaign` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `deflt_bypass_isbn_page` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `deflt_animation_calendar` | int(1) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |
| `deflt_notice_catalog_categories_auto` | int(1) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |
| `deflt_animation_waiting_list` | tinyint(3) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `deflt_animation_automatic_registration` | tinyint(3) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `deflt_animation_communication_type` | tinyint(3) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |
| `deflt_animation_unique_registration` | tinyint(3) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `user_alert_animation_mail` | int(1) unsigned NOT NULL DEFAULT 0 | non | 0 |  | donnee perso RGPD |
| `user_email_recipient` | varchar(255) DEFAULT '' | oui | '' |  | donnee perso RGPD |
| `deflt_dsi_diffusion_default_status` | tinyint(3) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |
| `deflt_dsi_product_default_status` | tinyint(3) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |
| `mfa_secret_code` | varchar(255) DEFAULT NULL | oui | NULL |  | SECRET : ne pas reprendre (reinitialiser cote cible) |
| `mfa_favorite` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `deflt_import_lenders` | tinyint(3) unsigned NOT NULL DEFAULT 1 | non | 1 |  |  |
| `param_notify_login_failed` | tinyint(3) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `deflt_dashboard_selected` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `deflt3recept_notice_statut` | int(3) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `deflt_animation_location` | tinyint(3) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |

## `users_groups`

Domaine probable : comptes professionnels / droits (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 2 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 602/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `grp_id` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `grp_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |

## `users_roles`

Domaine probable : comptes professionnels / droits (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 603/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id` | int(11) NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `comment` | text NOT NULL | non | — |  |  |

## `users_roles_members`

Domaine probable : comptes professionnels / droits (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 604/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id` | int(11) NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `type_member` | varchar(50) NOT NULL DEFAULT '' | non | '' |  |  |
| `num_member` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_role` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `users_roles_rights`

Domaine probable : comptes professionnels / droits (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 605/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id` | int(11) NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `component` | varchar(50) NOT NULL DEFAULT '' | non | '' |  |  |
| `module` | varchar(50) NOT NULL DEFAULT '' | non | '' |  |  |
| `categ` | varchar(50) NOT NULL DEFAULT '' | non | '' |  |  |
| `sub` | varchar(50) NOT NULL DEFAULT '' | non | '' |  |  |
| `url_extra` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `action` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `visible` | int(1) NOT NULL DEFAULT 1 | non | 1 |  |  |
| `privilege` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `log` | int(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `num_role` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `vedette`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 606/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_vedette` | int(11) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `label` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `grammar` | varchar(255) NOT NULL DEFAULT 'rameau' | non | 'rameau' |  |  |

## `vedette_grammars_by_entity`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 607/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `entity_type` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `grammar` | varchar(255) NOT NULL DEFAULT '' | non | '' | PK |  |

## `vedette_link`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 608/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_vedette` | int(10) unsigned NOT NULL | non | — | PK |  |
| `num_object` | int(10) unsigned NOT NULL | non | — | PK |  |
| `type_object` | int(10) unsigned NOT NULL | non | — | PK |  |

## `vedette_object`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 609/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `object_type` | int(3) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `object_id` | int(11) unsigned NOT NULL DEFAULT 0 | non | 0 | PK | identifiant |
| `num_vedette` | int(11) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `subdivision` | varchar(50) NOT NULL DEFAULT '' | non | '' | PK |  |
| `position` | int(3) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `num_available_field` | int(11) NOT NULL DEFAULT 0 | non | 0 |  |  |

## `vedette_schemes_by_entity`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 610/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `entity_type` | int(10) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `scheme` | int(11) NOT NULL DEFAULT 0 | non | 0 | PK |  |

## `visionneuse_params`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 611/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `visionneuse_params_id` | int(11) NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `visionneuse_params_class` | varchar(255) NOT NULL DEFAULT '' | non | '' | UNIQUE |  |
| `visionneuse_params_parameters` | text NOT NULL | non | — |  |  |

## `visits_statistics`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 612/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `visits_statistics_id` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `visits_statistics_date` | datetime NOT NULL DEFAULT '[masque: voir dump local]' | non | '[masque: voir dump local]' | DEFAUT MASQUE | date |
| `visits_statistics_location` | smallint(5) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `visits_statistics_type` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |

## `voir_aussi`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 613/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `num_noeud_orig` | int(9) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `num_noeud_dest` | int(9) unsigned NOT NULL DEFAULT 0 | non | 0 | PK |  |
| `langue` | varchar(5) NOT NULL DEFAULT '' | non | '' | PK |  |
| `comment_voir_aussi` | text NOT NULL | non | — |  |  |

## `widget`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 0, preuve : CREATE TABLE observe (bloc 614/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_widget` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `widget_name` | varchar(255) NOT NULL DEFAULT '' | non | '' |  | libelle |
| `widget_editable` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `widget_type` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `num_user` | int(5) unsigned NOT NULL DEFAULT 0 | non | 0 |  |  |
| `widget_shareable` | tinyint(1) NOT NULL DEFAULT 0 | non | 0 |  |  |
| `widget_settings` | mediumblob NOT NULL | non | — |  |  |

## `words`

Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 420133 (borne sup, pas effectif), instructions INSERT : 18, preuve : CREATE TABLE observe (bloc 615/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `id_word` | int(10) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `word` | varchar(255) NOT NULL DEFAULT '' | non | '' | UNIQUE |  |
| `lang` | varchar(10) NOT NULL DEFAULT '' | non | '' | UNIQUE |  |
| `double_metaphone` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |
| `stem` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |

## `z_attr`

Domaine probable : protocole Z39.50 / reservoirs externes (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max None (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 616/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `attr_bib_id` | int(6) unsigned NOT NULL DEFAULT 0 | non | 0 | PK | identifiant |
| `attr_libelle` | varchar(250) NOT NULL DEFAULT '' | non | '' | PK | libelle |
| `attr_attr` | varchar(250) DEFAULT NULL | oui | NULL |  |  |

## `z_bib`

Domaine probable : protocole Z39.50 / reservoirs externes (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 22 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 617/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `bib_id` | int(6) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `bib_nom` | varchar(250) DEFAULT NULL | oui | NULL |  |  |
| `search_type` | varchar(20) DEFAULT NULL | oui | NULL |  |  |
| `url` | varchar(250) DEFAULT NULL | oui | NULL |  |  |
| `port` | varchar(6) DEFAULT NULL | oui | NULL |  |  |
| `base` | varchar(250) DEFAULT NULL | oui | NULL |  |  |
| `format` | varchar(250) DEFAULT NULL | oui | NULL |  |  |
| `auth_user` | varchar(250) NOT NULL DEFAULT '' | non | '' |  |  |
| `auth_pass` | varchar(250) NOT NULL DEFAULT '' | non | '' |  |  |
| `sutrs_lang` | varchar(10) NOT NULL DEFAULT '' | non | '' |  |  |
| `fichier_func` | varchar(255) NOT NULL DEFAULT '' | non | '' |  |  |

## `z_notices`

Domaine probable : protocole Z39.50 / reservoirs externes (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 27757 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 618/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `znotices_id` | int(11) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `znotices_query_id` | int(11) DEFAULT NULL | oui | NULL |  | identifiant |
| `znotices_bib_id` | int(6) unsigned DEFAULT 0 | oui | 0 |  | identifiant |
| `isbd` | text DEFAULT NULL | oui | NULL |  |  |
| `isbn` | varchar(250) DEFAULT NULL | oui | NULL |  | metadonnee catalogue |
| `titre` | varchar(250) DEFAULT NULL | oui | NULL |  |  |
| `auteur` | varchar(250) DEFAULT NULL | oui | NULL |  |  |
| `z_marc` | longblob NOT NULL | non | — |  |  |

## `z_query`

Domaine probable : protocole Z39.50 / reservoirs externes (infere du prefixe, a confirmer).

Moteur MyISAM, charset utf8mb3, AUTO_INCREMENT max 8967 (borne sup, pas effectif), instructions INSERT : 1, preuve : CREATE TABLE observe (bloc 619/619) + DROP TABLE IF EXISTS present ; aucune FK declaree.

| colonne | type exact | NULL | defaut | cles | role |
|---|---|---|---|---|---|
| `zquery_id` | int(11) unsigned NOT NULL AUTO_INCREMENT | non | — | PK,AI | identifiant |
| `search_attr` | varchar(255) DEFAULT NULL | oui | NULL |  |  |
| `zquery_date` | timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp() | non | current_timestamp() |  | date |
