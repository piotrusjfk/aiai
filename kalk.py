print("dostępne działania: +, -, *, /")
print("aby wyjść wpisz 'q' ")

while True:
    dane = input( " wprowadź działanie")

    if dane.lower() == 'q':
        print("koniec programu")
        break

    try:
        a, op, b = dane.split()
        a = float(a)
        b = float(b)
        
        if op == '+':
            wynik = a + b
        elif op == '-':
            wynik = a - b
        elif op == '*':
            wynik = a * b
        elif op == '/':
            if b == 0:
                print("nie można dzielić przez 0")
                continue
            wynik = a / b
        else:
            print("nieznana operacja")
            continue

        print(f"wynik: {wynik}")
    except ValueError:
        print("błąd liczbowy")
    except:
        print("inny błąd")