import difflib, re
import module
def getProcessMetrics(mod, prev_filename):

    curr_filename = mod.filename
    # curr_filename = '/Users/phayate/src/ApacheDerby/10.11/tools/release/jirasoap/src/main/java/org/apache/derbyBuild/jirasoap/FilteredIssueLister.java'
    # prev_filename = '/Users/phayate/src/ApacheDerby/10.12/tools/release/jirasoap/src/main/java/org/apache/derbyBuild/jirasoap/FilteredIssueLister.java'
    addedLine, deletedLine, modifiedLine = getDiff(curr_filename, prev_filename)

    # pur metrics on the module
    mod.churnMetrics = addedLine + modifiedLine
    mod.DeletredChurn = float()
    if mod.LOC < 1 :
         mod.LOC = mod.getLoc()
    mod.relativeChrun = (addedLine + modifiedLine)/ mod.LOC
    mod.deletredChurn = (addedLine + modifiedLine)/ mod.LOC
    if deletedLine < 1:
        mod.ncdChurn = 0
    else:
        mod.ncdChurn = ( addedLine+modifiedLine) / deletedLine

    return mod



def getDiff(file1, file2):
    """
    @param file1 curr
    @param file2 prev
    """
    f = open(file1, 'r')
    prev_text = []
    for line in f:
        prev_text.append(line)
    f.close()

    f = open(file2, 'r')
    curr_text = []
    for line in f:
        curr_text.append(line)
    f.close()

    p = 0   # +
    m = 0   # -
    q = 0   # ?
    for buf in difflib.ndiff(curr_text, prev_text):
        isP = re.search("^\+",buf)
        if isP is not None :
            p += 1
        isM = re.search("^\-",buf)
        if isM is not None :
            m += 1
        isQ = re.search("^\?",buf)
        if isQ is not None :
            q += 1

    addedLine = p - q
    deletedLine = m-q
    modifiedLine = q

    if addedLine < 0:
        print 'addedLine<0: ' + file1
        addedLine = 0
    if deletedLine < 0:
        print 'deletedLine<0: ' + file1
        deletedLine = 0

    return addedLine, deletedLine, modifiedLine







''' test'''
#  no diff
# curr_filename = '/Users/phayate/src/ApacheDerby/10.11/tools/release/jirasoap/src/main/java/org/apache/derbyBuild/jirasoap/FilteredIssueLister.java'
# prev_filename = '/Users/phayate/src/ApacheDerby/10.12/tools/release/jirasoap/src/main/java/org/apache/derbyBuild/jirasoap/FilteredIssueLister.java'
# getDiff(curr_filename, prev_filename)

# getDiff('test-module1.java', 'test-module3.java')
# getDiff('test-module1.java', 'test-module2.java')
def testGetDiff():
    addedLine, deletedLine, modifiedLine = getDiff('test-data/test-module4.txt', 'test-data/test-module5.txt')
    # expect -> 0,1,0
    print addedLine, deletedLine, modifiedLine
    # actual -> 1,0,0

#    testGetDiff()
