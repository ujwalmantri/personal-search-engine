import string

def tokenize(text):
    words = text.split()
    cleaned_words = []
    for word in words:
        cleaned = word.strip(string.punctuation).lower()
        if cleaned:
            cleaned_words.append(cleaned)
    return cleaned_words

if __name__ == "__main__":
    sample = "Hello, World !! This is a TEST message. "
    print(tokenize(sample))