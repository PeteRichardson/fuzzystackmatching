'''import_traces.py'''

from glob import glob
import sys
from stacktrace import StackTrace
from stacktrace_gateway import ST_Gateway

files = glob('traces/*.txt')
if len(files) == 0:
    print "Nothing matched traces/*.txt"
    sys.exit(0)

st = ST_Gateway()
st.delete()
st.create()


for file in files:
    issue = file[7:-4]
    stack = open(file, "r").read()
    trace = StackTrace(stack)
    print "sig is {0} chars".format(len(trace.signature))
    st.insert(issue, stack, trace.signature)
