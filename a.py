def binarny(a):
    wynik = ''
    while (a > 0):
        m = a % 2
        a = a // 2
        wynik = str(m) + wynik
    print(wynik)

binarny(42)

def decimal(a):
    dec = 0 
    i = 0
    while (a >0):
        m = a % 10
        a = a // 10
        dec += m * (2**i)
        i += 1
    print(dec)
decimal(101010)

def pierwsza(a):
    if a <= 1: 
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
    return True

print(pierwsza(1523))

def palindrom(text):
    if text == text[::-1]:
        print(f"{text} jest palindromem")
    else:
        print(f"{text} nie jest palindromem")

palindrom("kajak")