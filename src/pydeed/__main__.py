import settings
import query, ofile

odir = settings.pars['data_dir']
o2dir = odir + 'saved_pages/'
ofile.mkdir(odir)
ofile.mkdir(o2dir)

def main():
    query.query_newjob_index(npage = 2)
    f_dat = odir + 'index.txt'
    dat = ofile.LoadIndex(f_dat)
    for ijob in range(dat.njobs):
        job = dat.jobs[ijob]
        try:
            query.query_job(job)
        except:
            pass
    return dat

if __name__ == '__main__':
    a = main()
    d = a.data
