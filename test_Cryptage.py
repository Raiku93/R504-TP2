import unittest
from Cryptage import *

class Cryptage_Test(unittest.TestCase):
    def setUp(self):
        self.instance=Cryptage()



    def test_crypt_message_avec_pas(self):
        message = "Comment ça mon reuf ?"
        self.assertEqual(self.instance.crypt(message), "Dpnnfouaçbanpoasfvga@")



if __name__ == '__main__':
    unittest.main()