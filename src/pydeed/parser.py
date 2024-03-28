import re
from bs4 import BeautifulSoup

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

def remove_html_tags(text):
    soup = BeautifulSoup(text, features="html.parser")
    cleaned_text = soup.get_text()
    return cleaned_text


def index_company(job):
    soup = BeautifulSoup(job, features="html.parser")
    r = soup.find('span', {'data-testid':'company-name'})
    r2 = remove_html_tags(str(r))
    return r2

