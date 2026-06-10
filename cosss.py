class Samochod():
    marka = ""
    model = ""
    kolor = ""
    silnik = ""
    moc_hp = 0
    def __init__(self, marka, model, kolor, silnik, moc_hp):
        self.marka = marka
        self.model = model
        self.kolor = kolor
        self.silnik = silnik
        self.moc_hp = moc_hp

    def wyswietl(self):
        print(self.marka, self.model, self.kolor, self.silnik, self.moc_hp)

auto = Samochod("Dodge", "charger", "czerwony", "V8", 717)
auto.wyswietl
auto.marka = "Dodge"
auto.model = "charger"
auto.kolor = "czerwony"
auto.silnik = "V8"
auto.moc_hp = 717