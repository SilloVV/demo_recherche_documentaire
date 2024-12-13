import docx
import nltk
from nltk.tokenize import sent_tokenize

# Télécharger les ressources nltk nécessaires
nltk.download('punkt')

class DOCX_Text_Extractor:
    def __init__(self, docx_path):
        """
        Initialise le préprocesseur avec le chemin du fichier DOCX.
        :param docx_path: chemin du fichier DOCX à traiter.
        """
        self.docx_path = docx_path
        self.paragraphs_sentences = []

    def extract_text(self):
        """
        Extrait le texte de chaque paragraphe du fichier DOCX en utilisant python-docx.
        :return: une liste contenant le texte de chaque paragraphe.
        """
        doc = docx.Document(self.docx_path)
        paragraphs_text = [para.text for para in doc.paragraphs if para.text.strip() != '']
        return paragraphs_text

    def tokenize_sentences(self, text):
        """
        Divise le texte donné en phrases. (nltk)
        :param text: texte à diviser.
        :return: une liste de phrases.
        """
        return sent_tokenize(text)



# Exemple d'utilisation avec un fichier DOCX

chemin = "test.docx"
preprocessor = DOCX_Text_Extractor(chemin)
paragraphs_sentences = preprocessor.extract_text()
print(paragraphs_sentences)