 import difflib, re
 import module
 import file_operation as fo

def getProcessMetrics(mod, prev_filename):

    curr_filename = mod.filename
    totalLOC = mod.LOC

    # convert to list
    curr = fo.readFile(filename=curr_filename)
    prev = fo.readFile(filename=prev_filename)

    # measure metrics
    addedLOC, deletedLOC = getAddDeleteLOC(curr, prev)
    changedLOC = getChengedLOC(curr, prev)

    # calculate metrics
    churnedLOC = addedLOC + changedLOC

    # injection metrics
    mod.M1 = churnedLOC / totalLOC
    mod.M2 = deletedLOC / totalLOC
    mod.M6 = churnedLOC + deletedLOC
    mod.M7 = churnedLOC / deletedLOC

    return mod
    
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
