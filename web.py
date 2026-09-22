import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def extract_text_from_html(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text(separator="\n")

if __name__ == "__main__":
    html = fetch_page("https://example.com")
    text = extract_text_from_html(html)
    print(text)