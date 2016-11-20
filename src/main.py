import file_operation as fo
import module
import product_metrics as pdm
import process_metrics as psm

def printModules(list):
    for mod in list:
        print mod.filename
        print mod.LOC
        print mod.TChar
        print mod.churnMetrics
        print mod.relativeChrun
        print mod.deletredChurn
        print mod.ncdChurn
        print mod.isNew


'''identify module'''
root = '/Users/phayate/src/ApacheDerby/'
ver = '10.12'
prev_ver = '10.11'
# get list about files under the repository
list = fo.fild_all_files(root + ver)
for mod in list:
    print mod.filename
    # get product metrics
    mod = pdm.getProcuctMetrics(mod)
    # find same file from previous version
    files = fo.get_all_files_text(root + prev_ver)
    if type (mod) ==  module.Module:
        # if exists, get diff
        if mod.filename in files:
            mod = psm.getProcessMetrics(mod, files[ files.index(mod.filename) ])
        # if not, isNew attribute = 1
        else:
            mod.isNew = 1

printModules(list)
