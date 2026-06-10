from Uzytkownik import Uzytkownik
user1 = Uzytkownik()
user2 = Uzytkownik()
user3 = Uzytkownik()
user4 = Uzytkownik()

user1.imie = "Piotr"
user1.nazwisko = "Nowak"
user1.wiek = 56

user2.imie = "Jan"
user2.nazwisko = "Kowalski"
user2.wiek = 30

user3.imie = "Kamil"
user3.nazwisko = "Krakowski"
user3.wiek = 60

user4.imie = "Anna"
user4.nazwisko = "Wiśniewska"
user4.wiek = 22

# print(user1.imie, user1.nazwisko, user1.wiek)
# print(user2.imie, user2.nazwisko, user2.wiek)
# print(user3.imie, user3.nazwisko, user3.wiek)
# print(user4.imie, user4.nazwisko, user4.wiek)

# user1.wyswietl()
# user2.wyswietl()
# user3.wyswietl()
# user4.wyswietl()

user1.wyswietl()
user1.zmien_wiek(12)
user1.wyswietl()

# ZADANIE 2

class Przedmiot():
    srednia = 0

    def stworz_liste(self):
        self.oceny = []

    def dodaj_ocene(self, ocena):
        self.oceny.append(ocena)
        self.srednia = sum(self.oceny) / len(self.oceny)

    def wyswietl_oceny(self):
        print("Lista ocen", self.oceny)
    def wyswietl_srednia(self):
        print(f"Średnia ocen: {self.srednia}")

matematyka = Przedmiot()
matematyka.stworz_liste()
matematyka.dodaj_ocene(5)
matematyka.dodaj_ocene(6)
matematyka.dodaj_ocene(2)
matematyka.dodaj_ocene(3)
matematyka.dodaj_ocene(4)
matematyka.dodaj_ocene(1)

matematyka.wyswietl_oceny()
matematyka.wyswietl_srednia()