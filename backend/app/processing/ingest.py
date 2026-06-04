import io
import os
import pathlib
from pdfminer.high_level import extract_text as pdf_extract_text
import docx2txt
import markdown

def extract_text_from_file(filename: str, content: bytes) -> str:
    """Extract plain text from supported file types.
    Supports PDF, DOCX, TXT, MD, HTML.
    """
    ext = pathlib.Path(filename).suffix.lower()
    if ext == ".pdf":
        with io.BytesIO(content) as f:
            return pdf_extract_text(f)
    elif ext == ".docx":
        # docx2txt works with file path; write temporary file
        tmp_path = f"/tmp/{os.path.basename(filename)}"
        with open(tmp_path, "wb") as tmp:
            tmp.write(content)
        text = docx2txt.process(tmp_path)
        os.remove(tmp_path)
        return text
    elif ext == ".txt":
        return content.decode(errors="ignore")
    elif ext in {".md", ".markdown"}:
        # Convert markdown to plain text
        md = content.decode(errors="ignore")
        return markdown.markdown(md)
    elif ext == ".html":
        # Simple HTML tag removal
        import re
        html = content.decode(errors="ignore")
        text = re.sub(r"<[^>]+>", " ", html)
        return text
    else:
        raise ValueError(f"Unsupported file type: {ext}")
