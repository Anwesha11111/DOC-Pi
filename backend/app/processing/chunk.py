# chunk.py – placeholder for document chunking utilities

"""Chunking utilities to split cleaned text into overlapping windows.
Default: 512 tokens per chunk with 50 token overlap.
"""

def chunk_text(cleaned_text: str, max_tokens: int = 512, overlap: int = 50) -> list:
    """Return a list of text chunks.
    This stub will later use a tokenizer (e.g., tiktoken) to count tokens.
    """
    # TODO: implement actual token‑based chunking
    return [cleaned_text]
