class FizzBuzz():
    def affiche():
        liste = ""
        for i in range(1, 101):
            if i % 15 == 0:
                liste += "FrisBee"
            elif i % 3 == 0:
                liste += "Fizz"
            elif i % 5 == 0:
                liste += "Buzz"
            else:
                liste += str(i)
        print(liste)
