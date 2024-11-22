import time
import random
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import warnings

warnings.filterwarnings("ignore")

class IndeedCrawler:
    def __init__(self, base_url="https://www.indeed.com/jobs"):
        self.base_url = base_url
        self.driver = None

    def _setup_driver(self):
        """Set up the Selenium WebDriver with Firefox."""
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")  # Run headless (without UI)
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        self.driver = webdriver.Firefox(options=options)

    def _scroll_page(self):
        """Simulate human scrolling to load more content."""
        for _ in range(random.randint(3, 5)):  # Scroll 3-5 times to load dynamic content
            self.driver.execute_script("window.scrollBy(0, 300);")
            time.sleep(random.uniform(0.2, 0.5))  # Random delay between scrolls

    def crawl(self, query, location, num_pages=1):
        """Crawl job postings based on search query and location."""
        jobs = []

        for page in range(num_pages):
            # Start the Selenium driver for new page
            self._setup_driver()
            params = {"q": query, "l": location, "start": str(int(page * 10)), 'sort': 'date'}
            url = self.base_url + "?" + "&".join([f"{key}={value}" for key, value in params.items()])
            self.driver.get(url)
            time.sleep(random.uniform(2,5))  # Random delay before scraping

            # Scroll to load more jobs dynamically
            self._scroll_page()

            # Parse job postings with BeautifulSoup
            soup = BeautifulSoup(self.driver.page_source, "html.parser")
            jobs.extend(self._parse_results(soup))

        self.driver.quit()
        return jobs

    def _parse_results(self, soup):
        """Parse job posts from the BeautifulSoup object."""
        job_posts = []
        job_cards = soup.find_all("div", class_="job_seen_beacon")
        for job_card in job_cards:
            try:
                title = job_card.find("h2", class_="jobTitle").get_text(strip=True)
                link = job_card.find("a", href=True)["href"]
                location = job_card.find("div", class_="company_location").get_text(strip=True)
                location = location.replace('InterImage','').replace('DataAnnotation4.0','')
                salary = job_card.find("div", class_="salary-snippet-container").get_text(strip=True) if job_card.find("div", class_="salary-snippet-container") else "n/a"
                days_posted = job_card.find('span', {'data-testid':'myJobsStateDate'}).get_text(strip=True) if job_card.find('span', {'data-testid':'myJobsStateDate'}) else "n/a"
                full_link = 'https://www.indeed.com'+link
                post_text = self.get_raw_text_of_post(full_link)
                job_posts.append({
                    "title": title,
                    "link": f"https://www.indeed.com{link}",
                    "location": location,
                    "salary": salary,
                    "days_posted": days_posted,
                    'text': post_text
                    })
                print('checked: '+title)
            except AttributeError:
                continue  # Skip if any attribute is missing

        return job_posts

    def get_raw_text_of_post(self, post_url):
        """Extract raw text of the job post from the job page URL."""
        self._setup_driver()
        self.driver.get(post_url)
        time.sleep(random.uniform(0.3, 0.5))  # Wait for the page to load

        # Extract job description from the individual job post page
        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        raw_text = soup.get_text(strip=True)

        self.driver.quit()
        return raw_text

# Usage Example
if __name__ == "__main__":
    crawler = IndeedCrawler()
    jobs = crawler.crawl("python developer", "remote", num_pages=2)
    for job in jobs:
        print(job["title"], job["link"])
