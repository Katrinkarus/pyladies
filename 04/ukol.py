zaznamy = ["pepa novak", "Jiri Sladek", "Ivo navratil", "jan Polednik"]

spravne = []

for zaznam in zaznamy:
    jmeno, prijmeni = zaznam.split()
    if not jmeno[0].islower() and not prijmeni[0].islower():
        spravne.append(zaznam)

print(spravne)

spatne = []

for zaznam in zaznamy:
    jmeno, prijmeni = zaznam.split()
    if jmeno[0].islower() or prijmeni[0].islower():
        spatne.append(zaznam)

for zaznam in zaznamy:
    jmeno, prijmeni = zaznam.split()
    if not jmeno[0].islower() and not prijmeni[0].islower():
        spravne.append(zaznam)
    else:
        spatne.append(zaznam)

print(spatne)

{}{}}}}}}

