import chromadb
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings


def load_retriever(chroma_directory, embedding_model, ollama_host, number_of_results=5):
    """
    load the chromadb vector store and return a retriever.

    Args:
        chroma_directory (str): path to the chromadb storage folder
        embedding_model (str): ollama embedding model name
        number_of_results (int): number of recipes to retrieve

    Returns:
        VectorStoreRetriever: langchain retriever
    """
    db = Chroma(
        client=chromadb.PersistentClient(path=chroma_directory),
        embedding_function=OllamaEmbeddings(model=embedding_model, base_url=ollama_host),
    )
    return db.as_retriever(search_kwargs={"k": number_of_results})