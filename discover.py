from pathlib import Path

def discover_documents(folder_path):

    folder = Path(folder_path)

    if not folder.exists():
        raise FileNotFoundError(f"No such directory: {folder_path}")

    if not folder.is_dir():
        raise NotADirectoryError(f"Not a directory: {folder_path}")

    supported_extensions = [".txt", ".md"]
    discovered_documents = []

    for item in folder.rglob("*"):
        if (
            item.is_file() and
            item.suffix in supported_extensions
        ):
            file_stats = item.stat()
            record = {
                "path": str(item), 
                "name": item.name,
                "extension": item.suffix,
                "size": file_stats.st_size,
                "modified_time": file_stats.st_mtime,
            }
            discovered_documents.append(record)

    return discovered_documents

if __name__ == "__main__":
    results = discover_documents("example_documents")
    print(results)