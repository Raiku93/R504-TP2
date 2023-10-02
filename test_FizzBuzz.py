import unittest
from FizzBuzz import *

class TestFizzBuzz(unittest.TestCase):
    def setUp(self):
         self.instance=FizzBuzz()

    def test_affiche_sans_param(self):
         self.assertEqual(self.instance.affiche(), "12Fizz")

if __name__ == '__main__':
     unittest.main()