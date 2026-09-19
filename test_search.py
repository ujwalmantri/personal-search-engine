from search import search 

def test_single_word_query():
    index = {
        "hello": ["doc1.txt", "doc2.txt"],
        "world": ["doc1.txt"],
    }

    results = search("hello", index)

    assert set(results) == {"doc1.txt", "doc2.txt"}
    # Here set is used because ordering doesnt matter in set
    # i.e. ['doc2.txt', 'doc1.txt'] == ['doc1.txt', 'doc2.txt'] -> List -> FALSE
    # but {'doc2.txt', 'doc1.txt'} == {'doc1.txt', 'doc2.txt'} -> Set -> TRUE

def test_multi_word_query_requires_all_words():
    index = {
        "hello": ["doc1.txt", "doc2.txt"],
        "world": ["doc1.txt"],
    }

    results = search("hello world", index)

    assert set(results) == {"doc1.txt"}

def test_word_not_in_index_returns_empty():
    index = {
        "hello": ["doc1.txt", "doc2.txt"],
        "world": ["doc1.txt"],
    }

    results = search("goodbye", index)

    assert results == []

def test_empty_query_returns_empty():
    index = {
        "hello": ["doc1.txt", "doc2.txt"],
        "world": ["doc1.txt"],
    }

    results = search("", index)

    assert results == []