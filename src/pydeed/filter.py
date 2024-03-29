from . import settings, ofile

odir = settings.pars['data_dir']
o2dir = odir + 'saved_pages/'
ofile.mkdir(odir)
ofile.mkdir(o2dir)

def filter_jobs(
            include='', exclude='',
            infilename='index.txt',
            outfilename='filtered.html'):
    if infilename is None:
        infilename = 'index.txt'
    if outfilename is None:
        outfilename = 'filtered.html'
    key_include = expand_key(include)
    key_exclude = expand_key(exclude)
    print('Must include: ', key_include)
    print('Must exclude: ', key_exclude)
    f_in = odir + infilename
    dat = ofile.LoadIndex(f_in)
    out = ofile.IndexFile(odir + outfilename)
    for ijob in range(dat.njobs):
        job = dat.jobs[ijob]
        jid = job['Download_ID']
        f_des = o2dir + jid + '.txt'
        if check_keyword(f_des, key_include, key_exclude):
            add_job(out, job)
    return 0

def add_job(out, job):
    link = job['Indeed_link']
    out.append('<h3>'+job['Title']+'</h3>')
    out.append(job['Company']+', ')
    out.append(job['Location']+' <br>')
    out.append(job['Other_info']+' <br>')
    out.append(job['Post_date']+' ')
    out.append('<a href="'+link+'" target="_blank"> Indeed link </a>')
    return 0

def expand_key(k):
    if k:
        return k.split(',')
    else:
        return []
    
def check_keyword(f, k_in, k_ex):
    r = False
    txt = open(f).read()
    if len(k_in) == 0:
        r = True
    else:
        for k in k_in:
            if k == '':
                r = True
                break
            if k in txt:
                r = True
                break
    if len(k_ex) == 0:
        return True
    for k in k_ex:
        if k in txt:
            r = False
            break
    return r
