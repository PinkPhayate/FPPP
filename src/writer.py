import module
import pandas as pd
def write_csv(modules):
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
