import math

def rank(query_words, matching_paths, index, total_documents):
    scores = {}

    for path in matching_paths:
        total = 0
        for word in query_words:
            tf = index[word][path]
            idf = compute_idf(word, index, total_documents)
            total += tf * idf
        scores[path] = total

    ranked = sorted(scores.items(), key=lambda item:item[1], reverse=True)
    
    return ranked

def compute_idf(word, index, total_documents):
    documents_with_word = len(index.get(word, {}))
    if documents_with_word == 0:
        return 0
    return math.log(total_documents / documents_with_word)

if __name__ == "__main__":
    fake_index = {
        "common": {"a": 1, "b": 1, "c": 1},
        "rare": {"a":1},
        }

    print("IDF of 'common': ", compute_idf("common", fake_index, 3))
    print("IDF of 'rare': ", compute_idf("rare", fake_index, 3))
