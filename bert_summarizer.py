from transformers import BertTokenizer, BertForSequenceClassification
import torch
from pdf_text_extractor import PDF_Text_Extractor

class BertSummarizer:
    def __init__(self, model_name="bert-base-uncased"):
        """
        Initialise le résumeur avec un modèle BERT pré-entraîné.
        :param model_name: Nom du modèle BERT à utiliser (par défaut "bert-base-uncased").
        """
        self.model_name = model_name
        self.tokenizer = BertTokenizer.from_pretrained(model_name)
        self.model = BertForSequenceClassification.from_pretrained(model_name, num_labels=1)

    def summarize(self, text, max_length=130, min_length=30):
        """
        Génère un résumé pour le texte donné en utilisant BERT comme classificateur de phrases.
        :param text: Texte à résumer.
        :param max_length: Longueur maximale du résumé.
        :param min_length: Longueur minimale du résumé.
        :return: Résumé du texte.
        """
        # si c'est une liste (plus d'une page), joindre les textes pour avoir un string
        if isinstance(text, list):
            text = ' '.join(text)
        # Découper le texte en phrases
        sentences = text.split('.')

        # Tokenizer et scorer les phrases
        scored_sentences = []
        for sentence in sentences:
            inputs = self.tokenizer(sentence, return_tensors="pt", max_length=512, truncation=True)
            with torch.no_grad():
                outputs = self.model(**inputs)
                score = outputs.logits.item()
                scored_sentences.append((sentence, score))

        # Trier les phrases par score décroissant
        scored_sentences = sorted(scored_sentences, key=lambda x: x[1], reverse=True)

        # Construire le résumé en respectant les limites de longueur
        summary = []
        current_length = 0
        for sentence, score in scored_sentences:
            sentence_length = len(sentence.split())
            if current_length + sentence_length > max_length:
                break
            if sentence_length >= min_length:
                summary.append(sentence.strip())
                current_length += sentence_length

        return '. '.join(summary) + '.'


# Exemple d'utilisation avec un fichier pdf

'''chemin = "test.docx"
preprocessor = PDF_Text_Extractor(chemin)
texte = preprocessor.extract_text()

summarizer = TextSummarizer()

# Supprime les retours à la ligne successifs et remplace les doubles espaces par des simples
texte = ' '.join(texte).replace('\n\n', ' ').replace('  ', ' ')

# Augmenter la taille du résumé
max_length = 80  # longueur maximale du résumé (en tokens)
min_length = 20   # longueur minimale du résumé (en tokens)

resume = summarizer.summarize(texte, max_length=max_length, min_length=min_length)
print("Résumé:")
print(resume)'''