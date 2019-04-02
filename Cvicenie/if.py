strana = float(input("Zadej stranu ctverce v centimetrech:"))
cislo_je_spravne = strana > 0

if cislo_je_spravne:
    print("Obvod ctverce se stranou", strana, "je", 4 * strana, "cm")
    print("Obsah ctverce se stranou", strana, "je", strana * strana, "cm2")
else:
    print("Strana musi byt kladna, jinak z toho nebude ctverec!")

print("dekujeme za pouziti geometricke kalkulacky.")