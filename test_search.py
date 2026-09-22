import math
from search import search 

def test_single_word_query():
    index = {
        "hello": {"doc1.txt": 1, "doc2.txt": 1},
        "world": {"doc1.txt": 1},
    }

    results = search("hello", index, total_documents=2)

    paths = {path for path, score in results}

    assert paths == {"doc1.txt", "doc2.txt"}
    # Here set is used because ordering doesnt matter in set
    # i.e. ['doc2.txt', 'doc1.txt'] == ['doc1.txt', 'doc2.txt'] -> List -> FALSE
    # but {'doc2.txt', 'doc1.txt'} == {'doc1.txt', 'doc2.txt'} -> Set -> TRUE

def test_multi_word_query_requires_all_words():
    index = {
        "hello": {"doc1.txt": 1, "doc2.txt": 1},
        "world": {"doc1.txt": 1},
    }

    results = search("hello world", index, total_documents=2)

    idf_hello = math.log(2/2)
    idf_world = math.log(2/1)
    expected_score = (1 * idf_hello) + (1 * idf_world)

    assert results == [("doc1.txt", expected_score)]

def test_word_not_in_index_returns_empty():
    index = {
        "hello": {"doc1.txt":1, "doc2.txt":1},
        "world": {"doc1.txt":1},
    }

    results = search("goodbye", index, total_documents=2)

    assert results == []

def test_empty_query_returns_empty():
    index = {
        "hello": ["doc1.txt", "doc2.txt"],
        "world": ["doc1.txt"],
    }

    results = search("", index, total_documents=2)

    assert results == []