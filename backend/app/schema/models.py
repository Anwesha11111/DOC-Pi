# models.py – API request/response schemas

from pydantic import BaseModel, Field
from typing import List, Optional

class DocumentUpload(BaseModel):
    filename: str = Field(..., description="Original filename of the uploaded document")
    content_type: str = Field(..., description="MIME type of the uploaded file")
    # In a real endpoint we'd accept UploadFile, but this model is for reference

class QueryRequest(BaseModel):
    query: str = Field(..., description="Natural language query from the user")
    top_k: Optional[int] = Field(5, description="Number of top results to return")

class SearchResult(BaseModel):
    doc_id: int = Field(..., description="Identifier of the matching document/chunk")
    score: float = Field(..., description="Relevance score (BM25 or embedding)")
    snippet: str = Field(..., description="Excerpt from the document showing the match")

class BFSUpdate(BaseModel):
    type: str = Field(..., description="Message type: init, step, done")
    current: Optional[str] = Field(None, description="Current node being visited")
    queue: List[str] = Field(default_factory=list)
    visited: List[str] = Field(default_factory=list)
    # Additional fields can be added for path info, confidence, etc.
