'''test_stacktrace_gateway.py - tests for ST_Gateway class'''

import unittest
from stacktrace_gateway import ST_Gateway


class Test_ST_Gateway(unittest.TestCase):
    st = None

    def setUp(self):
        self.st = ST_Gateway()
        self.st.delete()
        self.st.create()
        self.st.insert("foo", "bar", 'TIN-1234')

    def test_simple(self):
        cur = self.st.find_matches("bar")
        self.assertEqual(len(cur), 1)

if __name__ == '__main__':
    unittest.main()\
