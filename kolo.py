class Kolo():
    def __init__(self, r):
        self.promien = r
        self.pole = 3.14 * r * r
        self.obwod = 2 * 3.14 * r

    def pokaz_pole(self):
        print("Pole: ", self.pole)
    
    def pokaz_obwod(self):
        print("Obwod: ", self.obwod)


kolo1 = Kolo(6)
kolo1.pokaz_pole()
kolo1.pokaz_obwod()