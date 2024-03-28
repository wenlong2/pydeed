from .. import settings
from selenium import webdriver
import time

def get_page(url, wait_time=1):
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(wait_time) ## to be improved
    html = driver.page_source
    driver.close()
    return html

def save_page(html, f_out):
    with open(f_out,'w') as h:
        h.write(html)
    return 0

def url2gurl(q='',l='',start=0):
    url_base = settings.pars['url_base']
    gurl = url_base + 'jobs?q='+q+'&l='+l+'&sort=date'
    if start > 0:
        gurl = gurl + '&start='+str(start)
    return gurl

def href2url(href):
    url_base = settings.pars['url_base2']
    url = url_base+href
    return(url)

