matma = float(input("ocena z matmy: "))
polski = float(input("ocena z polskiego: "))
angielski = float(input("ocena z angielskiego: "))
informatyka = float(input("ocena z informatyki: "))
wf = float(input("ocena z wf: "))

srednia = (matma + polski + angielski + informatyka + wf) / 5
print(f"srednia ocen: {srednia:.2f}")

if srednia > 4.75:
    print("masz czerwony pasek")
else:
    print("nie masz paska")