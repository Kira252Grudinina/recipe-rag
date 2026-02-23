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
- python 3.11+
- pip install uv
- ollama installed and running (https://ollama.com/download)

then pull the models:
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

## run with docker
make sure ollama is running, then:
```
uv run scripts/index.py
docker compose up --build
```

## local setup
```
uv sync
uv run scripts/index.py
uv run uvicorn src.api:app --reload
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

## notes
- dataset: epicurious recipes (~25k recipes)
- indexing takes ~30 minutes on cpu
- chroma index is not included in the repo, run index.py first
