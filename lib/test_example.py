import unittest
import example

class Example(unittest.TestCase):

    def test_fortytwo(self):
        self.assertEqual(example.fortytwo(),42)

    def test_hellostr(self):
        self.assertEqual(example.hellostr(),'hello')

