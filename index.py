from collections import Counter

def build_index(documents):
    index = {}

    for doc in documents:
        if doc["tokens"] is None:
            continue

        word_counts = Counter(doc["tokens"])

        for word, count in word_counts.items():
            if word not in index:
                index[word] = {}
            index[word][doc["path"]] = count

    return index

if __name__ == "__main__":
    from pipeline import load_documents

    documents = load_documents("example_documents")
    index = build_index(documents)
    print(index)