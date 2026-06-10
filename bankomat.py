saldo = 100.0
wybor = ''
 
# programy pomocnicze
 
def menu() -> str:
    print("Wybierz opcje:")
    print("1. Wpłata\n2. Wypłata\n3. Sprawdz stan konta\n4. Zakoncz")
    return input("Wpisz odpowiedz: ")
 
def stan_konta() -> float:
    print(f'Twoj stan konta: {saldo}')
 
def wyplata():
    global saldo
    stan_konta()
    wyplata = input("Podaj ile chcesz wyplacic kasy: ")
 
    try:
        wyplata = float(wyplata)
        if wyplata > 0 and wyplata <= saldo:
            saldo -= wyplata
            print(f'Wyplaciles {wyplata}')
            stan_konta()
        else:
            raise Exception()
    except:
        print("Podaj poprawna wartosc")
 
 
def wplata():
    global saldo
    stan_konta()
    wplata = input("Podaj ile chcesz wplacic: ")
 
    try:
        wplata = float(wplata)
        if wplata > 0:
            saldo += wplata
            stan_konta()
        else:
            raise Exception()
    except:
        print("Podaj poprawna wartosc")
 
# nasz główny program
 
program = True
 
while(program):
    wybor = menu()
 
    match wybor:
        case "1":
            wplata()
            pass
        case "2":
            wyplata()
            pass
        case "3":
            stan_konta()
            pass
        case "4":
            program = False
            pass
        case _:
            print("Wybrales zla odpowiedz")
            pass