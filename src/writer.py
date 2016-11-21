import module
import csv
def write_csv(modules):
    f = open('./metrics_df.csv', 'ab')
    csvWriter = csv.writer(f)
    for mod in modules:
        if type (mod) !=  module.Module :
            return
        list = [
                mod.filename,
                mod.LOC,
                mod.TChar,
                mod.churnMetrics,
                mod.relativeChrun,
                mod.deletredChurn,
                mod.ncdChurn,
                mod.isNew
        ]
        csvWriter.writerow(list)
    f.close()

'''
Test
'''

import stub
list = []
[list.append( stub.generate_stub() ) for x in xrange(10)]
write_csv(list)
