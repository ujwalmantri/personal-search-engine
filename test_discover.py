import pytest
from discover import discover_documents

def test_discovers_supported_files(tmp_path):
    (tmp_path / "sample.txt").write_text("Some text content")
    (tmp_path / "sample.md").write_text("# Some markdown content")
    results = discover_documents(tmp_path)
    names = [doc["name"] for doc in results]
    assert "sample.txt" in names
    assert "sample.md" in names

def test_ignore_unsupported_files(tmp_path):
    (tmp_path / "sample.py").write_text("print('Hello, World!')")
    results = discover_documents(tmp_path)
    names = [doc["name"] for doc in results]
    assert "sample.py" not in names

def test_empty_directory_returns_empty_list(tmp_path):
    results = discover_documents(tmp_path)
    assert results == []

def test_discovers_files_in_nested_directories(tmp_path):
    nested_folder = tmp_path / "subfolder"
    nested_folder.mkdir()
    nested_file = nested_folder / "nested.txt"
    nested_file.write_text("nested content")

    results = discover_documents(tmp_path)
    names = [doc["name"] for doc in results]
    assert "nested.txt" in names

def test_invalid_directory_raises_error():
    with pytest.raises(FileNotFoundError):
        discover_documents("this_folder_does_not_exist")