from rank import rank

def test_ranks_by_total_frequency():
    index = {
        "hello": {"doc1.txt":3, "doc2.txt":1},
    }

    results = rank(["hello"], {"doc1.txt", "doc2.txt"}, index)

    assert results == [("doc1.txt", 3), ("doc2.txt", 1)]

def test_sums_scores_across_multiple_query_words():
    index ={
        "hello": {"doc1.txt":2},
        "world": {"doc1.txt":3},
    }

    results = rank(["hello", "world"], {"doc1.txt"}, index)

    assert results == [("doc1.txt", 5)]

def test_empty_matching_paths_returns_empty():
    index = {
          "hello": {"doc1.txt":2}
    }

    results = rank(["hello"], set(), index)

    assert results == []