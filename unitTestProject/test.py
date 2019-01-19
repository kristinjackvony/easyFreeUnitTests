import unittest

from my_test import isItADozen

class TestDozen(unittest.TestCase):
    def test_a_dozen(self):
        result = isItADozen(12)
        self.assertEqual(result, "Yup, it's a dozen!")

    def test_more_than_a_dozen(self):
    	result = isItADozen(15)
    	self.assertEqual(result, "You have more than a dozen here")

    def test_less_than_a_dozen(self):
    	result = isItADozen(10)
    	self.assertEqual(result, "Nope, you have less than a dozen")

    def test_less_than_zero(self):
    	result = isItADozen(-1)
    	self.assertEqual(result, "You don't have any at all!")

    def test_not_a_number(self):
    	result = isItADozen("FOO")
    	self.assertEqual(result, "This is not a number")

if __name__ == '__main__':
    unittest.main()