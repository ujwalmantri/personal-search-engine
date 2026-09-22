import math
from rank import rank

def test_ranks_by_tfidf_score():
    index = {
        "hello": {"doc1.txt": 3, "doc2.txt": 1},
    }

    results = rank(["hello"], {"doc1.txt", "doc2.txt"}, index, total_documents=3)

    idf = math.log(3/2)

    assert results == [("doc1.txt", 3 * idf), ("doc2.txt", 1 * idf)]

def test_sums_tfidf_scores_across_multiple_query_words():
    index = {
        "hello": {"doc1.txt": 3, "doc2.txt": 1},
        "world": {"doc1.txt": 3},
    }

    results = rank(["hello", "world"], {"doc1.txt"}, index, total_documents=2)

    idf_hello = math.log(2/2)
    idf_world = math.log(2/1)
    expected_score = (2 * idf_hello) + (3 * idf_world)

    assert results == [("doc1.txt", expected_score)]

def test_empty_matching_paths_returns_empty():
    index = {"hello": {"doc1.txt": 1}}

    results = rank(["hello"], set(), index, total_documents=1)

    assert results == []