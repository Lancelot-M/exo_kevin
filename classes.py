#!/usr/bin/python3.6
# -*-coding:Utf-8 -*

class Carre:
    "Classe prennant en paramaètre la longueur d'un coté en cm."

    def __init__(self, cote):
        self.cote = cote
        self.perimeter = self.perimeter()
        self.aire = self.aire()

    def perimeter(self):
        "Cette méthode permet de retourner le périmètre du carré"

        return(self.cote * 4)

    def aire(self):
        return(self.cote * self.cote)

    def facto(X, carre):
        x = X * carre.cote
        return(Carre(x))

    def addit(carreA, carreB):
        x = carreA.cote + carreB.cote
        return(Carre(x))

    def inht(carre):
        return(int(carre.cote))

#PARTIE TEST ----------------------------------------------------------

if __name__ == '__main__':

    carre1 = Carre(2.1)
    print("Le carre à un côté de {}cm, une aire de {}cm2 et un périmètre de {}cm.\n".format(carre1.cote, carre1.aire, carre1.perimeter))
    carre2 = Carre.facto(2, carre1)
    carre3 = Carre.addit(carre1, carre2)
    print(Carre.inht(carre3))
    input("Pouet")
