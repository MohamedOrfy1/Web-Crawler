import asyncio
from collections import deque
from urllib.parse import urlparse

from fetcher import PageFetcher
from extractor import LinkExtractor


class Crawler:
    def __init__(self, seed_url, max_depth, max_pages, db):
        self.seed_url = seed_url
        self.max_depth = max_depth
        self.max_pages = max_pages
        self.db = db

        self.visited = set()
        self.queue = deque()
        self.queue.append((seed_url, 0))

        self.fetcher = PageFetcher()
        self.extractor = LinkExtractor()

    async def run(self):
        pages_crawled = 0

        while self.queue and pages_crawled < self.max_pages:
            url, depth = self.queue.popleft()

            if url in self.visited or depth > self.max_depth:
                continue

            self.visited.add(url)

            print(f"[{depth}] Crawling: {url}")
            html, status = await self.fetcher.fetch(url)

            if html is None:
                continue

            title = self.extractor.extract_title(html)
            self.db.insert_page(url, title, status, depth)
            pages_crawled += 1

            links = self.extractor.extract_links(html, base_url=url)
            for link in links:
                if link not in self.visited:
                    self.queue.append((link, depth + 1))

        await self.fetcher.close()
