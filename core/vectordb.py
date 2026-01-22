import chromadb
_chroma_path =  "./chroma_langchain_db"

def create_chromadb(page_content, page_content_vectors, id_list, metadata_list):
    
    chroma_client = chromadb.PersistentClient(_chroma_path)
    
    collection = chroma_client.get_or_create_collection(name="handbook_embeddings_collections")
    
    collection.add(
        documents=page_content,
        embeddings=page_content_vectors,
        ids=id_list,
        metadatas= metadata_list
    )