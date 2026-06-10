WRM = 0
def oblicz_WRM(matematyka_podst):
    WRM = 2 * matematyka_podst
def oblicz_punkty():
    M = float(input("podaj procentowy wynik matury z matematyki "))
    WRM = 2 * M
G1 = float(input("Podaj liczbę punktów z przedmiotu g1"))
G2 = float(input("Podaj liczbę punktów z przedmiotu g2"))

suma_punktow = WRM + G1 + G2
print(f"\nPodwojona liczba punktów z matematyki podstawowej (WRM): {WRM}")
print(f"punkty g1: {G1}")
print(f"punkty G2:{G2}")
print(f"Łączna suma punktów: {suma_punktow}")

if __name__ == "__main__":
    oblicz_punkty()