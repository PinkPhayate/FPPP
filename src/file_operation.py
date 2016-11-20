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
                list.append(full_path)
                print full_path
    return list
