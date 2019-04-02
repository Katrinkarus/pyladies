def RC():
    rodne_cislo = input("Zadaj rodne cislo: ")
    datum = rodne_cislo[0:6]
    poradie = rodne_cislo[7:11]
    rok = datum[0:2]
    mesiac = datum[2:4]
    pohlavie = rodne_cislo[2]
    den = datum[4:6]
    while True:
        datum = rodne_cislo[0:6]
        lomitko = "/"
        poradie = rodne_cislo[7:11]
        x = int(datum + poradie)
        if x % 11 == 0 and rodne_cislo == datum + lomitko + poradie:
            print('Spravne zadane rodne cislo.')
        # if x % 11 == 0:
        #     print("Spravne zadane rodne cislo.")
            break
        else:
            print("Zle zadane rodne cislo. Zadaj rodne cislo: ")
    # for i in rodne_cislo:
    #     if rodne_cislo != datum + "/" + poradie:
    #         print("Zle zadane rodne cislo!")
    #     if rodne_cislo == datum + "/" + poradie :
    #         print("Spravne zadane rodne cislo: ", rodne_cislo)
    #     x = int(datum + poradie)
    #     if x % 11 == 0:
    #         print("Cislo je delitelne 11.")
    #     else:
    #         print("Cislo nie je delitelne 11. Zle rodne cislo!")
    y = int(pohlavie)
    if y == 5 or 6:
        print("Datum narodenie je: ", den, int(mesiac) - 50, rok, "Si zena.")
    else:
        print("Datum narodenia je: ", den, mesiac, rok, "Si muz.")
RC()

