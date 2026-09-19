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

**Day 2 — Text Extraction**

- Reads the raw text content of a given file
- Correctly handles missing files and directories
- Raises a clear, custom error when a file can't be decoded as text
- fully covered by an automated test suite

No indexing or search functionality exists yet. Discovery and extraction are not yet connected into a single pipeline.

**Day 3 — Pipeline (Discovery + Extraction)**

- `load_documents(folder_path)` discovers documents and extracts their content in one call
- files that fail extraction (e.g. invalid encoding) are skipped
- Each document result includes its content ( or`None`) and an `extraction_error` field explaining any failure
- Fully covered by an automated test suite

No text processing (tokenization, normalization), indexing, or search functionality exists yet.

**Day 4 — Text Processing**

- `tokenize(text)` converts raw text into a clean list of lowercase words
- Strips leading/trailing punctuation from each word without touching internal punctuation (e.g. contractions)
- Filters out empty results (e.g. from tokens that were pure punctuation)
- `load_documents()` now includes a `tokens` field for each successfully extracted document
- Fully covered by an automated test suite

No indexing or search functionality exists yet.

**Day 5 — Index Construction & Entry Point**

- `build_index(documents)` builds an inverted index: a mapping from each word to the list of document paths containing it
- Skips documents that failed extraction (`tokens: None`)
- `main.py` provides a runnable entry point: prompts for a folder path, runs the full pipeline (discovery → extraction → tokenization → indexing), and prints a summary
- Handles invalid folder paths with friendly error messages instead of crashing
- Fully covered by an automated test suite, including tests for `input()`/`print()`-driven code

No search interface or result ranking exists yet — the index can be built and inspected, but there's no way to query it with a search term.

## Architecture

Day 1 built a single function, `discover_documents(folder_path)`, that:

1. Validates the given path exists and is a directory
2. Recursively walks the directory
3. Filters for supported file extensions
4. Collects metadata into a dictionary per file
5. Returns a list of these dictionaries

Day 2 added a second, independent function, `extract_text(file_path)`, that:

1. Reads a file's full text content
2. Relies on Python's built-in file-reading errors for missing files/directories
3. Raises a clear error if the file can't be decoded as text

Day 3 connected the two with `load_documents(folder_path)`, which:

1. Calls `discover_documents()` to find candidate files
2. Calls `extract_text()` on each one
3. Adds `content` and `extraction_error` fields to each document's record
4. Skips files that fail extraction instead of stopping the whole run

No classes, no external frameworks — just plain functions and Python's standard library.

Day 4 added a third function, `tokenize(text)`, that:

1. Splits text into words on whitespace
2. Strips leading/trailing punctuation from each word
3. Lowercases every word
4. Filters out any resulting empty tokens

`load_documents()` now calls `tokenize()` on successfully extracted content, adding a `tokens` field to each document. When extraction fails, `tokens` is set to `None`, consistent with `content`.

Day 5 added `build_index(documents)`, which:

1. Takes the list of documents produced by `load_documents()`
2. Skips any document with `tokens: None`
3. Builds a dictionary mapping each word to the list of document paths containing it

`build_index()` is intentionally kept separate from `load_documents()` — it operates on the full collection of documents at once (unlike per-document steps like extraction/tokenization), so it's composed at the call site rather than merged into the pipeline function.

`main.py` ties everything together as the project's entry point — prompting for a folder path and running the complete pipeline end-to-end.

Day 6 added `search(query, index)`, which:

1. Tokenizes the query using the same `tokenize()` function used for documents
2. Looks up each query word in the index, using `.get()` to safely handle words never seen before
3. Computes the intersection of all matching document sets — a document must contain every query word to match

`main.py` now chains all six stages together: prompt for a folder → discover → extract → tokenize → index → prompt for a query → search → display results.

## Technology Stack

- **Python 3** — standard library (`pathlib`) is sufficient for file discovery and metadata; no external dependencies needed for this part of the project
- **pytest** — for writing and running automated tests using plain functions, without requiring class-based test structure

## Project Structure

```
personal-search-engine/
├── .gitignore              # Files/folders Git should not track
├── requirements.txt        # Python package dependencies
├── discover.py             # Document discovery logic
├── extract.py              # Text extraction logic
├── process.py              # Text tokenization/processing logic
├── pipeline.py             # Combines discovery + extraction + processing
├── index.py                # Inverted index construction
├── search.py               # Query-based document search
├── main.py                 # Entry point: full interactive search tool
├── test_discover.py        # Automated tests for discover.py
├── test_extract.py         # Automated tests for extract.py
├── test_process.py         # Automated tests for process.py
├── test_pipeline.py        # Automated tests for pipeline.py
├── test_index.py           # Automated tests for index.py
├── test_search.py          # Automated tests for search.py
├── test_main.py            # Automated tests for main.py
└── example_documents/      # Sample files used to demo the pipeline
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

Run the program, enter a folder to index, then enter a search query:

```bash
python3 main.py
```


Multi-word queries require every word to appear in a document to count as a match (e.g. "example markdown" only matches documents containing both words).

**Known limitation:** Running against a folder that contains this project's own `venv/` or `.git/` directories (e.g. the project root itself) will also pick up unrelated files from those folders, since recursive search doesn't currently exclude them. Point it at a dedicated documents folder to avoid this.

## Testing

Run the full test suite with:

```bash
pytest
```

Tests cover:

**Discovery (`test_discover.py`)**
- Discovery of supported file types (`.txt`, `.md`)
- Unsupported files being correctly ignored
- Empty directories returning no results
- Nested directories being searched recursively
- Invalid directory paths raising appropriate errors

**Extraction (`test_extract.py`)**
- Reading a file's exact text content
- Reading an empty file
- Missing files and directories raising the correct built-in errors
- Files with invalid encoding raising a clear custom error

**Pipeline (`test_pipeline.py`)**
- Successfully extracted documents include their content and tokens
- Failed extractions are recorded with an error instead of crashing (content and tokens both `None`)
- One bad file doesn't prevent other files from being processed

**Processing (`test_process.py`)**
- Splitting text on whitespace
- Stripping punctuation from words
- Lowercasing words
- Filtering out empty tokens
- Handling empty input text

**Index (`test_index.py`)**
- A word appearing in multiple documents is correctly mapped to all of them
- A word appearing in a single document maps only to that one
- Documents with failed extraction (`tokens: None`) are skipped

**Search (`test_search.py`)**
- A single-word query returns all documents containing that word
- A multi-word query only returns documents containing every word (AND-matching)
- A query word absent from the index returns no results
- An empty query returns no results

**Main (`test_main.py`)**
- Running the full program end-to-end with a simulated folder path and search query produces the expected results

## Roadmap

**DONE**
- Document discovery and metadata collection (local files, `.txt`/`.md`)
- Recursive directory search
- Invalid input handling for discovery
- Text extraction from individual files
- Text extraction error handling (missing files, bad encoding)
- Combined discovery + extraction pipeline with graceful failure handling
- Text tokenization (splitting, punctuation stripping, lowercasing, empty-token filtering)
- Inverted index construction
- Runnable entry point (`main.py`) accepting any folder path
- Search functionality with multi-word AND-matching
- Automated test suite across all modules, including input/output-driven code

**PLANNED**
- Ranking of search results by relevance
- Basic web page crawling and keyword search
- Machine learning / NLP-based ranking improvements

## Learning

**Day - 1**
- How file structure works.
- Using `pathlib` to extract information about a particular directory
- Automated tests in python using pytest

**Day - 2**
- How try/except works in python
- How to write and read a file using pathlib
- Separation of Concerns

**Day - 3**
- combining two files and their functions
- python shell

**Day - 4**
- Tokenization
- Pythons in built string library 
- String methods

**Day - 5**
- More about dictionaries and lists
- continue and break
- monkeypatch and lambda function

**Day - 6**
- Sets in python and operations