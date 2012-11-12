#!/usr/bin/env python

import sys
from glob import glob
from stacktrace import StackTrace
from stacktrace_gateway import ST_Gateway

assert len(sys.argv) > 1, "Need at least one arg"
files = glob(sys.argv[1])
if len(files) == 0:
    print "Nothing matched {0}".format(sys.argv[1])
    sys.exit(0)

st = ST_Gateway()
for file in files:
    stacktext = open(file, "r").read()
    trace = StackTrace(stacktext)
    curs = st.find_matches(trace.signature)
    for row in curs:
        print row
