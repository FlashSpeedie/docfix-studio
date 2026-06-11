import json
import tempfile
from pathlib import Path
from typing import Any, Dict

from docling.document_converter import DocumentConverter

from chunker import chunk_text

SUPPORTED_EXTENSIONS = {
    ".pdf",
    ".docx",
    ".pptx",
    ".png",
    ".jpg",
    ".jpeg",
    ".html",
    ".htm",
    ".md",
    ".txt",
}

converter = DocumentConverter()


def is_supported_file(filename: str) -> bool:
    suffix = Path(filename).suffix.lower()
    return suffix in SUPPORTED_EXTENSIONS


def convert_file(uploaded_file, chunk_size: int = 1200, overlap: int = 200) -> Dict[str, Any]:
    """
    Convert an uploaded document using Docling.

    Returns:
    - Markdown
    - Plain text
    - Structured JSON/dict
    - RAG-ready chunks
    """
    filename = uploaded_file.name
    suffix = Path(filename).suffix.lower()

    if not is_supported_file(filename):
        raise ValueError(
            f"Unsupported file type: {suffix}. Supported types: "
            f"{', '.join(sorted(SUPPORTED_EXTENSIONS))}"
        )

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(uploaded_file.getbuffer())
        tmp_path = Path(tmp.name)

    try:
        result = converter.convert(str(tmp_path))
        doc = result.document

        markdown = doc.export_to_markdown()
        plain_text = doc.export_to_text()
        doc_json = doc.export_to_dict()

        chunks = chunk_text(
            plain_text,
            chunk_size=chunk_size,
            overlap=overlap,
        )

        if not plain_text.strip() and not markdown.strip():
            raise ValueError(
                "No readable text was extracted. This file may be scanned, image-only, "
                "encrypted, or unsupported by the current converter settings."
            )

        return {
            "filename": filename,
            "extension": suffix,
            "markdown": markdown,
            "plain_text": plain_text,
            "json": doc_json,
            "chunks": chunks,
            "chunk_count": len(chunks),
            "plain_text_characters": len(plain_text),
            "markdown_characters": len(markdown),
        }

    finally:
        try:
            tmp_path.unlink(missing_ok=True)
        except Exception:
            pass


def to_json_download(data: Any) -> str:
    return json.dumps(data, indent=2, ensure_ascii=False)
