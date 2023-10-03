import unittest
from FizzBuzz import *

class TestFizzBuzz(unittest.TestCase):
    def setUp(self):
         self.instance=FizzBuzz()

    def test_affiche_deux_param(self):
         nombre1 = 10
         nombre2 = 16
         self.assertEqual(self.instance.affiche(nombre1, nombre2), "Buzz11Fizz1314FrisBee16")
    


if __name__ == '__main__':
     unittest.main()


