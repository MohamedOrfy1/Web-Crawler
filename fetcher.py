import aiohttp
import asyncio

class PageFetcher:
    def __init__(self):
        self.session = None

    async def _init_session(self):
        if self.session is None:
            timeout = aiohttp.ClientTimeout(total=10)
            self.session = aiohttp.ClientSession(timeout=timeout)

    async def fetch(self, url):
        await self._init_session()
        try:
            async with self.session.get(url, headers={"User-Agent": "SimpleCrawler/1.0"}) as response:
                if response.status == 200 and 'text/html' in response.headers.get('Content-Type', ''):
                    html = await response.text()
                    return html, response.status
                else:
                    return None, response.status
        except Exception as e:
            print(f"[ERROR] Failed to fetch {url}: {e}")
            return None, None

    async def close(self):
        if self.session:
            await self.session.close()
