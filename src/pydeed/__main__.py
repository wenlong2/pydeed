from . import settings
from . import query, ofile
import argparse

odir = settings.pars['data_dir']
o2dir = odir + 'saved_pages/'
ofile.mkdir(odir)
ofile.mkdir(o2dir)

def download_jobs(*args, **kwargs):
    query.query_newjob_index(*args, **kwargs)
    f_dat = odir + 'index.txt'
    dat = ofile.LoadIndex(f_dat)
    for ijob in range(1):
        print('Retrieving '+str(ijob+1)+' out of '+str(dat.njobs)+' jobs.')
        job = dat.jobs[ijob]
        try:
            query.query_job(job)
        except:
            pass
    return dat

def main(args) -> None:
    if args.job == 'get':
        download_jobs(
            keyword=args.keyword,
            location=args.location,
            npage=args.npage,
            outfilename=args.outfile)
    if args.job == 'filter':
        print('todo')

if __name__ == '__main__':
    pars = argparse.ArgumentParser()
    pars.add_argument('-j', '--job',
                          help='download recent jobs from indeed.com',
                          required=True)
    pars.add_argument('-k', '--keyword', help='job title keyword to be searched')
    pars.add_argument('-l', '--location', help='job location')
    pars.add_argument('-n', '--npage', help='number of pages to search')
    pars.add_argument('-o', '--outfile', help='output file name')
    pars.add_argument('-i', '--include', help='included keywords. If there are multiple keywords, separate them with coma ","')
    pars.add_argument('-e', '--exclude', help='included keywords. If there are multiple keywords, separate them with coma ","')
    args = pars.parse_args()
    main(args)
