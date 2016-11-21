import module
import random

def generate_stub():
    source_str = 'abcdefghijklmnopqrstuvwxyz'
    full_path = "".join([random.choice(source_str) for x in xrange(10)])
    mod = module.Module(full_path)
    mod.LOC = random.randint(1,100)
    mod.TChar = random.randint(1,100)
    mod.churnMetrics = random.randint(1,100)
    mod.relativeChrun = random.randint(1,100)
    mod.deletredChurn = random.randint(1,100)
    mod.ncdChurn = random.randint(1,100)
    mod.isNew = random.randint(1,100)

    return mod
