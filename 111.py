import random

def losowe_liczby(rozmiar, min_wartosc, max_wartosc):
    lista = [random.randint(min_wartosc, max_wartosc) for _ in range(rozmiar)]
    return lista
lista = losowe_liczby(5, 10, 15)
print(lista) 