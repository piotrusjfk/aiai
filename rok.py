from datetime import datetime
rok_urodzenia = int(input("podaj rok urodzenia: "))
rok_aktualny = datetime.now().year

for rok in range(rok_urodzenia, rok_aktualny + 1):
    wiek = rok - rok_urodzenia
    print(f"w roku {rok} miałeś {wiek} lat")