from pathlib import Path

def extract_text(file_path):
    path = Path(file_path)
    try:
        return path.read_text()
    except UnicodeDecodeError:
        raise ValueError(f"Could not read '{file_path}' as text - it may not be a valid text file.")