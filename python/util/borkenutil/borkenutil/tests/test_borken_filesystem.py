from unittest import TestCase

from borkenutil import borken_logger

class TestBorken(TestCase):
	def test_info(self):
            borken_logger.info("INFO")
