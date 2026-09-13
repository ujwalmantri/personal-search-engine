from pathlib import Path

def discover_documents(folder_path):

    folder = Path(folder_path)
    supported_extensions = [".txt", ".md"]
    discovered_documents = []

    for item in folder.iterdir():
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
    results = discover_documents(".")
    print(results)