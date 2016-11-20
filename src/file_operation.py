import os, re
import module

def fild_all_files(directory):
    list = []
    for root, dirs, files in os.walk(directory):
        for file_ in files:
            full_path = os.path.join(root, file_)
            # isJava = re.search(full_path, r'(\.java)$')
            isJava = re.search("\.JAVA$",full_path.upper())
            if isJava is not None :
                list.append(module.Module(full_path))
    return list
def get_all_filesa_text(directory):
    list = []
    for root, dirs, files in os.walk(directory):
        for file_ in files:
            full_path = os.path.join(root, file_)
            # isJava = re.search(full_path, r'(\.java)$')
            isJava = re.search("\.JAVA$",full_path.upper())
            if isJava is not None :
                list.append(module.Module(full_path))
    return list


root = '/Users/phayate/src/ApacheDerby/'
ver = '10.12'
# get list about files under the repository
list = fild_all_files(root + ver)

''' test to exist module class '''
for module in list:
    print module.filename
