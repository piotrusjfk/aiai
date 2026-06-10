import getpass
poprawny_pin = "1234" 
poprawne_haslo = "masło"

pin = input("podaj 4 cyfrowy pin: ")

if pin == poprawny_pin:
    haslo = input("Podaj hasło słowne: ")
    if haslo == poprawne_haslo:
        print("Dostęp przyznany!")
    else:
        print("Nieprawidłowe hasło.")
else:
    print("Błędny PIN.")