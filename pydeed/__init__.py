"""
pydeed: A package for crawling and filtering Indeed job posts.

Modules:
- crawler: Handles web crawling from Indeed.
- filter: Filters job posts based on keywords.
- saver: Saves job posts to local HTML files.
"""

from .crawler import IndeedCrawler
from .filter import JobFilter
from .saver import JobSaver

__all__ = ["IndeedCrawler", "JobFilter", "JobSaver"]
