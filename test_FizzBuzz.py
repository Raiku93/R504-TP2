import unittest
from FizzBuzz import *

class TestFizzBuzz(unittest.TestCase):
    def setUp(self):
         self.instance=FizzBuzz()

    def test_affiche_sans_param(self):
         nombre = 15
         self.assertEqual(self.instance.affiche(nombre), "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FrisBee")


if __name__ == '__main__':
     unittest.main()


