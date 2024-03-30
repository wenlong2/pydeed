from . import settings
from . import query, ofile
from .filter import filter_jobs
import argparse

odir = settings.pars['data_dir']
o2dir = odir + 'saved_pages/'
ofile.mkdir(odir)
ofile.mkdir(o2dir)

def download_jobs(*args, **kwargs):
    query.query_newjob_index(*args, **kwargs)
    f_dat = odir + 'index.txt'
    dat = ofile.LoadIndex(f_dat)
    for ijob in range(dat.njobs):
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
        filter_jobs(
            include=args.withkey,
            exclude=args.exclude,
            infilename=args.infile,
            outfilename=args.outfile)

if __name__ == '__main__':
    pars = argparse.ArgumentParser()
    pars.add_argument('-j', '--job',
                          help='job type:\n"get" to download recent posts from indeed.com\n"filter" to filter the downloaded posts\nExample: python3 -m pydeed -j get -k Python -l California -n 5\npython3 -m pydeed -j filter -e \'TS/SCI,US citizen,security clearance\'',
                          required=True)
    pars.add_argument('-k', '--keyword', help='job title keyword to be searched')
    pars.add_argument('-l', '--location', help='job location')
    pars.add_argument('-n', '--npage', help='number of pages to search')
    pars.add_argument('-o', '--outfile', help='output file name')
    pars.add_argument('-i', '--infile', help='input file name')
    pars.add_argument('-w', '--withkey', help='with keywords. If there are multiple keywords, separate them with coma ","')
    pars.add_argument('-e', '--exclude', help='excluded keywords. If there are multiple keywords, separate them with coma ","')
    args = pars.parse_args()
    main(args)
