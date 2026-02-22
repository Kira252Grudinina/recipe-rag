# recipe-rag

a rag-based cooking assistant that answers questions about recipes from epicurious.

## stack
- langchain
- chromadb
- ollama (nomic-embed-text + qwen2.5:7b-instruct)
- fastapi
- uv

## requirements

ollama installed and running with these models:
```
ollama pull nomic-embed-text
ollama pull qwen2.5:7b-instruct
```

## run with docker
```
docker compose up --build
```

## test
```
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "how do I make guacamole?"}'
```
```
curl http://localhost:8000/health
```

## local setup
```
uv sync
uv run scripts/index.py
uv run uvicorn src.api:app --reload
```

## notes
- dataset: epicurious recipes (~25k recipes)
- indexing takes ~30 minutes on cpu
- chroma index is not included in the repo, run index.py first
