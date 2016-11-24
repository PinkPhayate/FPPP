# get changedLOC
def getChengedLOC(curr, prev):
    """
    @param list of file1 curr
    @param list of file2 prev
    """
    changedLOC= 0
    for line in difflib.context_diff(curr, prev, fromfile='hoge.txt',tofile='fuga.txt'):
        isE = re.search("^\!",buf)
        if isE is not None :
            changedLOC += 1
    return changedLOC




# get addLOC and deletedLOC
def getAddDeleteLOC(curr, prev):
    """
    @param list of file1 curr
    @param list of file2 prev
    """
    addedLOC = 0   # +
    deletedLOC = 0   # -

    for buf in difflib.ndiff(curr, prev):
        isP = re.search("^\+",buf)
        if isP is not None :
            addedLOC += 1
        isM = re.search("^\-",buf)
        if isM is not None :
            deletedLOC += 1
            
    return addedLOC, deletedLOC
