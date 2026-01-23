#Turn user query -> vectors -> search chroma -> return top chunks
from .embed import vector_embedding
from .vectordb import get_collections

#search chroma with vectorized query
def search_chroma(query, k=3):
    query_vector = vector_embedding(query)
    collection = get_collections()

    result = collection.query(
        query_embeddings = [query_vector],
        n_results = k
    )
    return result

if __name__ == "__main__":
    result = search_chroma("Location of a campus")
    print(result['documents'][0])