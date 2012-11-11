'''stacktrace.py - a stacktrace'''

from subprocess import Popen, PIPE, STDOUT

class StackTrace(object):
    def __init__(self, stacktrace, signature=None):
        self.stacktrace = stacktrace
        if signature:
            self._signature = signature

    @property
    def signature(self):
        '''fuzzy hash of stacktrace'''
        try:
            return self._signature
        except AttributeError:
            self._signature = self.calc_signature()
        return self._signature

    def calc_signature(self):
        p = Popen(['bin/ssdeep'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
        stdout_data = p.communicate(input=self.stacktrace)[0]
        return stdout_data.split("\n")[1].split(",")[0].split(":")[1]

    @staticmethod
    def from_file(filename):
        '''Factory method to create a StackTrace from text in a file'''
        st = open(filename, "r").read()
        return StackTrace(st)
