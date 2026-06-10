def suma_cyfr(liczba):
    suma = 0
    for cyfra in str(abs(liczba)):
        suma += int(cyfra)
    return suma

wynik = suma_cyfr(4325356767889908987896585474362514)
print(wynik)