# -*-coding:Utf-8 -*

class Carre:
    "Classe prennant en paramaètre la longueur d'un coté en cm."

    def __init__(self, côté):
        self.côté = côté
        self.aire = côté * côté

    def perimeter(self):
        "Cette méthode permet de retourner le périmètre du carré"

        return(self.côté * 4)


#PARTIE TEST ------------------------

try:
    condition = open("classes.py", "r")
except IOError:
    print("File not open")
else:
    print("carré")
    x = 2
    carré_cubique = Carre(x)
    print("L'aire d'un carré de côté {} est de {} cm2.".format(x, carré_cubique.aire))
    print(carré_cubique.perimeter)
    input("Pouet")
