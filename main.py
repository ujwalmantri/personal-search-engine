from pipeline import load_documents
from index import build_index

def main():
    folder_path = input("Enter the folder path to search: ")
    try:
        documents = load_documents(folder_path)
    except FileNotFoundError:
        print(f"Error: '{folder_path}' does not exist.")
        return
    except NotADirectoryError:
        print(f"Error: '{folder_path}' is not a dirctory.")
        return
    
    index = build_index(documents)

    print(f"\nDiscovered and processed {len(documents)} documents.")
    print(f"Index contains {len(index)} unique words.\n")

    for word, paths in index.items():
        print(f"{word}: {paths}")

if __name__ == "__main__":
    main()