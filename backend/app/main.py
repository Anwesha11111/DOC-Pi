from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn
import os
from typing import List

from .processing.ingest import extract_text_from_file
from .services.embedding import get_embedding

app = FastAPI(title="Document Search Engine Backend")

# In‑memory store placeholders
DOCUMENT_STORE = {}
EMBEDDING_INDEX = {}
GRAPH_NODES = []  # List of node dicts for graph visualization
GRAPH_EDGES = []  # List of edge dicts

class SearchRequest(BaseModel):
    query: str
    top_k: int = 5

@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file provided")
    content = await file.read()
    # Simple text extraction based on file extension
    try:
        text = extract_text_from_file(file.filename, content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    # Store raw text
    DOCUMENT_STORE[file.filename] = text
    # Generate embedding (placeholder)
    embedding = get_embedding(text)
    EMBEDDING_INDEX[file.filename] = embedding
    return {"filename": file.filename, "status": "uploaded"}

@app.post("/search")
async def semantic_search(req: SearchRequest):
    query_emb = get_embedding(req.query)
    # Very naive cosine similarity placeholder
    import numpy as np
    scores = []
    for fname, emb in EMBEDDING_INDEX.items():
        sim = np.dot(query_emb, emb) / (np.linalg.norm(query_emb) * np.linalg.norm(emb) + 1e-10)
        scores.append((fname, float(sim)))
    scores.sort(key=lambda x: x[1], reverse=True)
    top = scores[: req.top_k]
    results = [{"filename": fname, "score": score, "snippet": DOCUMENT_STORE[fname][:200]} for fname, score in top]
    return {"query": req.query, "results": results}

@app.get("/graph")
async def get_graph():
    return {"nodes": GRAPH_NODES, "edges": GRAPH_EDGES}

@app.get("/bfs")
async def bfs_traversal(start_node: str = None):
    if not GRAPH_NODES:
        raise HTTPException(status_code=404, detail="Graph not initialized")
    start = start_node or GRAPH_NODES[0]["id"]
    visited = set()
    queue = [start]
    steps = []
    adjacency = {n["id"]: [] for n in GRAPH_NODES}
    for e in GRAPH_EDGES:
        adjacency[e["source"]].append(e["target"])
        adjacency[e["target"]].append(e["source"])
    while queue:
        node = queue.pop(0)
        if node in visited:
            continue
        visited.add(node)
        steps.append({"visit": node})
        for neigh in adjacency.get(node, []):
            if neigh not in visited:
                queue.append(neigh)
    return {"steps": steps}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
