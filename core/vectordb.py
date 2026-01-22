import chromadb
_chroma_path =  "./chroma_langchain_db"
COLLECTION_NAME = "handbook_embeddings"


def get_collections():
    client = chromadb.PersistentClient(path=_chroma_path)
    return client.get_or_create_collection(name=COLLECTION_NAME)

def add_to_collection(collection, documents, embeddings, ids, metadatas):
    collection.add(
        documents=documents,
        embeddings=embeddings,
        ids=ids,
        metadatas= metadatas
    )
