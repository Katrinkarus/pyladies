tah_pocitace = "kamen"
tah_cloveka = input("Kamen, nuzky, nebo papir? ")
if tah_cloveka == tah_pocitace:
    print("Plichta!")
elif tah_pocitace and tah_cloveka == "nuzky":
    print("Pocitac vyhral!")
elif tah_cloveka and tah_cloveka == "papir":
    print("Vyhral jsi!")
else:
    print ("Nerozumim.")