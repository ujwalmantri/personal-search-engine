from crawler import crawl


def test_crawl_respects_max_pages(monkeypatch):
    fake_pages = {
        "https://a.com": "<html><body><a href='https://b.com'>B</a></body></html>",
        "https://b.com": "<html><body><a href='https://c.com'>C</a></body></html>",
        "https://c.com": "<html><body>No more links</body></html>",
    }

    def fake_fetch_page(url):
        return fake_pages[url]

    monkeypatch.setattr("crawler.fetch_page", fake_fetch_page)
    monkeypatch.setattr("crawler.time.sleep", lambda seconds: None)

    pages = crawl("https://a.com", max_pages=2, max_depth=5)

    assert len(pages) == 2

def test_crawl_respects_max_depth(monkeypatch):
    fake_pages = {
        "https://a.com": "<html><body><a href='https://b.com'>B</a></body></html>",
        "https://b.com": "<html><body><a href='https://c.com'>C</a></body></html>",
        "https://c.com": "<html><body>No more links</body></html>",
    }

    def fake_fetch_page(url):
        return fake_pages[url]

    monkeypatch.setattr("crawler.fetch_page", fake_fetch_page)
    monkeypatch.setattr("crawler.time.sleep", lambda seconds: None)

    pages = crawl("https://a.com", max_pages=10, max_depth=0)

    urls = [page["url"] for page in pages]
    assert urls == ["https://a.com"]


def test_crawl_skips_failed_pages(monkeypatch):
    fake_pages = {
        "https://a.com": "<html><body><a href='https://broken.com'>Broken</a><a href='https://c.com'>C</a></body></html>",
        "https://c.com": "<html><body>Fine</body></html>",
    }

    def fake_fetch_page(url):
        if url == "https://broken.com":
            raise Exception("Simulated failure")
        return fake_pages[url]

    monkeypatch.setattr("crawler.fetch_page", fake_fetch_page)
    monkeypatch.setattr("crawler.time.sleep", lambda seconds: None)

    pages = crawl("https://a.com", max_pages=10, max_depth=5)

    urls = [page["url"] for page in pages]
    assert "https://broken.com" not in urls
    assert "https://c.com" in urls