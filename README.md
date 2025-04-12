# Web Crawler

A Python-based web crawler that efficiently extracts and processes web pages using asynchronous HTTP requests and BeautifulSoup for parsing.

## Features

- Asynchronous web page fetching using `aiohttp`
- HTML parsing and link extraction using `BeautifulSoup4`
- Database storage for crawled data
- Title extraction from web pages
- URL normalization and filtering
- Efficient link processing

## Project Structure

- `main.py` - Entry point of the application
- `crawler.py` - Main crawler implementation
- `fetcher.py` - Asynchronous HTTP fetching module
- `extractor.py` - HTML parsing and link extraction
- `db.py` - Database operations
- `utils.py` - Utility functions
- `crawler.db` - SQLite database file

## Requirements

- Python 3.7+
- aiohttp
- beautifulsoup4
- lxml

## Installation

1. Clone the repository:
```bash
git clone https://github.com/MohamedOrfy1/Web-Crawler
cd web-crawler
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the crawler using:
```bash
python main.py
```

## Components

### LinkExtractor
The `LinkExtractor` class handles:
- Extracting page titles
- Finding and normalizing links
- Filtering valid HTTP/HTTPS URLs

### Fetcher
The `Fetcher` class manages:
- Asynchronous HTTP requests
- Connection pooling
- Response handling

### Database
The database module provides:
- Storage for crawled pages
- URL tracking
- Data persistence

## License

[Add your license here]

## Contributing

[Add contribution guidelines here] 
