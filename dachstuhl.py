import math
"""
#Giebel redchnung
a = float(input("Die Breite des Hauses : "  ))
b = float(input("Länge der Höhe des Giebels : "  ))

c = (a * b) / 2

print(f"Flächeninhalt des Dachgiebels beträgt: " + str(round((c), 2))+ " m^2")
"""
"""
#Dachsparren
d=float(input("Länge von a: "))
e=float(input("Länge von b: "))

f = d*d + e*e
f = math.sqrt(f)

print(f"Die länge der Dachsparrenbeträgt : " + str(round((f), 2))+ " m")
"""
breite = float(input("Die Breite des Hauses : "  ))
laenge = float(input("Die Länge des Hauses : "  ))
hoehe = float(input("Die Höhe des Hauses (ohne Dachhöhe): "  ))
dachhoehe = float(input("Die Dachhöhe des Hauses : "  ))

#Rechnung
ergebnis =((laenge * hoehe)*2) + ((breite*hoehe)*2) + (breite * dachhoehe) + math.sqrt(((((breite/2)*(breite/2))+math.sqrt(hoehe+hoehe)) * laenge)*2)

print("Die Gesamtoberfläche des Hauses beträgt" + str(ergebnis))