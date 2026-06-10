miesiac = input("podaj miesiac: ").lower()

if miesiac in ["1", "2"]:
    print ("cena biletu: $150")
elif miesiac in ["3", "4", "11", "12"]:
    print("cena biletu: $199")
elif miesiac in ["5", "6", "10"]:
    print("cena biletu: $249")
elif miesiac in ["7", "8", "9"]:
    print("cena biletu: $299")