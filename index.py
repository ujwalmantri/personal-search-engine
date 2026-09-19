def build_index(documents):
    index = {}

    for doc in documents:
        if doc["tokens"] is None:
            continue

        for token in doc["tokens"]:
            if token not in index:
                index[token] = []
            index[token].append(doc["path"])

    return index

if __name__ == "__main__":
    from pipeline import load_documents

    documents = load_documents("example_documents")
    index = build_index(documents)
    print(index)