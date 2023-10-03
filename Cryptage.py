import string

class Cryptage:
    def crypt(self, message, pas):
        caracteres = string.ascii_letters + string.punctuation + string.digits + " "
        message_crypte = ""

        for lettre in message:
            if lettre in caracteres:
                index = caracteres.index(lettre)
                lettre_cryptee = caracteres[(index + pas) % len(caracteres)]
                message_crypte += lettre_cryptee
            else:
                message_crypte += lettre

        return message_crypte


