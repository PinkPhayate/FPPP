import module
def getProcuctMetrics(m):
    if type (m) !=  module.Module:
        return
    filename = m.filename
    f = open(filename, 'r')

    loc = 0
    tchar = 0
    cl = 0
    tcomm = 0
    mchar = 0
    dchar = 0
    isCommenting = False

    for line in f:

        # judge wheter be comment or not
        line_id = confirmComment(line)
        # if continuing to comment line
        if isCommenting:
            line_id = 0
            print isCommenting
        # if not comment
        if line_id == 20:
            # loc += 1
            # cl += 1
            tchar += len(line)
            dchar += len(line)

        # if be comment
        else:
            tcomm += 1
            mchar += 1

            # check status
            if line_id == 1:
                isCommenting = True
            if line_id == 2:
                isCommenting == False

    f.close()
    m.LOC = loc
    m.TChar = tchar
    m.CL = cl
    m.TComm = tcomm
    m.MChar = mchar
    m.DChar = dchar

    return m

def confirmComment(line):
    '''
    return code 0   ->  comment only one    //
    return code 1   ->  could find start of comment /*
    return code 2   ->  find  end of comment    */
    return code 20   ->  script without comment
    '''
    print lin
    if '//' in line:
        return 0
    elif '*/' in line:
        return 2
    elif '/*' in line:
        return 1
    return 20


''' test to get loc and tchar'''
def testGetProductMetrics():
    filename = '/Users/phayate/src/ApacheDerby/10.12/tools/release/jirasoap/src/main/java/org/apache/derbyBuild/jirasoap/FilteredIssueLister.java'
    mod = module.Module(filename)
    mod = getProcuctMetrics(mod)
    print mod.LOC
    print mod.TChar
    print mod.CL
    print mod.TComm
    print mod.MChar
    print mod.DChar
    print mod.M1
    print mod.M2
    print mod.M3
    print mod.M4
    print mod.M5
    print mod.M6
    print mod.M7
    print mod.M8


testGetProductMetrics()
