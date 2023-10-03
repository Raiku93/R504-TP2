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


cryptage = Cryptage()
message = "123457"
pas = 7  # Exemple de pas
message_crypte = cryptage.crypt(message, pas)
print("Message crypté :", message_crypte)