strana = float (input("zadej cislo "))

cislo_je_spravne = strana > 0

if cislo_je_spravne:
    print("obvod ctverce se stranou", strana, "je", strana * 4, "cm" )
    print("obsah ctverce se stranou", strana, "je", strana * strana, "cm2")
else:
    print("zadej kladne cislo.")


