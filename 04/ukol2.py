
kosik = {"jablko": "cervene", "hruska": "zelena", "broskev": "oranzova", "baban": "zluty"}

shnile = {}

for ovoce, barva in kosik.items():
    shnile[ovoce] = "hnedo-{}".format(barva)

print(shnile)