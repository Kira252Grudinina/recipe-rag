import os
from fastapi import FastAPI
from pydantic import BaseModel
from src.generator import generate_answer

app = FastAPI()

chroma_directory = "data/chroma"
embedding_model = "nomic-embed-text"
language_model = "qwen2.5:7b-instruct"
ollama_host = os.getenv("OLLAMA_HOST", "http://localhost:11434")


class Question(BaseModel):
    question: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/ask")
def ask(body: Question):
    result = generate_answer(
        question=body.question,
        chroma_directory=chroma_directory,
        embedding_model=embedding_model,
        language_model=language_model,
        ollama_host=ollama_host,
    )
    return result