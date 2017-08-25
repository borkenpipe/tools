from unittest import TestCase

from borkenutil import *

class TestBorken(TestCase):
    def test_is_string(self):
        s ="SDF"
        self.assertTrue(isinstance(s, basestring))
        self.assertTrue(False != True)
