def bez_powtorzen(lista):
    wynik = []
    for x in lista:
        if x not in wynik:
            wynik.append(x)
    return wynik

lista = [1, 4, 2 , 4, 2]
print(bez_powtorzen(lista))