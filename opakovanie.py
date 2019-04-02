word = input("Write an english word: ")

prve_pismeno = word[0]
stred = word[1:]
convert = stred + prve_pismeno + "ay"

print(convert)
# PRIKLAD:DOMACI UKOLY2: ULOHA 9
# from random import randrange
# cislo = randrange(3)
# if cislo == 0:
#     print("kamen")
#     if cislo == 1:
#         print("nuzky")
# else:
#     print("parir")


# PRIKLAD:DOMACI UKOLY2: ULOHA 6,7
# strana = int(input("Zadaj stranu krychle: "))
# povrch = 6 * strana **2
# objem = strana **3
# print("S krychle je " + str(povrch) + " cm2")
# print("V krychle je " + str(objem) + " cm3")