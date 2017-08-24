import sys
import os

DEFAULTRUNNOW=True

class BorkenDirectory():

    path = ""
    dirListing = None

    def __init__(self, path, runNow=DEFAULTRUNNOW, eventDrivenWatch=False, pollDrivenWatch=False):
        self.path = path
        self.runNow = runNow 
        if self.runNow:
            self.run()

    def run(self):
        rootDir = self.path
        return self._run(rootDir)

    def pprint(self):
        if self.dirListing != None:
            for (k, v) in self.dirListing.iteritems():
                print k,
                ranOnce=False
                for i in v:
                    if ranOnce == False:
                       print ": ",
                    ranOnce=True
                    print "%s,"%(i),


                print ""

    def rootDict(self):
        return self.dirListing

    def _run(self, rootDir):
        dirListing = {}
        for dirName, subdirList, fileList in os.walk(rootDir):
            dirListing.setdefault(dirName,[])
            for fname in fileList:
                dirListing.setdefault(dirName,[]).append(fname)
                # Remove the first entry in the list of sub-directories
                # if there are any sub-directories present
                if len(subdirList) > 0:
                    del subdirList[0]
        self.dirListing = dirListing

    def __str__(self):
        return self.path

