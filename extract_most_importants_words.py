import nltk
from sklearn.feature_extraction.text import TfidfVectorizer

# Télécharger les stop words en français via nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

# Obtenir les stopwords en français
stop_words_fr = stopwords.words('french')

# Exemple de résumés
summaries = [
    "Le projet de rénovation vise à améliorer la structure du bâtiment.",
    "Le plan de rénovation inclut des améliorations énergétiques pour la performance thermique.",
    "Les travaux prévoient des réaménagements des espaces intérieurs et l'ajout de nouvelles installations."
]

# Initialiser le TF-IDF vectorizer avec les stopwords français
vectorizer = TfidfVectorizer(stop_words=stop_words_fr)

# Appliquer le TF-IDF sur les résumés
X = vectorizer.fit_transform(summaries)

# Récupérer les mots et leurs scores TF-IDF
words = vectorizer.get_feature_names_out()
scores = X.toarray()

# Extraire les mots avec les scores les plus élevés pour chaque résumé
top_n = 5  # Nombre de mots-clés à extraire
for i, score in enumerate(scores):
    indices = score.argsort()[-top_n:][::-1]  # Trier les scores
    top_keywords = words[indices]
    print(f"Résumé {i+1}: {', '.join(top_keywords)}")
