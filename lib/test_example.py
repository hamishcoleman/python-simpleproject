""" This is an example test script for the "example.py" module
"""

import unittest
import example


class Example(unittest.TestCase):
    """ This is the class that the test system looks for tests in
    """

    def test_fortytwo(self):
        """ Confirm that fourtytwo is, in fact 42
        """
        self.assertEqual(example.fortytwo(), 42)

    def test_hellostr(self):
        """ Be sure to check that hellostr is hello
        """
        self.assertEqual(example.hellostr(), 'hello')
