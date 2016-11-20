import file_operation as fo
import product_metrics as pdm
import process_metrics as psm

'''identify module'''
root = '/Users/phayate/src/ApacheDerby/'
ver = '10.12'
prev_ver = '10.11'
# get list about files under the repository
list = fo.fild_all_files(root + ver)
for mod in list:
    # get product metrics
    mod = pdm.getProcuctMetrics(mod)
    # find same file from previous version
    files = get_all_files_text(root + prev_ver)
    if mod.filename in files:
        psm.getProcessMetrics(mod, files[ files.index(mod.filename) ])


''' get process metrics '''

# if exists, get diff
