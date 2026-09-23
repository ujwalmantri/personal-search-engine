import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, urlunparse

def fetch_page(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def extract_text_from_html(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text(separator="\n")

def extract_links(html, base_url):
    soup = BeautifulSoup(html, "html.parser")
    links = []
    for tag in soup.find_all("a"):
        href = tag.get("href")
        if href:
            absolute_url = urljoin(base_url, href)
            links.append(absolute_url)
    return links

def normalize_url(url):
    parsed = urlparse(url)
    return urlunparse(parsed._replace(fragment=""))

if __name__ == "__main__":
    html = fetch_page("https://example.com")
    text = extract_text_from_html(html)
    print(text)