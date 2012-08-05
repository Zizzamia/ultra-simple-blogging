from pypath import pypath;pypath()
import unittest
from google.appengine.api import memcache
from google.appengine.ext import db
from google.appengine.ext import testbed


class ATestSuit(unittest.TestCase):

    def setUp(self):
        self.param = 1

    def test_param(self):
        self.assertEqual(self.param, 1)

if __name__ == '__main__':
    unittest.main()

