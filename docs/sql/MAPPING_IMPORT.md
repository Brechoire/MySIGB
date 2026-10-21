# MAPPING_IMPORT — source vers cible

Cible : futur projet (MySIGB Django existant en hypothese : apps catalogue / adherents / circulation ; colonne cible = hypothese ou « a decider »). Exclusions assumees : mots de passe/hachages/sessions/jetons (reinitialiser), caches (*_cache, index_*), historique technique (sessions, logs).

| source | sens et preuve | cible (hypothese) | transformation | NULL/sentinelles | ids | verification | statut |
|---|---|---|---|---|---|---|---|
| notices.* | notice biblio ; CREATE TABLE observe | catalogue.Notice (a decider) | utf8mb3->utf8mb4, conserver code/ISBN en chaines | '' -> NULL ; 0000-00-00 -> NULL | garder notice_id en ref source | COUNT + echantillon metier | a faire |
| exemplaires.* | exemplaire ; CB UNIQUE observee | catalogue.Exemplaire (a decider) | CB en chaine (zeros initiaux) | expl_bulletin=0 -> NULL | garder expl_id + CB | orphelins sans notice | a faire |
| bulletins.* | bulletin ; double lien notice | catalogue.Bulletin (a decider) | dates mention/date_date | 0000-00-00 -> NULL | garder bulletin_id | bulletins sans mere | a faire |
| authors + responsability | autorites + liaisons ; PK composite | catalogue.Auteur (a decider) | dedupliquer (notice,auteur,fonction,ordre) | fonction '' -> auteur | garder ids | doublons | a faire |
| empr.* sauf secrets | lecteurs ; 4 categ / 4 codestat / 2 statuts | adherents.Adherent (a decider) | reinitialiser acces ; categ 2 = compte pro | expiration NULL = a statuer | garder id_empr + CB | adhesions expirees | a faire |
| pret.* | encours ; PK=exemplaire | circulation.Pret (a decider) | recalculer retard (pret_retour < date) | 0000-00-00 -> NULL | couple (empr,expl) | prets orphelins | a faire |
| pret_archive.* | historique denormalise (~complet voulu) | archive/statistiques (a decider) | lots bornes, idempotent (arc_id) | dates zero -> NULL | garder arc_id | COUNT par annee | a faire |
| resa.* + resa_archive | reservations | circulation.Reservation (a decider) | file d'attente | resa_cb '' -> NULL | garder id_resa | resas sans cible | a faire |
| comptes/transactions | finance ; 2 comptes/lecteur supposes | finance (a decider) | montants DECIMAL exacts | solde NULL -> 0.00 | garder id_compte | soldes vs mouvements | a faire |
| docs_* + lenders | referentiels + 12 sites | referentiels cibles | import prealable (ordre 1) | — | garder ids sources | couverture | a faire |
