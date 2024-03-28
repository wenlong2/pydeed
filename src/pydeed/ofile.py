import settings
import os

def mkdir(path):
    try:
        os.makedirs(path)
        return True
    except FileExistsError:
        return True
    except Exception as e:
        print(f"Error while creating directory: {e}")
        return False
    
class IndexFile:
    
    def __init__(self, filename):
        self.filename=filename
        if os.path.exists(filename):
            print(filename+' already exists. It will be overwritten')
        with open(self.filename, 'w') as h:
            h.write('')
            
    def append(self, t):
        with open(self.filename, 'a') as h:
            h.write(t+'\n')
        return 0
    
    def separate(self):
        self.append('\n\n'+'-'*80+'\n\n')
        return 0
    
class LoadIndex:
    def __init__(self, filename):
        self.filename=filename
        if os.path.exists(filename):
            with open(self.filename, 'r') as h:
                self.data = h.readlines()
        else:
            print(filename+' does not exist. It will be overwritten')
        self.separate()
        
    def separate(self):
        data = self.data
        jobs = []
        sep = '-'*30
        for i in range(len(data)):
            if sep in data[i]:
                sub = data[(i+3):(i+11)]
                job = self.to_dict(sub)
                jobs.append(job)
                i = i + 10
        self.jobs = jobs
        self.njobs = len(jobs)
        return(data)
    
    def to_dict(self, s):
        d = {}
        for t in s:
            t = t.replace('\n','')
            if t:
                idx = t.find(': ')
                d[t[0:idx]] = t[idx+2:]
        return d
