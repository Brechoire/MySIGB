# PMB_DOMAINES — perimetre et questions

Perimetre du clone : catalogue, adherents (dont ~10 comptes pro type collectivites), prets en cours + historique complet, retards, comptes/finance. Annexes (CMS, anim, connecteurs, ontologies) hors perimetre a priori.

## Catalogue
- `notices` : Notice bibliographique (livre, periodique, partition...). Coeur du catalogue. (INSERT: 107)
- `exemplaires` : Exemplaire physique rattache a une notice (ou un bulletin). Porte cote, section, statut, localisation, CB. (INSERT: 15)
- `bulletins` : Bulletin de periodique (exemplaire + depouillement d'articles). (INSERT: 1)
- `authors` : Autorite : auteurs (personnes / collectivites / congres). (INSERT: 5)
- `responsability` : Liaison notices <-> auteurs + fonction et ordre. (INSERT: 5)
- `publishers` : Autorite : editeurs. (INSERT: 1)
- `collections` : Autorite : collections editoriales. (INSERT: 1)
- `sub_collections` : Autorite : sous-collections editoriales. (INSERT: 1)
- `series` : Autorite : series. (INSERT: 1)
- `titres_uniformes` : Autorite : titres uniformes (musique surtout). (INSERT: 1)
- `categories` : Autorite : categories matiere du thesaurus. (INSERT: 2)
- `notices_categories` : Liaison notices <-> categories matiere. (INSERT: 1)
- `notices_relations` : Liaisons entre notices (autres editions, suites...). (INSERT: 1)
- `analysis` : Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer). (INSERT: 1)

## Adherents
- `empr` : Fiche lecteur (donnees perso RGPD). Futur modele Adherent. (INSERT: 2)
- `empr_categ` : Referentiel : categories d'adherents (voir libelles ci-dessous). (INSERT: 1)
- `empr_codestat` : Referentiel : code statistique adherent. (INSERT: 1)
- `empr_statut` : Referentiel : statut de fiche (Actif / Interdit). (INSERT: 1)
- `empr_groupe` : Liaison adherent <-> groupe (familles, collectivites). (INSERT: 1)
- `empr_custom` : Domaine probable : adherents / lecteurs (infere du prefixe, a confirmer). (INSERT: 1)
- `empr_custom_dates` : Domaine probable : adherents / lecteurs (infere du prefixe, a confirmer). (INSERT: 0)
- `empr_custom_lists` : Domaine probable : adherents / lecteurs (infere du prefixe, a confirmer). (INSERT: 1)
- `empr_custom_values` : Domaine probable : adherents / lecteurs (infere du prefixe, a confirmer). (INSERT: 1)

## Circulation
- `pret` : Prets en cours (cle = exemplaire). Retard si pret_retour < aujourd'hui. (INSERT: 1)
- `pret_archive` : Historique des prets (denormalise arc_*). Volume le plus gros. (INSERT: 112)
- `resa` : Reservations en cours. (INSERT: 1)
- `resa_archive` : Historique des reservations. (INSERT: 4)
- `transferts` : Transferts d'exemplaires entre sites (constats). (INSERT: 5)
- `transferts_demande` : Demandes de transfert / navette entre sites. (INSERT: 4)
- `quotas` : Quotas de pret par categorie/type. (INSERT: 1)
- `serialcirc` : Domaine probable : circulation des periodiques (infere du prefixe, a confirmer). (INSERT: 0)
- `serialcirc_copy` : Domaine probable : circulation des periodiques (infere du prefixe, a confirmer). (INSERT: 0)

## Retards
- `pret` : Prets en cours (cle = exemplaire). Retard si pret_retour < aujourd'hui. (INSERT: 1)
- `log_retard` : Journal des passages de relance. (INSERT: 1)
- `cache_amendes` : Cache calcule des amendes par adherent. (INSERT: 1)
- `recouvrements` : Recouvrements (perdus, reclamations). (INSERT: 1)

## Comptes/Finance
- `comptes` : Comptes adherents (~2 par lecteur : types 1/2, solde, prepaye). (INSERT: 1)
- `type_comptes` : Referentiel : types de comptes financiers. (INSERT: 0)
- `transactions` : Transactions sur comptes (montant, sens, caisse). (INSERT: 1)
- `transacash` : Passages en caisse (encaisse, rendu). (INSERT: 1)
- `transactype` : Referentiel : types de transactions tarifees. (INSERT: 0)
- `frais` : Frais annexes (inscription, reproduction...). (INSERT: 0)
- `paiements` : Referentiel : modes de paiement. (INSERT: 0)
- `rent_accounts` : Domaine probable : locations (comptes, facturation) (infere du prefixe, a confirmer). (INSERT: 0)
- `rent_invoices` : Domaine probable : locations (comptes, facturation) (infere du prefixe, a confirmer). (INSERT: 0)

## Referentiels
- `docs_location` : Referentiel : sites du reseau (12). (INSERT: 1)
- `docs_section` : Referentiel : sections internes. (INSERT: 1)
- `docs_statut` : Referentiel : statuts d'exemplaire. (INSERT: 1)
- `docs_type` : Referentiel : types de document (+ durees pret/resa). (INSERT: 1)
- `docs_codestat` : Referentiel : code statistique exemplaire. (INSERT: 1)
- `lenders` : Preteurs du reseau (dont MDN). (INSERT: 1)
- `notice_statut` : Table technique PMB (module annexe ou cache ; hors perimetre de reprise a priori, a confirmer). (INSERT: 1)

## Referentiels cles (parametrage public, sans donnees personnelles)
- `empr_categ` : 1 Adulte, 2 Collectivite (= comptes pro), 9 Enfant, 12 Hebergement.
- `empr_codestat` : Commune / Indetermine / Communaute de communes / Hors CC.
- `empr_statut` : Actif / Interdit.
- `docs_location` : 12 sites (Fourmies, Feron, Glageon, Trelon, Wallers-en-Fagne, Anor, Wignehies, Eppe-Sauvage, Ecomusee, Mediapass, Ohain, Willies).
- `docs_type` : Livre, CD, DVD, Jeu, Periodique... (durees pret/resa par type).
- `docs_statut` : Empruntable, Perdu, Pilonne, En reparation... ; `docs_codestat` : Adulte/Tous/Jeune.

## Questions ouvertes
- Correspondance exacte comptes pro <-> sites : `empr` categ 2 + `empr_groupe` ? (comptage local).
- Regles d'amende/relance (niveaux 0-3, montants) : code PMB v8 a consulter.
- Champs custom (empr_/expl_/notices_custom) : utilises ? (tables de valeurs a controler).
- Medias explnum : fichiers inclus dans le dump ? Non (pas de BLOB de contenu repere) — ressources externes a inventorier.
