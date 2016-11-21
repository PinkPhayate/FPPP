class Module(object):
    def __init__(self, filename):
         self.filename = filename
         self.LOC = int()
         self.TChar = int()
         self.churnMetrics = float()
         self.relativeChrun = float()
         self.deletredChurn = float()
         self.ncdChurn = float()
         self.isNew = 0

    def printfilename():
        print self.filenme

    # def getLoc():
    #     # self.LOC = sum(1 for line in open( self.filename ))
    #     # return self.LOC
    #     return sum(1 for line in open( self.filename ))
