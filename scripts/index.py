import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tqdm import tqdm
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from src.ingestion import load_recipes

filepath = "data/raw/recipes_raw_nosource_epi.json"
chroma_directory = "data/chroma"
embedding_model = "nomic-embed-text"
batch_size = 500


def main():
    print("loading recipes...")
    docs = load_recipes(filepath)
    print(f"loaded {len(docs)} recipes")

    print("indexing into chromadb...")
    embeddings = OllamaEmbeddings(model=embedding_model)
    database   = None

    batches = [docs[i:i + batch_size] for i in range(0, len(docs), batch_size)]

    for batch in tqdm(batches, desc="indexing"):
        if database is None:
            database = Chroma.from_documents(
                documents=batch,
                embedding=embeddings,
                persist_directory=chroma_directory,
            )
        else:
            database.add_documents(batch)

    print(f"done! {len(docs)} recipes indexed.")


if __name__ == "__main__":
    main()