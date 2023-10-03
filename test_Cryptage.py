import unittest
from Cryptage import *

class Cryptage_Test(unittest.TestCase):
    def setUp(self):
        self.instance=Cryptage()

    def test_crypt_message_avec_pas(self):
        message = "Comment ça mon reuf ?"
        pas = 5
        self.assertEqual(self.instance.crypt(message, pas), "Htrrjsyeçfertsewjzke^5")

    def test_decrypt_message_avec_pas(self):
        message = "Htrrjsyeçfertsewjzke^5"
        self.assertEqual(self.instance.decrypt(message), "Comment ça mon reuf ?")

if __name__ == '__main__':
    unittest.main()