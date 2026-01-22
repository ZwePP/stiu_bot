from pathlib import Path
from .loader import load_pdf, clean_pdf
from .processor import split_doc
from .embed import embed_pages
from .vectordb import get_collections, add_to_collection

BASE_DIR = Path(__file__).resolve().parent.parent
PDF_PATH = BASE_DIR / "data" / "ug_student_handbook.pdf"


def main():
    print("Loading PDF...")
    pages = load_pdf(str(PDF_PATH))
    pages = clean_pdf(pages)

    print("Splitting documents...")
    metadatas, ids, texts = split_doc(pages)

    print("Embedding...")
    vectors = embed_pages(texts)

    print("Storing in ChromaDB...")
    collection = get_collections()
    add_to_collection(collection, texts, vectors, ids, metadatas)

    print("Ingestion complete!")


if __name__ == "__main__":
    main()
