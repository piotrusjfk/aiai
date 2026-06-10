suma = 0
licznik = 0

N = int(input("Ile maksymalnie ocen chcesz wprowadzić: "))

for i in range(N):
    wpis = input(f"Podaj ocenę {i+1} (lub 'q' aby zakończyć): ")
    if wpis.lower() == 'q':
        break
    try:
        ocena = float(wpis)
        suma += ocena
        licznik += 1
    except ValueError:
        print("To nie jest poprawna ocena. Spróbuj ponownie.")

if licznik > 0:
    srednia = suma / licznik
    print(f"Średnia ocen wynosi: {srednia:.2f}")
else:
    print("Nie podano żadnych ocen.")
