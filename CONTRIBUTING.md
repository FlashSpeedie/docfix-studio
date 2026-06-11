# Contributing to DocFix Studio

Thank you for your interest in improving DocFix Studio. This guide covers everything you need to get started.

## Local setup

1. Fork the repository.
2. Clone your fork:
   ```bash
   git clone https://github.com/FlashSpeedie/docfix-studio.git
   cd docfix-studio
   ```
3. Create a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```
5. Run the app:
   ```bash
   streamlit run app.py
   ```

## Create an issue

Found a bug or have a feature request?

1. Search existing issues to avoid duplicates.
2. Open a new issue with a clear title and description.
3. For bugs, include steps to reproduce, expected behavior, and actual behavior.
4. For features, explain the use case and why it fits the project.

## Submit a pull request

1. Create a new branch for your change:
   ```bash
   git checkout -b fix/short-description
   ```
2. Make your changes.
3. Test locally with `streamlit run app.py`.
4. Update docs if needed.
5. Commit with a clear message:
   ```bash
   git add .
   git commit -m "Add short description"
   ```
6. Push to your fork and open a pull request.

## Good first issue ideas

If you're new to the project, these are great places to start:

* Improve the sample handbook in `examples/sample-handbook.txt`.
* Add more example file types to `examples/`.
* Improve error messages in the app.
* Add a progress bar for batch uploads.
* Refactor `converter.py` to make it easier to extend.
* Write unit tests for `chunker.py`.
