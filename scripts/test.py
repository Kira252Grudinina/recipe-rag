import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.generator import generate_answer

result = generate_answer(
    question="what can I make with chicken and potatoes?",
    chroma_directory="data/chroma",
    embedding_model="nomic-embed-text",
    language_model="qwen2.5:7b-instruct",
    ollama_host="http://localhost:11434",
)

print("answer:", result["answer"])
print("\nsources:")
for source in result["sources"]:
    print(f"  - {source}")