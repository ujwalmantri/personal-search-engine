from discover import discover_documents
from extract import extract_text
from process import tokenize

def load_documents(folder_path):
    documents = discover_documents(folder_path)
    for doc in documents:
        try:
            doc["content"] = extract_text(doc["path"])
            doc["extraction_error"] = None
            doc["tokens"] = tokenize(doc["content"])
        except (ValueError, UnicodeDecodeError) as error:
            doc["content"] = None
            doc["extraction_error"] = str(error)
            doc["tokens"] = None

    return documents

if __name__ == "__main__":
    results = load_documents("example_documents")
    for doc in results:
        print(doc["name"], "-> tokens:", doc["tokens"])