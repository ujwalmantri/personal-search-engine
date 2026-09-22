import pytest
from web import fetch_page
from web import extract_text_from_html


def test_extracts_text_from_html():
    html = "<html><body><h1>Hello</h1><p>World</p></body></html>"

    text = extract_text_from_html(html)

    assert "Hello" in text
    assert "World" in text

class FakeResponse:
    def __init__(self, text, status_code):
        self.text = text
        self.status_code = status_code

    def raise_for_status(self):
        if self.status_code >= 400:
            raise Exception(f"HTTP {self.status_code}")


def test_fetch_page_returns_text(monkeypatch):
    def fake_get(url):
        return FakeResponse("<html><body>Hello</body></html>", 200)

    monkeypatch.setattr("web.requests.get", fake_get)

    result = fetch_page("https://example.com")

    assert result == "<html><body>Hello</body></html>"


def test_fetch_page_raises_on_error_status(monkeypatch):
    def fake_get(url):
        return FakeResponse("Not Found", 404)

    monkeypatch.setattr("web.requests.get", fake_get)

    with pytest.raises(Exception):
        fetch_page("https://example.com/missing")
