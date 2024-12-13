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


# Extraction de Mots-Clés avec TF-IDF

## Qu'est-ce que TF-IDF ?

**TF-IDF** (Term Frequency - Inverse Document Frequency) est une méthode d'analyse de texte utilisée pour évaluer l'importance d'un mot dans un document, en tenant compte de sa fréquence dans le document et dans l'ensemble du corpus. Elle est particulièrement utile pour extraire des mots-clés d'un texte.

### 1. **TF (Term Frequency) :** 
Mesure la fréquence d'un mot dans un document donné. Plus un mot apparaît fréquemment dans un document, plus sa valeur TF est élevée. 

\[
TF = \frac{\text{Nombre d'occurrences du mot dans le document}}{\text{Nombre total de mots dans le document}}
\]

### 2. **IDF (Inverse Document Frequency) :** 
Mesure l'importance d'un mot dans l'ensemble des documents. Plus un mot apparaît dans un grand nombre de documents, moins il est considéré comme pertinent.

\[
IDF = \log \left( \frac{\text{Nombre total de documents}}{\text{Nombre de documents contenant ce mot}} \right)
\]

### 3. **TF-IDF :** 
Le score final pour chaque mot est calculé en multipliant sa valeur TF et IDF :

\[
\text{TF-IDF} = TF \times IDF
\]

### Résumé :
Un mot avec une fréquence élevée dans un document mais rare dans l'ensemble des documents aura un score TF-IDF élevé, ce qui signifie qu'il est important pour ce document.

---

## Utilisation de TF-IDF dans le fichier `extract_most_important_words.py`

Le fichier **`extract_most_important_words.py`** utilise **TF-IDF** pour extraire les mots-clés les plus importants de plusieurs résumés. Voici le fonctionnement du script :

1. **Prétraitement des données :**
   Le script commence par charger une série de résumés sous forme de texte dans une liste Python.

2. **Vectorisation avec `TfidfVectorizer` :**
   Le texte est ensuite transformé en une matrice de scores TF-IDF à l'aide de `TfidfVectorizer` de la bibliothèque `scikit-learn`.

   ```python
   vectorizer = TfidfVectorizer(stop_words=stop_words_fr)
   X = vectorizer.fit_transform(summaries)


