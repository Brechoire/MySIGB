# PLAN_REPRISE — phases et garde-fous

Decision : reprise COMPLETE (21/10/2026), y compris historiques.
Preconditions : cible jetable, compte lecture seule si connexion, sauvegarde restaurable testee, arret des ecritures ou delta defini avant bascule.
Ordre : referentiels -> autorites -> notices -> bulletins -> exemplaires -> adherents -> circulation active -> archives -> finance.
Lots : bornes (ex. 5 000), checkpoints SANS donnees perso (ids techniques + comptes), quarantaine locale des rejets, simulation d'abord (dry-run + rapport).
Tests : COUNT par table et par annee, doublons (CB, couples), orphelins (prets/exemplaires/notices), parcours metier (preter/retour/reserver/relancer/facturer) sur jeu synthetique puis echantillon.
Acceptation : ecarts expliques un par un ; un COUNT identique ne prouve pas l'exactitude.
Retour arriere : reimport depuis l'export fige + rejouer le delta ; pas de rollback transactionnel promis sur DDL massif.
Volumes (indicateurs, pas effectifs) : 3897 instructions INSERT, AUTO_INCREMENT max par table dans le dictionnaire ; COUNT locaux requis avant calibrage (requetes proposees, non executees).
