import unittest
from FizzBuzz import *

class TestFizzBuzz(unittest.TestCase):
    def setUp(self):
         self.instance=FizzBuzz()

    def test_affiche_deux_param(self):
         nombre1 = 5
         nombre2 = 10
         self.assertEqual(self.instance.affiche(nombre1, nombre2), "BuzzFizz78FizzBuzz")
    


if __name__ == '__main__':
     unittest.main()


