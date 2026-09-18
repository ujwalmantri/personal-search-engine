from process import tokenize

def test_splits_on_whitespace():
    assert tokenize("hello world") == ["hello", "world"]

def test_strips_punctuation():
    assert tokenize("Hello, World!") == ["hello", "world"]

def test_lowercase_words():
    assert tokenize("HELLO, World!") == ["hello", "world"]

def test_filters_empty_tokens():
    assert tokenize("Hello -- World!") == ["hello", "world"]

def test_empty_string_returns_empty_list():
    assert tokenize("") == []