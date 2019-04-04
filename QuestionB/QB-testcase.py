import unittest
from QuestionB import *



class TestversionsFunc(unittest.TestCase):
	"""Test mathfuc.py"""

	def test_versions(self):
		"""Test method versions(version1, version2)"""
		self.assertEqual('1.1.1 is euqal to 1.1.1', versions("1.1.1", "1.1.1"))
		self.assertEqual('1.1.1 is euqal to 1.1.01', versions("1.1.1", "1.1.01"))
		self.assertEqual('1.1.1 is less than 1.1.2', versions("1.1.1", "1.1.2"))
		self.assertEqual('1.1.1 is less than 1.1.02', versions("1.1.1", "1.1.02"))
		self.assertEqual('1.1.2 is greater than 1.1.1', versions("1.1.2", "1.1.1"))
		self.assertEqual('1.1.2 is greater than 1.1.01', versions("1.1.2", "1.1.01"))


if __name__ == '__main__':
	unittest.main()