from transformers import BartTokenizer, BartForConditionalGeneration
import torch
from pdf_text_extractor import PDF_Text_Extractor

class TextSummarizer1:
    def __init__(self, model_name="facebook/bart-large-cnn"):
        """
        Initialise le résumeur avec un modèle BART pré-entraîné.
        :param model_name: Nom du modèle BART à utiliser (par défaut "facebook/bart-large-cnn").
        """
        self.model_name = model_name
        self.tokenizer = BartTokenizer.from_pretrained(model_name)
        self.model = BartForConditionalGeneration.from_pretrained(model_name)

    def summarize(self, text, max_length=130, min_length=30):
        """
        Génère un résumé pour le texte donné en utilisant BART.
        :param text: Texte à résumer.
        :param max_length: Longueur maximale du résumé.
        :param min_length: Longueur minimale du résumé.
        :return: Résumé du texte.
        """
        # si c'est une liste (plus d'une page), joindre les textes pour avoir un string
        if isinstance(text, list):
            text = ' '.join(text)
            
        #Debug
        #print(text)
        
        # Tokenizer le texte
        inputs = self.tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=1024, truncation=True)
        
        # Générer le résumé
        summary_ids = self.model.generate(inputs, max_length=max_length, min_length=min_length, length_penalty=2.0, num_beams=4, early_stopping=True)
        summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        
        return summary


# Exemple d'utilisation avec un fichier pdf

'''chemin = "test.pdf"
preprocessor = PDF_Text_Extractor(chemin)
texte = preprocessor.extract_text()

summarizer = TextSummarizer()

# Supprime les retours à la ligne successifs et remplace les doubles espaces par des simples
texte = ' '.join(texte).replace('\n\n', ' ').replace('  ', ' ')

# Augmenter la taille du résumé
max_length = 300  # longueur maximale du résumé (en tokens)
min_length = 100  # longueur minimale du résumé (en tokens)

resume = summarizer.summarize(texte, max_length=max_length, min_length=min_length)
print("Résumé: ")
print(resume)'''