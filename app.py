import json
from datetime import datetime
from pathlib import Path
from zipfile import ZipFile

import streamlit as st

from converter import SUPPORTED_EXTENSIONS, convert_file, to_json_download

APP_NAME = "DocFix Studio"
OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)


def safe_filename(name: str) -> str:
    safe = "".join(c if c.isalnum() or c in ("-", "_", ".") else "_" for c in name)
    return safe[:120]


def create_export_zip(results):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_path = OUTPUT_DIR / f"docfix_export_{timestamp}.zip"

    with ZipFile(zip_path, "w") as zipf:
        for result in results:
            base = safe_filename(result["filename"])

            zipf.writestr(f"{base}.md", result["markdown"])
            zipf.writestr(f"{base}.txt", result["plain_text"])
            zipf.writestr(f"{base}.document.json", to_json_download(result["json"]))
            zipf.writestr(f"{base}.chunks.json", to_json_download(result["chunks"]))

    return zip_path


st.set_page_config(
    page_title=APP_NAME,
    page_icon="📄",
    layout="wide",
)

st.title("📄 DocFix Studio")
st.caption("Open-source document cleanup and RAG-prep tool powered by Docling.")

st.markdown(
    """
    Upload messy documents and convert them into **clean Markdown**, **plain text**,
    **structured JSON**, and **RAG-ready chunks** for AI apps, chatbots, search tools,
    and study systems.
    """
)

with st.sidebar:
    st.header("Export settings")

    chunk_size = st.slider(
        "Chunk size",
        min_value=500,
        max_value=3000,
        value=1200,
        step=100,
        help="The maximum number of characters in each RAG chunk.",
    )

    overlap = st.slider(
        "Chunk overlap",
        min_value=0,
        max_value=800,
        value=200,
        step=50,
        help="How many characters overlap between chunks.",
    )

    st.divider()

    st.subheader("Supported files")
    st.write(", ".join(sorted(SUPPORTED_EXTENSIONS)))

    st.info(
        "Use chunks.json when preparing documents for chatbots, RAG apps, "
        "LangChain, LlamaIndex, Supabase, or custom AI search systems."
    )

uploaded_files = st.file_uploader(
    "Upload one or more documents",
    type=[ext.replace(".", "") for ext in SUPPORTED_EXTENSIONS],
    accept_multiple_files=True,
)

if "results" not in st.session_state:
    st.session_state["results"] = []

if uploaded_files:
    st.success(f"{len(uploaded_files)} file(s) selected.")

    if st.button("Convert document(s)", type="primary"):
        st.session_state["results"] = []

        progress = st.progress(0)
        status_area = st.empty()

        for index, uploaded_file in enumerate(uploaded_files):
            status_area.info(f"Converting {uploaded_file.name}...")

            try:
                result = convert_file(
                    uploaded_file,
                    chunk_size=chunk_size,
                    overlap=overlap,
                )
                result["status"] = "Success"
                result["error"] = ""
                st.session_state["results"].append(result)

            except Exception as e:
                st.session_state["results"].append(
                    {
                        "filename": uploaded_file.name,
                        "extension": Path(uploaded_file.name).suffix.lower(),
                        "status": "Failed",
                        "error": str(e),
                        "markdown": "",
                        "plain_text": "",
                        "json": {},
                        "chunks": [],
                        "chunk_count": 0,
                        "plain_text_characters": 0,
                        "markdown_characters": 0,
                    }
                )

            progress.progress((index + 1) / len(uploaded_files))

        status_area.success("Conversion finished.")

results = st.session_state["results"]

if results:
    st.subheader("Conversion results")

    summary_rows = [
        {
            "File": item["filename"],
            "Status": item["status"],
            "Type": item["extension"],
            "Chunks": item["chunk_count"],
            "Text characters": item["plain_text_characters"],
            "Error": item["error"],
        }
        for item in results
    ]

    st.dataframe(summary_rows, use_container_width=True)

    successful_results = [item for item in results if item["status"] == "Success"]

    if successful_results:
        zip_path = create_export_zip(successful_results)

        with open(zip_path, "rb") as f:
            st.download_button(
                "Download all successful exports as ZIP",
                f,
                file_name=zip_path.name,
                mime="application/zip",
            )

    selected_filename = st.selectbox(
        "Preview file",
        [item["filename"] for item in results],
    )

    selected = next(item for item in results if item["filename"] == selected_filename)

    if selected["status"] == "Failed":
        st.error(selected["error"])
    else:
        col1, col2, col3 = st.columns(3)
        col1.metric("File", selected["filename"])
        col2.metric("RAG chunks", selected["chunk_count"])
        col3.metric("Plain text characters", selected["plain_text_characters"])

        tab1, tab2, tab3, tab4 = st.tabs(
            ["Markdown preview", "Plain text", "RAG chunks", "JSON"]
        )

        with tab1:
            st.markdown(selected["markdown"])

            st.download_button(
                "Download Markdown",
                selected["markdown"],
                file_name=f"{safe_filename(selected['filename'])}.md",
                mime="text/markdown",
            )

        with tab2:
            st.text_area(
                "Plain text output",
                selected["plain_text"],
                height=500,
            )

            st.download_button(
                "Download TXT",
                selected["plain_text"],
                file_name=f"{safe_filename(selected['filename'])}.txt",
                mime="text/plain",
            )

        with tab3:
            st.caption("Previewing the first 5 chunks.")
            st.json(selected["chunks"][:5])

            st.download_button(
                "Download chunks.json",
                to_json_download(selected["chunks"]),
                file_name=f"{safe_filename(selected['filename'])}.chunks.json",
                mime="application/json",
            )

        with tab4:
            st.json(selected["json"])

            st.download_button(
                "Download document.json",
                to_json_download(selected["json"]),
                file_name=f"{safe_filename(selected['filename'])}.document.json",
                mime="application/json",
            )

st.divider()

st.markdown(
    """
    ### Why DocFix Studio?

    Most AI apps struggle when documents are messy, scanned, badly formatted,
    or full of tables. DocFix Studio helps clean and prepare files before they
    are used in chatbots, search systems, study tools, school assistants, or
    RAG pipelines.

    **No paid API key is required for the basic version.**
    """
)
