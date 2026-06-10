class Kinder:
    def __init__(self, nazwa, rodzaj_czekolady, data_produkcji, data_waznosci, ilosc_kalorii):
        self.nazwa = nazwa
        self.rodzaj_czekolady = rodzaj_czekolady
        self.data_produkcji = data_produkcji
        self.data_waznosci = data_waznosci
        self.ilosc_kalorii = ilosc_kalorii

    def najedzony(self):
        print(f"{self.nazwa} został zjedzony")

    def roztopiony(self):
        print(f"Było ciepło, {self.nazwa} roztopił się")

    def kiedy_produkcja(self):
        print(f"{self.nazwa} został wyprodukowany: {self.data_produkcji}")

    def kiedy_waznosc(self):
        print(f"{self.nazwa} jest ważny do: {self.data_waznosci}")


class Jajko(Kinder):
    def __init__(self, nazwa, rodzaj_czekolady, data_produkcji, data_waznosci, ilosc_kalorii, niespodzianka):
        super().__init__(nazwa, rodzaj_czekolady, data_produkcji, data_waznosci, ilosc_kalorii)
        self.niespodzianka = niespodzianka

    def unboxing(self):
        if "joy" in self.nazwa.lower():
            print(f"W środku Kinder Joja ukryła się {self.niespodzianka}")
        else:
            print(f"W środku Kinder jajka ukryła się {self.niespodzianka}")
