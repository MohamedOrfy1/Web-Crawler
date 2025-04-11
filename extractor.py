from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


class LinkExtractor:
    def extract_title(self, html):
        soup = BeautifulSoup(html, "lxml")
        if soup.title:
            return soup.title.string.strip()
        return "No Title"

    def extract_links(self, html, base_url):
        soup = BeautifulSoup(html, "lxml")
        links = set()

        for tag in soup.find_all("a", href=True):
            href = tag["href"]
            full_url = urljoin(base_url, href)
            parsed = urlparse(full_url)

            # Filter: only HTTP/S links with netloc
            if parsed.scheme in ["http", "https"] and parsed.netloc:
                clean_url = parsed.geturl()
                links.add(clean_url)

        return list(links)
