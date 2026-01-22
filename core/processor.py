import uuid
from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_doc(pages):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500,
    chunk_overlap = 50)

    chunks = text_splitter.split_documents(pages)

    #get meta data list
    metadata_list = [chunk.metadata for chunk in chunks]

    #get id list
    id_list = [str(uuid.uuid4()) for _ in chunks]

    page_content = [chunk.page_content for chunk in chunks]
    
    return metadata_list, id_list, page_content
