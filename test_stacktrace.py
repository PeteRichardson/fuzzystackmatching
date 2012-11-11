'''test_stacktrace.py - unittests for StackTrace class'''

import unittest
from stacktrace import StackTrace

class Test_StackTrace(unittest.TestCase):

    def test_simple(self):
        st = StackTrace("hello good buddy")
        self.assertEqual(st.signature, 'iKFCP')

    def test_fromFile(self):
        st = StackTrace.from_file("traces/jira-5.txt")
        self.assertEqual(st.signature, "iXwg242Q2t2CCt7qqDqy4tBBavTtY202gwoiOw6G5ED3XXOJHluRuiw79qOA")

if __name__ == '__main__':
    unittest.main()