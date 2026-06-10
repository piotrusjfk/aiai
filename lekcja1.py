print("Hej, jestem Python!")
print("A ty, jak masz na imie?")

imie = input()
#print(imie)

print("czesc", imie, " milo cie pozanac") # tu wypisuje imie uytkownika
print("ja powstalem w 1991 roku, dzieki pracy programisty Guido van Rossuma!")

#sekcja rok urodzenia
rok_urodzenia = input("a kiedy sie urodziles? ")
wiek = 2025 - int(rok_urodzenia) #"3" -> 3
print("Wow, czyli masz juz", wiek, "lat")

#sekcja kolor
kolor = input("Jaki jest twoj ulubiony kolor? ")
print("moj ulubiony kolor to niebieski.")

miasto = input("z jakiego miasta jesteś?")
print("bylo milo cie poznac", imie)

#program wypisuje ze:
# Wiem, ze masz 25 lat, jestes z (lodz) i lubisz zielony
print("wiem że masz", wiek, "i jesteś z", miasto, "a twoj ulubiony kolor to", kolor)
print("Postaram sie zapamietac do nastepnego spotkania")