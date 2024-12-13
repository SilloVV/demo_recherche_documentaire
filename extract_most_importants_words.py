import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from docx_text_extractor import DOCX_Text_Extractor
from pdf_text_extractor import PDF_Text_Extractor
from bert_summarizer import TextSummarizer
from bart_summarizer import TextSummarizer1

# Télécharger les stop words en français via nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

# Obtenir les stopwords en français
stop_words_fr = stopwords.words('french')

# Exemple d'extraction de texte avec un fichier DOCX
chemin = "test.docx"
preprocessor = DOCX_Text_Extractor(chemin)
paragraphs_sentences = preprocessor.extract_text()
text = ' '.join(paragraphs_sentences).replace('\n\n', ' ').replace('  ', ' ')

# Exemple d'extraction de texte avec un fichier PDF
chemin = "test.pdf"
preprocessor_1 = PDF_Text_Extractor(chemin)
text1 = preprocessor_1.extract_text()

# Initialiser les résumés à traiter
summaries = []

# Initialiser le résumeur BERT
summarizer = TextSummarizer()

# Initialiser le résumeur BART
summarizer1 = TextSummarizer1()


# Générer un résumé pour le texte donné
resume = summarizer.summarize(text, max_length=80, min_length=20)
print("Résumé Bert: ")
print(resume)

resume1 = summarizer1.summarize(text1, max_length=300, min_length=100)
print("Résumé Bart: ")
print(resume1)



# Ajouter le résumé à la liste summaries
summaries.append(resume)
summaries.append(resume1)


# Initialiser le TF-IDF vectorizer avec les stopwords français
vectorizer = TfidfVectorizer(stop_words=stop_words_fr)

# Appliquer le TF-IDF sur les résumés
X = vectorizer.fit_transform(summaries)

# Récupérer les mots et leurs scores TF-IDF
words = vectorizer.get_feature_names_out()
scores = X.toarray()

# Extraire les mots avec les scores les plus élevés pour chaque résumé
top_n = 10  # Nombre de mots-clés à extraire
for i, score in enumerate(scores):
    indices = score.argsort()[-top_n:][::-1]  # Trier les scores
    top_keywords = words[indices]
    print(f"Résumé {i+1}: {', '.join(top_keywords)}")
