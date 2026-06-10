imie = input ("Podaj swoje imie: ")
nazwisko = input("Podaj swoje nazwisko: ")
rok_urodzenia = int(input("Podaj rok urodzenia: "))

import datetime
aktualny_rok = datetime.datetime.now().year
wiek = aktualny_rok - rok_urodzenia

print(f"{imie} {nazwisko} ma rocznikowo {wiek} lat.")