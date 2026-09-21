from process import tokenize
from rank import rank

def search(query, index):
    query_words = tokenize(query)

    if not query_words:
        return []

    matching_sets = []
    for word in query_words:
        doc_counts = index.get(word, {})
        matching_sets.append(set(doc_counts.keys()))

    result = matching_sets[0]
    for s in matching_sets[1:]:
        result = result & s

    ranked_results = rank(query_words, result, index)
    return ranked_results

if __name__ == "__main__":
    from pipeline import load_documents
    from index import build_index

    documents = load_documents("example_documents")
    index = build_index(documents)

    results = search("example", index)
    print("Results for 'example':", results)

    results = search("example markdown", index)
    print("Results for 'example markdown':", results)

    results = search("nonexsistentword", index)
    print("Results for 'nonexsistentword':", results)