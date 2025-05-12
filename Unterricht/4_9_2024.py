from random import randint

Zahl = 1
Kopf = 0

while True:
    eingabe = input("Bitte gegen sie die Variablen für Kopf (k) und Zahl (z) ein:").upper
    if eingabe == "K" or "Z":
        break

zufalsZahl = randint(0,1)

if zufalsZahl == 1:
    print("Zahl hat gewonnen")
    seite = "Z"
if zufalsZahl == 0:
    print("Kopf hat gewonnen")
    seite = "K"

if eingabe != seite:
    win = "nicht"
else:
    win = ""

print("Sie haben " + win + " gewonnen")
