import docx
import PyPDF2
from bs4 import BeautifulSoup

def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text() + "\n"
    return text

def clean_pdf_text(text):
    text = text.replace("-\n", "")
    text = text.replace("\n", " ")
    text = text.replace("  ", " ")
    text = text.replace(". ", ".\n")
    return text

def extract_text_from_html(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        soup = BeautifulSoup(file, 'lxml')
        return soup.get_text()