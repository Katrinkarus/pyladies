kava = int(input("Kolko salok kavy denne vypijes? "))
if kava >= 5:
    print("Este zijes?")
elif kava == 4:
    print("Tazky den? Iste je ze bude este dlhy.")
elif kava == 3:
    print("Tento pocet ti schvalujem.")
elif kava == 2:
    print("Podozrivo malo.")
elif kava == 1:
    print("Len? Bud klames alebo si nemal/nemala čas.")
elif kava == 0:
    print("Neklam! Chod si dat radsej kavu. A ked nie tak aspon caj.")
else:
    print("Ale notak. Nepis zaporne cisla!")