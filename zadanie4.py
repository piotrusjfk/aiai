import math

a = float(input("Podaj długość boku a: "))
b = float(input("Podaj długość boku b: "))
c = float(input("Podaj długość boku c: "))

if a + b > c and a + c > b and b + c > a:
    print("Trójkąt może powstać")

    najkrotszy = min(a, b, c)
    najdluzszy = max(a, b, c)
    print(f"Najkrótszy bok: {najkrotszy}")
    print(f"Najdłuższy bok: {najdluzszy}")

    if a == b == c:
        print("Trójkąt równoboczny")
    elif a == b or b == c or a == c:
        print("Trójkąt równoramienny")
    else:
        print("Trójkąt różnoboczny")

    obwod = a + b + c
    print(f"Obwód trójkąta: {obwod}")

    p = obwod / 2
    pole = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(f"Pole trójkąta: {pole:.2f}")

    boki = sorted([a, b, c])
    x, y, z = boki

    if math.isclose(z**2, x**2 + y**2):
        print("Trójkąt prostokątny")
    elif z**2 > x**2 + y**2:
        print("Trójkąt rozwartokątny")
    else:
        print("Trójkąt ostrokątny")
else:
    print("Z tych długości nie da się zbudować trójkąta.")
