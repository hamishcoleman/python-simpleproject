#!/usr/bin/env python

""" This script is an example of a test for the main program
"""

import unittest


class TestStringMethods(unittest.TestCase):
    """ This is the class that the test harness looks for tests in
    """

    def test_upper(self):
        """ Test this thing
        """
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        """ Test this other thing
        """
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        """ Test this thing in particular
        """
        txt = 'hello world'
        self.assertEqual(txt.split(), ['hello', 'world'])
        # check that txt.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            txt.split(2)


if __name__ == '__main__':
    unittest.main()
