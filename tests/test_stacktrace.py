'''test_stacktrace.py - unittests for StackTrace class'''

import unittest
from stacktrace import StackTrace

class Test_StackTrace(unittest.TestCase):

    def test_simple(self):
        st = StackTrace("hello good buddy")
        self.assertEqual(st.signature, 'iKFCP')

    def test_fromFile1(self):
        st = StackTrace.from_file("traces/jira-1.txt")
        self.assertEqual(st.signature, "YX7/F0hrIRHF8ILKLC5CdLfwHnKvL3oIJG6WMY2GEGYVNGEG")
 
    def test_fromFile2(self):
        st = StackTrace.from_file("traces/jira-2.txt")
        self.assertEqual(st.signature, "YX7/F0hrIRHF8ILKLC5CdLfwHnKvL3oIJG6WMY2GEGYVNGE1n")

    def test_fromFile3(self):
        st = StackTrace.from_file("traces/jira-3.txt")
        self.assertEqual(st.signature, "YX7/F0hrIRHF8ILKLC5CdLfwHnKvL3oIJG6WMY2GEGYVNGEEu")

    def test_fromFile4(self):
        st = StackTrace.from_file("traces/jira-4.txt")
        self.assertEqual(st.signature, "YXB0tKVmLXgM/HMTRYyME1ROPpMTRbMCu")
 
    def test_fromFile5(self):
        st = StackTrace.from_file("traces/jira-5.txt")
        self.assertEqual(st.signature, "iXwg242Q2t2CCt7qqDqy4tBBavTtY202gwoiOw6G5ED3XXOJHluRuiw79qOA")

    def test_fromFile6(self):
        st = StackTrace.from_file("traces/jira-6.txt")
        self.assertEqual(st.signature, "PzUoD9HFYp/NELHcfeHq9HMrYpcGobGeksIXF1lwAvCZ0r")

    def test_fromFile7(self):
        st = StackTrace.from_file("traces/jira-7.txt")
        self.assertEqual(st.signature, "CE4rOkG7fOBL7JF//MvLYOqdncMhlTEaFCvLYOqdncMhlTEaFtdGWakIJmsIdGWR")


if __name__ == '__main__':
    unittest.main()