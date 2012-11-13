#!/usr/bin/env python
'''stackmatch.py - take a stacktrace and try to find a match
                    in the database'''

import sys
from glob import glob
from stacktrace import StackTrace
from stacktrace_gateway import STGateway

assert len(sys.argv) > 1, "Need at least one arg"
FILES = glob(sys.argv[1])
if len(FILES) == 0:
    print "Nothing matched {0}".format(sys.argv[1])
    sys.exit(0)

STG = STGateway()
for filename in FILES:
    stacktext = open(filename, "r").read()
    trace = StackTrace(stacktext)
    curs = STG.find_matches(trace.signature)
    for row in curs:
        print row
