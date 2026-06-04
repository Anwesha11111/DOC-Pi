from sentence_transformers import SentenceTransformer
import numpy as np

# Load a lightweight model once (adjust model name as needed)
_MODEL = SentenceTransformer('all-MiniLM-L6-v2')

def get_embedding(text: str) -> np.ndarray:
    """Return a normalized embedding vector for the given text."""
    emb = _MODEL.encode(text, convert_to_numpy=True)
    norm = np.linalg.norm(emb) + 1e-10
    return emb / norm
