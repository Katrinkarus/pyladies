while True:
    rodne_cislo = input('Zadaj rodne cislo: ')
    datum = rodne_cislo[0:6]
    lomitko = "/"
    poradie = rodne_cislo[7:11]
    x = int(datum + poradie)
    if rodne_cislo == datum + lomitko + poradie and x % 11 == 0:
        print('Spravne zadane rodne cislo.')
    # elif x % 11 == 0:
    #     print("Spravne zadane rodne cislo.")
        break
    print("Zle zadane rodne cislo. Zadaj rodne cislo: ")
