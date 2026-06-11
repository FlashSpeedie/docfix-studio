# DocFix Studio

Turn messy documents into clean Markdown, plain text, structured JSON, and RAG-ready chunks.

DocFix Studio is an open-source document cleanup and RAG-prep tool powered by Docling. It helps developers, students, educators, and AI builders prepare documents before using them in chatbots, search systems, study tools, school assistants, and retrieval-augmented generation pipelines.

## Features

* Upload PDF, DOCX, PPTX, images, HTML, Markdown, and text files
* Convert documents to clean Markdown
* Export plain text
* Export structured JSON
* Export RAG-ready chunks
* Batch upload multiple files
* Download all successful exports as one ZIP
* Choose chunk size and overlap
* Local-first Streamlit app
* No paid API key required for the basic version

## Why this exists

Most AI document chatbots fail when documents are messy, scanned, badly formatted, or full of tables. DocFix Studio helps clean documents before they are used in AI workflows.

## Use cases

* Prepare PDFs for AI chatbots
* Clean school handbooks before indexing
* Convert lecture notes into Markdown
* Extract structured text from reports
* Create RAG chunks for LangChain, LlamaIndex, Supabase, or custom AI apps
* Turn messy class materials into clean study documents
* Prepare documents for search and knowledge-base systems

## Tech stack

* Python
* Streamlit
* Docling

## Installation on Windows

```bash
git clone https://github.com/YOUR_USERNAME/docfix-studio.git
cd docfix-studio
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py
```

Then open:

```text
http://localhost:8501
```

## Usage

1. Upload one or more documents.
2. Choose chunk size and overlap.
3. Click **Convert document(s)**.
4. Preview Markdown, plain text, chunks, or JSON.
5. Download Markdown, TXT, JSON, chunks.json, or a ZIP export.

## Output formats

### Markdown

Good for documentation, notes, websites, and clean reading.

### Plain text

Good for search, simple processing, and AI prompts.

### JSON

Good for structured document pipelines.

### RAG chunks

Good for chatbot/search pipelines and retrieval systems.

## Roadmap

* Better table extraction to CSV
* OCR improvements for scanned documents
* Before/after document preview
* Optional AI cleanup with user-provided API key
* Docker setup
* CLI command
* FastAPI backend
* Export formats for LangChain, LlamaIndex, Supabase, and Chroma
* Example documents and outputs
* GIF demo in README

## Privacy

DocFix Studio runs locally in the basic version. It does not require an account or paid API key.

Do not upload sensitive files to hosted demos unless you trust the host. For private documents, run DocFix Studio locally.

## License

MIT License.

This project uses Docling for document conversion. Docling is MIT licensed. Individual model licenses may vary, so check upstream model licenses if you bundle models directly.
