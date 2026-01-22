from sentence_transformers import SentenceTransformer
_model = "sentence-transformers/all-MiniLM-L6-v2"
embedding = SentenceTransformer(_model)

def vector_embedding(text):
    return embedding.encode(text)

def embed_pages(page_contents):
    page_contents_vectors =  [vector_embedding(content)for content in page_contents]
    return page_contents_vectors