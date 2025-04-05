# GhostTrace DarkGPT

This container fuses WormGPT (LLM) with DarkBERT features for crawling and analyzing dark web content.

## Usage
- `docker build -t ghosttrace-darkgpt .`
- `docker run -it -p 11434:11434 ghosttrace-darkgpt`
- Inside container: `python3 /app/darkweb_crawler.py`
