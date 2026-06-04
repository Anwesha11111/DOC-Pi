import re
import unicodedata

def clean_text(text: str) -> str:
    """Normalize and clean raw extracted text.
    - Unicode NFKC normalization
    - Remove non‑printable characters
    - Collapse multiple whitespace
    - Lower‑case
    """
    # Unicode normalisation
    text = unicodedata.normalize("NFKC", text)
    # Remove control characters
    text = re.sub(r"[\x00-\x1F\x7F]", " ", text)
    # Collapse whitespace
    text = re.sub(r"\s+", " ", text)
    return text.strip().lower()
