import difflib, re
def getProcessMetrics(mod, filename):
    if type (m) != 'module.Module':
        return
    # curr_filename = mod.filename
    curr_filename = '/Users/phayate/src/ApacheDerby/10.11/tools/release/jirasoap/src/main/java/org/apache/derbyBuild/jirasoap/FilteredIssueLister.java'
    prev_filename = '/Users/phayate/src/ApacheDerby/10.12/tools/release/jirasoap/src/main/java/org/apache/derbyBuild/jirasoap/FilteredIssueLister.java'
    getDiff(curr_filename, prev_filename)

def getDiff(file1, file2):
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

    newline = 0

    for buf in difflib.ndiff(curr_text, prev_text):
        isChange = re.search("^\+",buf)
        print buf
        # if isChange != None:
        #     print buf

	#   print buf



''' test'''
#  no diff
# curr_filename = '/Users/phayate/src/ApacheDerby/10.11/tools/release/jirasoap/src/main/java/org/apache/derbyBuild/jirasoap/FilteredIssueLister.java'
# prev_filename = '/Users/phayate/src/ApacheDerby/10.12/tools/release/jirasoap/src/main/java/org/apache/derbyBuild/jirasoap/FilteredIssueLister.java'
# getDiff(curr_filename, prev_filename)

# getDiff('test-module1.java', 'test-module3.java')
# getDiff('test-module1.java', 'test-module2.java')
getDiff('test-module4.txt', 'test-module5.txt')
