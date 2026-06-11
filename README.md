# DocFix Studio

Convert messy documents into clean **Markdown**, **plain text**, **structured JSON**, and **RAG-ready chunks** — no paid API key required.

[Live Demo](https://huggingface.co/spaces/FlashSpeedie/docfix-studio) · [GitHub Repo](https://github.com/FlashSpeedie/docfix-studio) · [Report Bug](https://github.com/FlashSpeedie/docfix-studio/issues) · [Request Feature](https://github.com/FlashSpeedie/docfix-studio/issues)

If this project helps you, consider starring the repo to support open-source development.

---

## Overview

**DocFix Studio** is an open-source document cleanup and RAG-prep tool powered by [Docling](https://github.com/docling-project/docling).

It helps developers, students, educators, researchers, and AI builders prepare documents before using them in chatbots, search systems, school assistants, study tools, and retrieval-augmented generation pipelines.

Instead of sending messy documents directly into an AI system, DocFix Studio helps convert them into cleaner and more useful formats first.

---

## Live demo

Try the hosted demo here:

**https://huggingface.co/spaces/FlashSpeedie/docfix-studio**

> For private or sensitive documents, run DocFix Studio locally instead of uploading files to a public hosted demo.

---

## Features

* Upload PDF, DOCX, PPTX, image, HTML, Markdown, and text files
* Convert documents to clean Markdown
* Export plain text
* Export structured JSON
* Export RAG-ready chunks
* Batch upload multiple files
* Download all successful exports as one ZIP file
* Choose custom chunk size and overlap
* Local-first Streamlit app
* No login required
* No paid API key required for the basic version

---

## Why this exists

Many AI document chatbots and RAG tools struggle when documents are messy, scanned, badly formatted, or full of tables.

DocFix Studio focuses on the step before chatbot indexing:

> Clean the document first, then use it in your AI system.

This makes it useful for preparing documents for:

* AI chatbots
* RAG pipelines
* Knowledge bases
* Search systems
* School assistants
* Study tools
* Research workflows
* Documentation cleanup

---

## Supported formats

| File type  | Extensions              | Notes                                                             |
| ---------- | ----------------------- | ----------------------------------------------------------------- |
| PDF        | `.pdf`                  | Works best with readable text PDFs. Scanned PDFs may require OCR. |
| Word       | `.docx`                 | Modern Word documents.                                            |
| PowerPoint | `.pptx`                 | Slide text and document structure.                                |
| Images     | `.png`, `.jpg`, `.jpeg` | Extraction quality may depend on image clarity and OCR support.   |
| HTML       | `.html`, `.htm`         | Useful for webpages and exported site content.                    |
| Markdown   | `.md`                   | Useful for already-clean documents.                               |
| Text       | `.txt`                  | Fastest and simplest format.                                      |

---

## Output formats

### Markdown

Good for documentation, clean notes, websites, and readable document exports.

### Plain text

Good for simple search, indexing, prompt input, and lightweight processing.

### JSON

Good for structured document workflows and advanced processing pipelines.

### RAG chunks

Good for chatbot and retrieval systems such as LangChain, LlamaIndex, Supabase, Chroma, or custom vector database pipelines.

---

## Quick start

### 1. Clone the repository

```bash
git clone https://github.com/FlashSpeedie/docfix-studio.git
cd docfix-studio
```

### 2. Create a virtual environment

On Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

On macOS/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run app.py
```

Then open:

```text
http://localhost:8501
```

---

## Usage

1. Open the app.
2. Upload one or more documents.
3. Choose chunk size and overlap.
4. Click **Convert document(s)**.
5. Preview Markdown, plain text, chunks, or JSON.
6. Download individual outputs or a full ZIP export.

---

## Example use cases

* Prepare PDFs for AI chatbots
* Clean school handbooks before indexing
* Convert lecture notes into Markdown
* Extract structured text from reports
* Create RAG chunks for LangChain or LlamaIndex
* Prepare documents for Supabase or Chroma
* Turn messy class materials into clean study documents
* Convert documents into search-ready text
* Build cleaner knowledge bases from existing files

---

## Project structure

```text
docfix-studio/
├─ app.py
├─ streamlit_app.py
├─ converter.py
├─ chunker.py
├─ requirements.txt
├─ README.md
├─ LICENSE
├─ .gitignore
├─ assets/
├─ examples/
└─ outputs/
```

### Main files

| File               | Purpose                                      |
| ------------------ | -------------------------------------------- |
| `app.py`           | Main Streamlit application.                  |
| `streamlit_app.py` | Hugging Face Spaces entrypoint.              |
| `converter.py`     | Handles Docling document conversion.         |
| `chunker.py`       | Splits plain text into RAG-ready chunks.     |
| `requirements.txt` | Python dependencies.                         |
| `outputs/`         | Local export folder for generated ZIP files. |

---

## Tech stack

* Python
* Streamlit
* Docling
* Hugging Face Spaces

---

## Known limitations

* Very large files may take longer to process.
* Scanned PDFs or image-only documents may require OCR.
* Conversion quality depends on the source document structure.
* Complex tables may not always export perfectly.
* Hosted demos should not be used for private or sensitive documents.

---

## Roadmap

* Better table extraction to CSV
* Before/after document preview
* Improved scanned PDF handling
* Optional AI cleanup with user-provided API key
* Docker setup
* CLI command
* Export presets for LangChain
* Export presets for LlamaIndex
* Export presets for Supabase
* Export presets for Chroma
* Example input/output files
* GIF demo in README
* Batch processing improvements

---

## Contributing

Contributions are welcome.

Good first ideas:

* Improve README examples
* Add screenshots or a GIF demo
* Add sample documents
* Improve error messages
* Add table-to-CSV export
* Add CLI support
* Add more RAG export formats
* Improve UI polish

To contribute:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Test locally.
5. Open a pull request.

---

## Privacy

DocFix Studio is local-first in the basic version.

It does not require:

* an account
* a paid API key
* OpenAI
* Gemini
* Anthropic
* external AI APIs

Do not upload sensitive files to hosted demos unless you trust the host. For private documents, run DocFix Studio locally.

Avoid uploading:

* student records
* grades
* medical records
* private business documents
* passwords
* financial documents
* confidential reports

---

## License

This project is licensed under the MIT License.

See the [LICENSE](LICENSE) file for details.

---

## Attribution

DocFix Studio uses [Docling](https://github.com/docling-project/docling) for document conversion.

Docling is MIT licensed. Individual model licenses may vary, so check upstream model licenses if you bundle models directly.

---

## Star history

If this project becomes useful to you, a star helps others discover it.

**GitHub:** https://github.com/FlashSpeedie/docfix-studio