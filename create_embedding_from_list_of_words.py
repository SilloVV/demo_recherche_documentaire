from sentence_transformers import SentenceTransformer

# Charger le modèle all-MiniLM-L6-v2
model = SentenceTransformer('all-MiniLM-L6-v2')

# Liste des mots-clés extraits (donnée lors du lancement du script extract_most_importants_words.py)
top_keywords = ["ﬁnale", "étude", "ville", "écuyers", "usure", "rénovation", "subi", "phases", "préliminaire", "projet"]

# Créer des embeddings pour les mots-clés extraits
word_embeddings = model.encode(top_keywords)

# Afficher les embeddings
for word, embedding in zip(top_keywords, word_embeddings):
    print(f"{word}: {embedding[:10]}...")  # Afficher une partie de l'embedding
