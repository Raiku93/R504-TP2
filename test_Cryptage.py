import unittest
from Cryptage import *

class Cryptage_Test(unittest.TestCase):
    def setUp(self):
        self.instance=Cryptage()



    def test_crypt_message(self):
        message = "Comment ça mon reuf ?"
        self.assertEqual(self.instance.crypt(message), "")



if __name__ == '__main__':
    unittest.main()