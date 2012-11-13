'''import_traces.py'''

from glob import glob
import sys
from stacktrace import StackTrace
from stacktrace_gateway import STGateway

FILES = glob('traces/*.txt')
if len(FILES) == 0:
    print "Nothing matched traces/*.txt"
    sys.exit(0)

ST = STGateway()
ST.delete()
ST.create()


for filename in FILES:
    issue = filename[7:-4]
    stack = open(filename, "r").read()
    trace = StackTrace(stack)
    print "sig is {0} chars".format(len(trace.signature))
    ST.insert(issue, stack, trace.signature)
