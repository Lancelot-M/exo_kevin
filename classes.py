# -*-coding:Utf-8 -*

class Carre:
    "Classe prennant en paramaètre la longueur d'un coté en cm."

    def __init__(self, côté):
        self.côté = côté
        self.aire = côté * côté

try:
    condition = open("classes.py", "r")
except IOError:
    print("File not open")
else:
    print("carré")

