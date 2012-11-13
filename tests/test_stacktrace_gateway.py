'''test_stacktrace_gateway.py - tests for ST_Gateway class'''

import unittest
from stacktrace_gateway import STGateway


class TestSTGateway(unittest.TestCase):
    st = None

    def setup(self):
        self.stg = STGateway()
        self.stg.delete()
        self.stg.create()
        self.stg.insert("foo", "bar", 'TIN-1234')

    def test_simple(self):
        '''find a simple signature inserted in a dummy db'''
        cur = self.stg.find_matches("bar")
        self.assertEqual(len(cur), 1)

if __name__ == '__main__':
    unittest.main()

