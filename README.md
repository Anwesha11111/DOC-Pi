# AI-Powered Document Search Engine

## Overview

This project implements a **semantic document search engine** with an **interactive knowledge graph** that visualizes the reasoning path using a BFS animation.

- Upload documents (PDF, DOCX, TXT, MD, HTML)
- Generate embeddings with Sentence‑Transformers
- Store vectors in **FAISS** for fast similarity search
- Build a **Neo4j** graph of document chunks and relationships
- Front‑end built with **Next.js + TypeScript** and **React Flow** for graph visualization
- Backend powered by **FastAPI**

## Quick Start

```bash
# Clone the repo (if hosted)
# Navigate to project root
cd DOCP

# Build and start services
docker compose up --build -d

# Backend API available at http://localhost:8000
# Frontend at http://localhost:3000
```

## Directory Layout

```
DOCP/
├─ backend/
│  └─ app/
│     ├─ main.py
│     ├─ schemas.py
│     ├─ models.py
│     └─ processing/
│        ├─ ingest.py
│        ├─ embed.py
│        └─ graph.py
├─ frontend/
│  ├─ pages/
│  │  └─ index.tsx
│  ├─ components/
│  │  ├─ SearchBar.tsx
│  │  ├─ DocumentList.tsx
│  │  └─ KnowledgeGraph.tsx
│  └─ public/
├─ docker-compose.yml
├─ .gitignore
└─ README.md
```

## License

MIT License.
