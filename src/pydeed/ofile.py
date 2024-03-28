import settings
import os

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
    
    
