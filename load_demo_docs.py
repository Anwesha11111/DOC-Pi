"""
Run this once to pre-load the demo documents into the persistent store.
Usage:  python load_demo_docs.py  (inside the backend venv)
"""
import sys
import os

# Make sure app package is importable
sys.path.insert(0, os.path.dirname(__file__))

# Force offline mode so model loads from cache
os.environ["TRANSFORMERS_OFFLINE"] = "1"
os.environ["HF_DATASETS_OFFLINE"] = "1"

from app.index.store import init_db, save_document, save_chunk, load_all_documents
from app.processing.clean import clean_text
from app.processing.chunk import chunk_text
from app.services.embedding import get_embedding

DEMO_DIR = os.path.join(os.path.dirname(__file__), "demo_docs")

def load_demo():
    init_db()
    existing = load_all_documents()

    demo_files = [f for f in os.listdir(DEMO_DIR) if f.endswith(".txt")]
    if not demo_files:
        print("No demo files found in demo_docs/")
        return

    loaded = 0
    for fname in demo_files:
        if fname in existing:
            print(f"  [skip] {fname} already loaded")
            continue

        path = os.path.join(DEMO_DIR, fname)
        with open(path, "r", encoding="utf-8") as f:
            raw_text = f.read()

        save_document(fname, raw_text)

        cleaned = clean_text(raw_text)
        chunks = chunk_text(cleaned)

        for idx, text in enumerate(chunks):
            chunk_id = f"{fname}_chunk_{idx}"
            embedding = get_embedding(text)
            save_chunk(chunk_id, fname, idx, text, embedding)

        print(f"  [ok] {fname}  ({len(chunks)} chunks)")
        loaded += 1

    print(f"\nDone. {loaded} new document(s) loaded.")

if __name__ == "__main__":
    load_demo()
