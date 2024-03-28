import settings, ofile, parser
from sltool.webpage import get_page, save_page, url2gurl

odir = settings.pars['data_dir']

q = 'data'
l = 'Maryland'
url = url2gurl(q, l)
t = get_page(url, wait_time=1)
save_page(t, odir+'bar.html')

jobs, njobs = parser.split_index_jobs(t)
f_out = odir+'p1.txt'
outfile = ofile.IndexFile(f_out)
for job in jobs:
    outfile.separate()
    ## job title
    title = parser.index_title(job)
    outfile.append(title)
    ## company name
    company = parser.index_company(job)
    outfile.append(company)
    ## location
    location = parser.index_location(job)
    print(location)
    
    
    
    
