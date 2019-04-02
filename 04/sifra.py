import string
abeceda = string.ascii_lowercase
def odkoduj():
    key = int(input("Zadaj kluc: "))
    plaintext = input("Zadaj text: ").lower()
    ciphertext = ""

    for i in plaintext:
        if i in abeceda:
            pozicia = abeceda.find(i)
            nova_pozicia = (pozicia + key) % 26
            novy_charakter = abeceda[nova_pozicia]
            ciphertext += novy_charakter
        else:
            ciphertext += i
    print(ciphertext)

odkoduj()

# key = int(input("Zadaj kluc: "))
# plaintext = str(input("Zadaj text: "))
# male_abc = "abcdefghijklmnopqrstuvwxyz"
# posun = chr(ord(plaintext) + key)
# print(posun)