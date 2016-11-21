import file_operation as fo
import module, writer
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

# files in previous version
origin_files = fo.get_all_files_text(root + prev_ver)
# due to find same file under previous version
transed_files = fo.exchangea_files(origin_files, prev_ver, ver)

# get list about files under current repository
list = fo.fild_all_files(root + ver)
for mod in list:
    # get product metrics
    mod = pdm.getProcuctMetrics(mod)
    # find same file from previous version
    if type (mod) ==  module.Module:
        if mod.filename in transed_files:
            # if exists, get diff
            transed_filename = mod.filename.replace(ver, prev_ver)
            mod = psm.getProcessMetrics(mod, origin_files[ origin_files.index(transed_filename) ])
        else:
            # if not, isNew attribute = 1
            mod.isNew = 1
write_csv(list)
# printModules(list)
