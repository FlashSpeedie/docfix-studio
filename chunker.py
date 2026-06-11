from typing import List, Dict


def chunk_text(text: str, chunk_size: int = 1200, overlap: int = 200) -> List[Dict]:
    """
    Split long text into RAG-ready chunks.

    Each chunk includes metadata so users can export the chunks for chatbot,
    search, or RAG workflows.
    """
    cleaned = (text or "").strip()

    if not cleaned:
        return []

    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0")

    if overlap < 0:
        raise ValueError("overlap cannot be negative")

    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    chunks = []
    start = 0
    chunk_id = 1

    while start < len(cleaned):
        end = min(start + chunk_size, len(cleaned))
        chunk = cleaned[start:end].strip()

        if chunk:
            chunks.append(
                {
                    "id": chunk_id,
                    "content": chunk,
                    "characters": len(chunk),
                    "start_char": start,
                    "end_char": end,
                }
            )
            chunk_id += 1

        start += chunk_size - overlap

    return chunks
