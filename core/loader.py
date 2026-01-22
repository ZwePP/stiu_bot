from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

file_path = "../data/ug_student_handbook.pdf"

def load_pdf(path):
    if not Path(path).exists():
        raise FileNotFoundError(f"PDF not found: {path}")
    loader = PyPDFLoader(path)
    pdf_document = loader.load()
    return pdf_document


def clean_pdf(pdf_document):    
    for page in pdf_document:
        page.page_content = ' '.join(page.page_content.split())
    
    return pdf_document


# For Testing
if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parent.parent
    test_path = BASE_DIR / "data" / "ug_student_handbook.pdf"
    pages = load_pdf(str(test_path))
    pages = clean_pdf(pages)
    print(pages[0].page_content[:1000])