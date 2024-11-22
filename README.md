# pydeed

**pydeed** is a Python package for crawling and filtering job posts from Indeed.

## Features
- Crawl job posts by keywords and location.
- Filter job posts with specific keywords.
- Save filtered job posts to local HTML files.

## Installation
```bash
brew install geckodriver (if not available or out-dated)
pip install git+https://github.com/wenlong2/pydeed
```

## Example
```python
import pydeed as pe

job_type = 'Python'
location = 'Remote'
num_pages = 2
exclude_keywords=["citizen", 'clearance'] ## case insensitive

crawler = pe.IndeedCrawler()
jobs = crawler.crawl(job_type, location, num_pages=num_pages)

kfilter = pe.JobFilter(exclude_keywords=exclude_keywords)
filtered_jobs = kfilter.filter(jobs)

saver = pe.JobSaver()
saver.save_to_html(filtered_jobs, "filtered_jobs.html", exclude_keywords=exclude_keywords)
```
