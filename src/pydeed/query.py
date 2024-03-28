import settings, ofile, parser
from sltool.webpage import get_page, save_page, url2gurl

odir = settings.pars['data_dir']
o2dir = odir + 'saved_pages/'

def query_newjob_index(
        q = 'data', l = 'Maryland',
        npage = 2, outfilename='index.txt'):
    f_out = odir + outfilename
    outfile = ofile.IndexFile(f_out)
    for ipage in range(npage):
        print('Getting page '+str(ipage+1))
        start = 0
        if ipage > 0:
            start=ipage*10
        url = url2gurl(q, l, start=start)
        index_page = get_page(url, wait_time=1)
        save_page(index_page, o2dir+'p'+str(ipage+1)+'.html')
        format_page(index_page, ipage+1, outfile)
    return 0

def format_page(t, pagenum, outfile):
    jobs, njobs = parser.split_index_jobs(t)
    ijob = 1
    for job in jobs:
        outfile.separate()
        ## new job id
        jid = str(pagenum)+'-'+str(ijob)
        outfile.append('Download_ID: '+jid)
        ijob += 1
        ## job title
        title = parser.index_title(job)
        outfile.append('Title: '+title)
        ## company name
        company = parser.index_company(job)
        outfile.append('Company: '+company)
        ## location
        location = parser.index_location(job)
        outfile.append('Location: '+location)
        ## other info
        meta = parser.index_meta(job)
        outfile.append('Other_info: '+meta)
        ## date
        sdate = parser.index_date(job)
        outfile.append('Post_date: '+sdate)
        ## url link
        links = parser.index_link(job)
        for link in links:
            outfile.append('Indeed_link: '+link)
    return 0

def query_job(job):
    jid = job['Download_ID']
    link = job['Indeed_link']
    page = get_page(link, wait_time=1)
    page = parser.remove_html_tags(page, delimiter=' ')
    page = parser.trim_jobpage(page)
    f_out = o2dir + jid + '.txt'
    save_page(page, f_out)
    return 0
