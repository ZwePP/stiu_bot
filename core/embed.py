from sentence_transformers import SentenceTransformer
_model = "sentence-transformers/all-MiniLM-L6-v2"
embedding = SentenceTransformer(_model)


def vector_encode(page_content):
    page_content_vectors = [embedding.encode(content) for content in page_content]
    return page_content_vectors #return vector lists