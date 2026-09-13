# Personal Search Engine

A search engine built from scratch — local documents first, web search later

## Vision

The long-term goal is to build a working search engine from first principles, without relying on existing search libraries or frameworks. Starting with indexing personal local documents, the project aims to grow in stages:

1. Local document search (current stage)
2. Basic web page crawling and keyword search
3. Smarter ranking using machine learning / NLP techniques

The full pipeline, built incrementally:

Documents → Ingestion → Text extraction → Text processing → Index construction → Search → Ranking → Results

## Inspiration

Sparked by a Data Structures & Algorithms course assignment on searching and sorting — which led to exploring how these concepts apply to real-world systems like search engines.

## Current Progress

**Day 1 — Document Discovery / Ingestion**

- Scans a directory (including nested subdirectories) for supported document files
- Currently supports `.txt` and `.md` files; all other file types are ignored
- Collects metadata for each discovered file: path, filename, extension, size, and last modified time
- Raises clear errors for invalid input (nonexistent path, or a path that isn't a directory)
- Fully covered by an automated test suite (pytest)

No text extraction, indexing, or search functionality exists yet.

## Architecture

Day 1 is intentionally simple: a single function, `discover_documents(folder_path)`, that:

1. Validates the given path exists and is a directory
2. Recursively walks the directory
3. Filters for supported file extensions
4. Collects metadata into a dictionary per file
5. Returns a list of these dictionaries

No classes, no external frameworks — just plain functions and Python's standard library.

## Technology Stack

- **Python 3** — standard library (`pathlib`) is sufficient for file discovery and metadata; no external dependencies needed for this part of the project
- **pytest** — for writing and running automated tests using plain functions, without requiring class-based test structure

## Project Structure

```
personal-search-engine/
├── .gitignore              # Files/folders Git should not track
├── requirements.txt        # Python package dependencies
├── discover.py             # Document discovery logic
├── test_discover.py        # Automated tests for discover.py
└── example_documents/      # Sample files used to demo discover.py
```

## Setup

1. Clone the repository:
```bash
   git clone https://github.com/ujwalmantri/personal-search-engine.git
   cd personal-search-engine
```

2. Create and activate a virtual environment:
```bash
   python3 -m venv venv
   source venv/bin/activate
```

3. Install dependencies:
```bash
   pip install -r requirements.txt
```

## Usage

Run the discovery script against the included example folder:

```bash
python3 discover.py
```

This will print a list of discovered documents (from `example_documents/`), each with its path, filename, extension, size, and last modified time.

To scan a different folder, edit the folder path passed to `discover_documents()` in `discover.py`.

**Known limitation:** Running discovery against a folder that contains this project's own `venv/` or `.git/` directories (e.g. the project root itself) will also pick up unrelated files from those folders, since recursive search doesn't currently exclude them. Point it at a dedicated documents folder to avoid this.

## Testing

Run the test suite with:

```bash
pytest
```

Tests cover:
- Discovery of supported file types (`.txt`, `.md`)
- Unsupported files being correctly ignored
- Empty directories returning no results
- Nested directories being searched recursively
- Invalid directory paths raising appropriate errors

## Roadmap

**DONE**
- Document discovery and metadata collection (local files, `.txt`/`.md`)
- Recursive directory search
- Invalid input handling
- Automated test suite

**IN PROGRESS**
- (nothing currently in progress)

**PLANNED**
- Text extraction from discovered documents
- Text processing (tokenization, normalization)
- Index construction
- Basic search functionality
- Ranking of search results
- Basic web page crawling and keyword search
- Machine learning / NLP-based ranking improvements

## Learning

**Day - 1**
- How file structure works.
- Using `pathlib` to extract information about a particular directory
- Automated tests in python using pytest