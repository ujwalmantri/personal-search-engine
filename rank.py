def rank(query_words, matching_paths, index):
    scores = {}

    for path in matching_paths:
        total = 0
        for word in query_words:
            total += index[word][path]
        scores[path] = total

    ranked = sorted(scores.items(), key=lambda item:item[1], reverse=True)
    
    return ranked