import fitz  # PyMuPDF
import nltk
from nltk.tokenize import sent_tokenize

# Télécharger les ressources nltk nécessaires
nltk.download('punkt')

class PDF_Text_Extractor:
    def __init__(self, pdf_path):
        """
        Initialise le préprocesseur avec le chemin du PDF.
        :param pdf_path: chemin du fichier PDF à traiter.
        """
        self.pdf_path = pdf_path
        self.pages_sentences = []

    def extract_text(self):
        """
        Extrait le texte de chaque page du PDF en utilisant PyMuPDF.
        :return: une liste contenant le texte de chaque page.
        """
        pages_text = []
        with fitz.open(self.pdf_path) as pdf_document:
            for page_number in range(len(pdf_document)):
                page = pdf_document.load_page(page_number)
                text = page.get_text()
                pages_text.append(text)
        return pages_text


    def tokenize_sentences(self, text):
        """
        Divise le texte donné en phrases. (nltk)
        :param text: texte à diviser.
        :return: une liste de phrases.
        """
        return sent_tokenize(text)


    

#chemin= "test.pdf"
#preprocessor = PDF_Text_Extractor(chemin)
#text = preprocessor.extract_text()
#print(text)



