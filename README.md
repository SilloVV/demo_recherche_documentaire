# demo_recherche_documentaire
Ceci est une démo pour un projet de recherche de documents pdf,word,pptx.

## La Stratégie est la suivante :
-Extraire des résumés à partir de chaque document (PDF ou PowerPoint) :
-Extraire des mots-clés de chaque résumé (ou du PDF d'origine, si pertinent) :
-Générer un embedding pour chaque liste de mots clés de chaque résumé 
-Calculer la similarité entre tous les vecteurs des résumés :
-Effectuer un clustering à partir de la matrice de similarité pour regrouper les documents similaires 
-Calculer la similarité entre les mots-clés fournis par l’utilisateur et les centres des clusters, puis proposer les N documents les plus similaires aux mots-clés dans le cluster correspondant.

