# moje riešenie z hodiny
from math import pi
def obsah_elipsy(osa_a, osa_b):
    "Vrati obsah elipsy daných rozmerov"
    return pi * (osa_a * osa_b)
    
print(obsah_elipsy(5,3))
# riešenie z hodiny
elipsa = obsah_elipsy(3,5)
print(elipsa)
def objem_eliptickeho_valce(obsah_elipsy, vyska):
    return obsah_elipsy * vyska

print(objem_eliptickeho_valce(elipsa,3))
# riešenie z hodiny 2
def objem_eliptickeho_valce(a, b, vyska):
    return obsah_elipty(a, b) * vyska

print(obejm_eliptickeho_valce(3, 5, 3))


