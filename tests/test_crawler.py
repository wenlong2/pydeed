import pytest
from pydeed.crawler import IndeedCrawler

def test_crawler():
    crawler = IndeedCrawler()
    results = crawler.crawl("python developer", "remote", num_pages=1)
    assert isinstance(results, list)
