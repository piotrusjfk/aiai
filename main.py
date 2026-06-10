from dziedziczenie import Kinder, Jajko

k1 = Kinder("Kinder Bueno", "mleczna z nadzieniem", "10.11.2025", "10.12.2025", 572)
k1.kiedy_produkcja()
k1.kiedy_waznosc()

j1 = Jajko("Kinder Joy", "biało mleczna", "15.11.2025", "15.12.2025", 550, "samochodzik")
j2 = Jajko("Kinder Niespodzianka", "mleczna", "15.11.2025", "15.12.2025", 561, "figurka")

j1.unboxing()
j2.unboxing()
