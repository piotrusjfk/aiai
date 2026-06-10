tekst = input("wprowadź tekst")
if 'a' in tekst:
    print("tekst zawiera literę 'a'.")
if 'd' in tekst:
    print("tekst zawiera literę 'd'.")
if 'as' in tekst:
    print("tekst zawiera litery 'as'.")
if 'zzz' in tekst:
    print("tekst zawiera litery 'zzz'.")
if not ('a' in tekst or 'd' in tekst or 'as' in tekst or 'zzz' in tekst):
    print("Tekst nie zawiera żadnego z wymaganych znaków ani ciągów.")