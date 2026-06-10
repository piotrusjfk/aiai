def sprawdz_dane(login, haslo, poprawny_login, poprawne_haslo):
    """ Zwraca True jeśli dane są poprawne,  False gdy jest inaczej"""
    return login == poprawny_login and haslo == poprawne_haslo

def logowanie(poprawny_login, poprawne_haslo, max_proby = 3):
    for i in range(max_proby):
        login = input("podaj login: ")
        haslo = input("Podaj hasło: ")

        if sprawdz_dane(login, haslo, poprawny_login, poprawne_haslo):
            print("zalogowano!")
            return True
        else:
            print("niepoprawny login lub hasło")

    print("przekroczono dozwoloną liczbę prób")
    return False
    
poprawny_login = "admin"
poprawne_haslo = "1234"
logowanie(poprawny_login, poprawne_haslo)