# Recipe RAG Assistant

![python](https://img.shields.io/badge/python-3.11+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-green)
![docker](https://img.shields.io/badge/docker-ready-blue)
![ollama](https://img.shields.io/badge/ollama-local-grey)

a rag-based cooking assistant that answers questions about recipes.

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
## data

download the dataset from https://eightportions.com/datasets/Recipes/#fn:1

place the json files in `data/raw/`:
```
data/raw/recipes_raw_nosource_epi.json
data/raw/recipes_raw_nosource_fn.json
data/raw/recipes_raw_nosource_ar.json
```

then run indexing (uses epicurious by default, ~30 min on cpu):
```
uv run scripts/index.py
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
