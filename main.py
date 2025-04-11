import asyncio
from crawler import Crawler
from db import PageDatabase

async def main():
    seed_url = "https://example.com"
    max_depth = 2
    max_pages = 50

    # Initialize the database
    db = PageDatabase()

    # Initialize and start the crawler
    crawler = Crawler(seed_url=seed_url, max_depth=max_depth, max_pages=max_pages, db=db)
    await crawler.run()

    # Close the database connection
    db.close()

if __name__ == "__main__":
    asyncio.run(main())
