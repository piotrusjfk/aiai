zero = ["0","zero", "zera", "zerem"]
jeden = ["1","jeden", "jedynka", "jedynkę"]
dwa = ["2", "dwa", "dwójkę", "dwójka"]
trzy = ["3", "trzy", "trójkę", "trójka"]
cztery = ["4", "cztery", "czwórkę", "czwórka"]
piec = ["5", "pięć", "piątkę", "piątka"]
szesc = ["6", "sześć", "szóstkę", "szóstka"]
siedem = ["7", "siedem", "siódemkę", "siódemka"]
osiem = ["8", "osiem", "ósemkę", "ósemka"]
dziewiec = ["9", "dziewięć", "dziewiątkę", "dziewiątka"]
dziesiec = ["10", "dziesięć", "dziesiątka", "dziesiątkę", "dychę"]
jedenascie = ["11","jedenaście", "jedenastkę", "jedenastu"]
dwanascie = ["12", "dwanaście", "dwunastu", "dwunastkę"]
trzynascie = ["13", "trzynaście","trzynastu","trzynastkę"]
czternascie = ["14", "czternaście", "czternastu", "czternastkę"]
pietnascie = ["15", "piętnaście","piętnastu", "piętnastkę"]
szesnascie = ["16", "szesnaście","szesnastu","szesnastkę"]
siedemnascie = ["17","siedemnaście", "siedemnastu", "siedemnastkę"]
osiemnasice = ["18", "osiemnaście","osiemnastu","osiemnastkę"]
dziewietnascie = ["19","dziewiętnaście", "dziewiętnastu","dziewiętnastkę"]
plus = ["+", "dodaj", "plus", "dodać"]
minus = ["-", "odejmij", "minus", "odjąć"]
gwiazdka = ["*", "x", "razy", "mnożone", "pomnożone", "pomnożyć"]
ukosnik = ["/", ":", "dzielone", "podziel"]
baza = [zero, jeden,dwa,trzy, cztery, piec, szesc,siedem, osiem, dziewiec,
        dziesiec,jedenascie,dwanascie,trzynascie,czternascie,pietnascie,szesnascie,siedemnascie,osiemnasice,dziewietnascie, 
        plus, minus, gwiazdka, ukosnik]

dzialanie = ""
tekst = input("wpisz działanie: ")

def tlumacz(slowo_wpisane):
    for lista in baza:
        for slowo in lista:
            if slowo_wpisane == slowo:
                return lista[0]
    return ""

def oblicz_operacje(liczba1, liczba2, operacja):
    if operacja == '+':
        return liczba1 + liczba2
    elif operacja == '-':
        return liczba1 - liczba2
    elif operacja == '*':
        return liczba1 * liczba2
    elif operacja == '/':
        return liczba1 / liczba2

def oblicz_dzialanie(tekst):
    wynik = 0
    liczba = ''
    operacja = ''

    for znak in tekst:
        if znak.isdigit():
            liczba += znak
        elif liczba:
            if operacja == '':
                wynik = int(liczba)
            else:
                wynik = oblicz_operacje(wynik, int(liczba), operacja)
            liczba = ''
            operacja = znak
    if liczba:
        wynik = oblicz_operacje(wynik, int(liczba), operacja)
    return wynik

dzialanie = ""
tekst = input("wpisz działanie: ")

for slowo in tekst.split(" "):
    dzialanie += tlumacz(slowo)

print(dzialanie)
print(oblicz_dzialanie(dzialanie))