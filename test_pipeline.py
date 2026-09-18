from pipeline import load_documents

def test_successful_extraction_has_content(tmp_path):
    (tmp_path / "sample.txt").write_text("Hello, World!")

    results = load_documents(tmp_path)

    assert len(results) == 1
    assert results[0]["content"] == "Hello, World!"
    assert results[0]["extraction_error"] is None

def test_failed_extraction_has_none_content(tmp_path):
    bad_file = tmp_path / "bad.txt"
    bad_file.write_bytes(b"\xff\xfe\x00\x01")

    results = load_documents(tmp_path)

    assert len(results) == 1
    assert results[0]["content"] is None
    assert results[0]["extraction_error"] is not None

def test_one_bad_file_does_not_block_others(tmp_path):
    (tmp_path / "good.txt").write_text("Readable content")
    (tmp_path / "bad.txt").write_bytes(b"\xff\xfe\x00\x01")

    results = load_documents(tmp_path)

    assert len(results) == 2

    contents = {doc["name"]: doc["content"] for doc in results}
    errors = {doc["name"]: doc["extraction_error"] for doc in results}

    assert contents["good.txt"] == "Readable content"
    assert errors["good.txt"] is None 

    assert contents["bad.txt"] is None
    assert errors["bad.txt"] is not None

def test_successful_extraction_includes_tokens(tmp_path):
    (tmp_path / "sample.txt").write_text("Hello, World!")

    results = load_documents(tmp_path)

    assert results[0]["tokens"] == ["hello", "world"]

def test_failed_extraction_has_none_tokens(tmp_path):
    bad_file = tmp_path / "bad.txt"
    bad_file.write_bytes(b"\xff\xfe\x00\x01")

    results = load_documents(tmp_path)

    assert results[0]["tokens"] is None
