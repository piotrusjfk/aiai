from random import randint, choice

class Postac:
    def __init__(self):
        self.nazwa = ""
        self.zycie = 1
        self.max_zycie = 1

    def atakuj(self, przeciwnik):
        atak = randint(0,3)
        if atak == 0:
            print(f"{przeciwnik.nazwa} uniknął ataku")
        else:
            print(f"{self.nazwa} atakuje {przeciwnik.nazwa}, zadał mu {atak} obrażeń")
            przeciwnik.zycie -= atak


class Przeciwnik(Postac):
    def __init__(self, gracz):
        super().__init__()
        self.zycie = randint(1, gracz.zycie)
        self.max_zycie = self.zycie
        self.nazwa = choice(["zombie", "smok", "wąż", "pająk", "ogr"])


class Gracz(Postac):
    def __init__(self):
        super().__init__()
        self.max_zycie = 10
        self.zycie = 10
        self.nazwa = input("Podaj imię gracza: ")

    def odpoczynek(self):
        self.zycie += 1
        if self.zycie > self.max_zycie:
            self.zycie = self.max_zycie
        print(f"{self.nazwa} odpoczął, aktualny stan życia: {self.zycie}/{self.max_zycie}")

    def walka(self, przeciwnik):
        walka = True
        while walka:
            print(f'życie gracza: {self.zycie}')
            print(f'życie {przeciwnik.nazwa}: {przeciwnik.zycie}')
            akcja = input('Akcja (atak, uciekaj): ')
            if akcja == 'atak':
                self.atakuj(przeciwnik)
                if przeciwnik.zycie <= 0:
                    print(f'{self.nazwa} zabija {przeciwnik.nazwa}')
                    return True
                przeciwnik.atakuj(self)
            elif akcja == 'uciekaj':
                print(f'{self.nazwa} ucieka')
                przeciwnik.atakuj(self)
                walka = False
            else:
                print('Nieznana akcja')
            if self.zycie <= 0:
                print(f'{self.nazwa} ginie')
                return False
        return True


gracz = Gracz()
gra = True
while gra: 
    akcja = input('akcja (zwiedzaj, odpocznij): ')
 
    if akcja == 'zwiedzaj':
        if randint(0, 1) == 0:
            print(f'{gracz.nazwa} znalazl jaskinie')
        else:
            przeciwnik = Przeciwnik(gracz)
            print(f'{gracz.nazwa} natrafił na {przeciwnik.nazwa}')
            gra = gracz.walka(przeciwnik)       
    elif akcja == 'odpocznij':
        gracz.odpoczynek()
    else:
        print('Nieznana akcja')