# bm25.py – placeholder for BM25 retrieval implementation

"""BM25 retrieval utilities.
Uses `rank_bm25` to rank passages based on query terms.
"""

from rank_bm25 import BM25Okapi

class BM25Retriever:
    def __init__(self, documents: list[str]):
        """Initialize with a list of raw document texts.
        Tokenizes on whitespace; in production replace with a proper tokenizer.
        """
        self.corpus = [doc.split() for doc in documents]
        self.bm25 = BM25Okapi(self.corpus)

    def retrieve(self, query: str, top_k: int = 5) -> list[tuple[int, float]]:
        """Return top_k documents as (index, score) tuples.
        """
        query_tokens = query.split()
        scores = self.bm25.get_scores(query_tokens)
        # Get indices of top_k scores
        top_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:top_k]
        return [(i, scores[i]) for i in top_indices]
