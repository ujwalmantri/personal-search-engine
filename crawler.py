import time
from web import fetch_page, extract_links, extract_text_from_html, normalize_url

def crawl(start_url, max_pages=10, max_depth=2, delay=1):
    visited = set()
    to_visit = [(normalize_url(start_url), 0)]
    pages = []

    while to_visit and len(visited) < max_pages:
        url, depth = to_visit.pop(0)

        if url in visited:
            continue
        if depth > max_depth:
            continue

        try:
            html = fetch_page(url)
        except Exception as error:
            print(f"Skipping {url}: {error}")
            visited.add(url)
            continue

        visited.add(url)
        text = extract_links(html, url)
        pages.append({"url": url, "content": text})

        links = extract_links(html, url)
        for link in links:
            normalize_link = normalize_url(link)
            if normalize_link not in visited:
                to_visit.append((normalize_link, depth + 1))

        time.sleep(delay)

    return pages

if __name__ == "__main__":
    pages = crawl("https://github.com/ujwalmantri", max_pages=10, max_depth=3)
    for page in pages:
        print(page["url"])
