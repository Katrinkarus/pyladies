domaci_zvirata = ["pes", "kocka", "kralik", "had"]
# for zviera in domaci_zvirata:
#     if zviera[0] == "k":
#         print(zviera)
# #    if len(zviera) < 5:
# #         print(zviera)

# print(domaci_zvirata[0])

hadane_zviera = input("zadej nove zviera: ")
if hadane_zviera in domaci_zvirata:
    print("Ano je tam", hadane_zviera)
while hadane_zviera not in domaci_zvirata:
    if hadane_zviera in domaci_zvirata:
        print("Ano je tam", hadane_zviera)
    else: 
        hadane_zviera = input("zadej nove zviera: ")
        print("Nie je tam")