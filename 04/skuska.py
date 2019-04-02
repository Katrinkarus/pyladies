while True:
    rodne_cislo = input('Zadaj rodne cislo: ')
    datum = rodne_cislo[0:6]
    poradie = rodne_cislo[7:11]
    if rodne_cislo == datum + "/" + poradie:
        print('Spravne zadane rodne cislo.')
        break
    print("Zle zadane rodne cislo. Zadaj rodne cislo: ")
