import settings
import re
from bs4 import BeautifulSoup
from sltool.webpage import href2url

def split_index_jobs(t):
    uni_str1 = '<div class="cardOutline'
    uni_str2 = '</span><!--/'
    idx = [m.start() for m in re.finditer(uni_str1, t)]
    idx2 = [m.start() for m in re.finditer(uni_str2, t)]
    n = len(idx)
    jobs = []
    for i in range(len(idx)):
        ts = t[idx[i]:idx2[i]]
        jobs.append(ts)
    return jobs, n
    
def index_title(job):
    uni_str1 = '<span title="'
    uni_str2 = '" id="jobTitle-'
    title = job[(job.find(uni_str1) + len(uni_str1)):job.find(uni_str2)]
    return title

def remove_html_tags(text, delimiter=''):
    soup = BeautifulSoup(text, features="html.parser")
    cleaned_text = soup.get_text(delimiter)
    return cleaned_text


def index_company(job):
    soup = BeautifulSoup(job, features="html.parser")
    r = soup.find('span', {'data-testid':'company-name'})
    r2 = remove_html_tags(str(r))
    return r2

def index_location(job):
    soup = BeautifulSoup(job, features="html.parser")
    r = soup.find('div', {'data-testid':'text-location'})
    r2 = remove_html_tags(str(r))
    return r2

def index_meta(job):
    soup = BeautifulSoup(job, features="html.parser")
    r = soup.find('div', {'class':'jobMetaDataGroup'})
    r2 = remove_html_tags(str(r), delimiter='; ').replace(';  ; +;',' +')
    return r2

def index_date(job):
    soup = BeautifulSoup(job, features="html.parser")
    r = soup.find('span', {'data-testid':'myJobsStateDate'})
    r2 = remove_html_tags(str(r), delimiter='; ')
    return r2

def index_link(job):
    soup = BeautifulSoup(job, features="html.parser")
    r = soup.find('h2', {'class':'jobTitle'})
    r2 = get_href(str(r))
    return r2

def get_href(text):
    soup = BeautifulSoup(text, features="html.parser")
    r = []
    for a in soup.find_all('a', href=True):
        r.append(href2url(a['href']))
    return r

def trim_jobpage(t):
    uni_str1 = 'What Where Find Jobs'
    idx = t.find(uni_str1)
    r = t[idx+len(uni_str1):]
    uni_str2 = '&nbsp; Report job &nbsp;'
    idx = r.find(uni_str2)
    r2 = r[:idx]
    return r2
