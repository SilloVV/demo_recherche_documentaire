# demo_recherche_documentaire
Ceci est une démo pour un projet de recherche de documents pdf,word,pptx.

## La Stratégie est la suivante :
- Extraire des résumés à partir de chaque document (PDF ou PowerPoint) :
- Extraire des mots-clés de chaque résumé (ou du PDF d'origine, si pertinent) :
- Générer un embedding pour chaque liste de mots clés de chaque résumé 
- Calculer la similarité entre tous les vecteurs des résumés :
- Effectuer un clustering à partir de la matrice de similarité pour regrouper les documents similaires 
- Calculer la similarité entre les mots-clés fournis par l’utilisateur et les centres des clusters, puis proposer les N documents les plus similaires aux mots-clés dans le cluster correspondant.

## Classes :
- PDF_Text_Extractor: Permet d'extraire et stocker le texte d'un fichier pdf
-  DOCX_Text_Extractor: Permet d'extraire et stocker le texte d'un fichier word
- bert_summarizer : Permet de génerer le résumé du texte extrait à partir du modèle bert-base-uncased
- bart_summarizer


# Choix du modèle

## BERT vs T5 vs BART : 

- **BERT** : Modèle basé sur l'encodeur Transformer, idéal pour la compréhension du texte. Utilisé principalement pour des **résumés extractifs**, où le modèle sélectionne des passages clés du texte sans générer de nouvelles phrases.
  
- **T5** : Modèle "text-to-text", conçu pour des tâches de génération de texte, ce qui le rend plus adapté pour des **résumés abstratifs**, où le modèle génère un texte condensé et reformulé à partir du contenu original.

- **BART** : Modèle hybride qui combine un encodeur de type BERT et un décodeur de type GPT. Il est conçu pour des tâches de **résumés abstratifs** comme T5, mais il est également efficace pour d'autres tâches comme la traduction et la génération de texte. BART est particulièrement adapté pour générer des résumés plus cohérents et naturels, avec la capacité de reformuler et simplifier le contenu.

## Bases et tailles des modèles
 **BERT-Base** : Modèle standard avec des performances solides, rapide et moins coûteux en termes de ressources.
- **BERT-Large** : Version plus grande, offrant de meilleures performances pour des tâches complexes mais nécessitant plus de mémoire et de puissance de calcul.
- **BERT-Small** : Version plus petite de BERT, optimisée pour les environnements avec des ressources limitées, mais avec moins de précision.
  
- **T5-Base / T5-Large** : Version de T5 où **Base** est plus léger et rapide, tandis que **Large** offre une meilleure précision au prix de ressources accrues.
- **T5-3B** : Version de T5 avec 3 milliards de paramètres, offrant des performances encore meilleures, mais nécessitant plus de ressources.
- **T5-11B** : La plus grande version de T5 avec 11 milliards de paramètres, pour des tâches complexes, mais extrêmement coûteuse en ressources.

- **BART-Base / BART-Large** : BART est disponible en versions **Base** et **Large**, où **Large** offre une meilleure performance pour des résumés abstratifs, mais nécessite plus de ressources.




