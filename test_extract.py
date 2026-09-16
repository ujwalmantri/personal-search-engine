import pytest
from extract import extract_text

def test_extracts_text_from_file(tmp_path):
    file_path = tmp_path / "sample.txt"
    file_path.write_text("Hello, World!")

    result = extract_text(file_path)

    assert result == "Hello, World!"

def test_extract_empty_string_from_empty_file(tmp_path):
    file_path = tmp_path / "empty.txt"
    file_path.write_text("")

    result = extract_text(file_path)

    assert result == ""

def test_missing_file_raises_error(tmp_path):
    missing_path = tmp_path / "does_not_exist.txt"

    with pytest.raises(FileNotFoundError):
        extract_text(missing_path)

def test_directory_raises_error(tmp_path):
    with pytest.raises(IsADirectoryError):
        extract_text(tmp_path)

def test_invalid_encoding_raises_value_error(tmp_path):
    file_path = tmp_path /"bad_encoding.txt"
    file_path.write_bytes(b"\xff\xfe\x00\x01")

    with pytest.raises(ValueError):
        extract_text(file_path)