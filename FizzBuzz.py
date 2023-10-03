class FizzBuzz():
    def affiche(self, n1, n2):
        liste = ""
        for i in range(n1, n2+1):
            if i % 15 == 0:
                liste += "FrisBee"
            elif i % 3 == 0:
                liste += "Fizz"
            elif i % 5 == 0:
                liste += "Buzz"
            else:
                liste += str(i)
        print(liste)
        return liste

