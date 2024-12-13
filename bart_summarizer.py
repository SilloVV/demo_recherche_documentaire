from transformers import pipeline
from pdf_text_extractor import PDF_Text_Extractor

class Bart_Summarizer:
    def __init__(self, model_name="facebook/bart-large-cnn", max_chunk_size=800):
        """
        Initialise le résumeur avec un modèle BART pré-entraîné.
        :param model_name: Nom du modèle BART à utiliser (par défaut "facebook/bart-base").
        :param max_chunk_size: Taille maximale des morceaux de texte à résumer.
        """
        self.summarizer = pipeline("summarization", model=model_name)
        self.max_chunk_size = max_chunk_size

    def summarize(self, text, max_length=130, min_length=40):
        """
        Génère un résumé pour le texte donné en utilisant BART.
        :param text: Texte à résumer.
        :param max_length: Longueur maximale du résumé.
        :param min_length: Longueur minimale du résumé.
        :return: Résumé final du texte.
        """
        # Diviser le texte en morceaux plus petits
        chunks = [text[i:i + self.max_chunk_size] for i in range(0, len(text), self.max_chunk_size)]
        
        # Résumer chaque morceau de texte
        summaries = []
        for chunk in chunks:
            summary = self.summarizer(chunk, max_length=max_length, min_length=min_length, do_sample=False)
            summaries.append(summary[0]['summary_text'])
        
        # Combiner les résumés de chaque morceau
        final_summary = ' '.join(summaries)
        return final_summary

# Exemple d'utilisation
if __name__ == "__main__":
    chemin = "test.pdf"
    preprocessor = PDF_Text_Extractor(chemin)
    texte = preprocessor.extract_text()

    # Supprime les retours à la ligne successifs et remplace les doubles espaces par des simples
    texte = ' '.join(texte).replace('\n\n', ' ').replace('  ', ' ')

    summarizer = Bart_Summarizer()
    final_summary = summarizer.summarize(texte)
    final_summary = final_summary.replace('\n\n', ' ').replace('  ', ' ')
    print("Résumé: ")
    print(final_summary)