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

        message_crypte += str(pas)
        return message_crypte

    def decrypt():
        caracteres = string.ascii_letters + string.punctuation + string.digits + " "
        message_decrypte = ""

        for lettre in message:
            if lettre in caracteres:
                index = caracteres.index(lettre)
                lettre_decryptee = caracteres[(index - pas) % len(caracteres)]
                message_decrypte += lettre_decryptee
            else:
                message_decrypte += lettre

        return message_decrypte