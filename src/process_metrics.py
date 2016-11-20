def getProcessMetrics(mod, filename):
    prev_filename = '/Users/phayate/src/ApacheDerby/10.12/tools/release/jirasoap/src/main/java/org/apache/derbyBuild/jirasoap/FilteredIssueLister.java'
    f = open(filename, 'r')
    prev_text = []
    for line in f:
        prev_text.append(line)
    f = close()

    f = open(mod.filename, 'r')
    curr_text = []
    for line in f:
        curr_text.append(line)
    f = close()
