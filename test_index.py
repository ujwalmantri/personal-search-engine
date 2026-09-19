from index import build_index

def test_word_appears_in_multiple_documents():
    documents = [
        {"path": "doc1.txt", "tokens": ["hello", "world"]},
        {"path": "doc2.txt", "tokens": ["hello", "there"]},
    ]

    index = build_index(documents)

    assert index["hello"] == ["doc1.txt", "doc2.txt"]

def test_word_appears_single_document():
    documents = [
        {"path": "doc1.txt", "tokens": ["hello", "world"]},
        {"path": "doc2.txt", "tokens": ["goodbye"]},
    ]

    index = build_index(documents)

    assert index["world"] == ["doc1.txt"]

def test_skips_documents_with_none_tokens():
    documents = [
        {"path": "doc1.txt", "tokens": ["hello"]},
        {"path": "doc2.txt", "tokens": None},
    ]

    index = build_index(documents)

    assert index == {"hello": ["doc1.txt"]}