from kartenspiel import *
# Testprogramm
spiel = True
kartenstapel = Kartenstapel()
kartenstapel.mischen()
kartenhaufen = Kartenhaufen()

print("Herzlich willkommen bei Black Jack! Sie bekommen zu Beginn zwei Karten.")
for i in range(2):
    gezogeneKarte = kartenstapel.karteZiehen()
    kartenhaufen.hinzufuegen(gezogeneKarte)
print("Sie haben folgende Karten gezogen: ",kartenhaufen.kartenListe)
print("Die Karten haben einen Wert von: ",kartenhaufen.wert)
while spiel:
    karte = input("Möchten Sie noch eine Karte ziehen? (ja/nein) ")
    if karte == "ja":
        gezogeneKarte = kartenstapel.karteZiehen()
        kartenhaufen.hinzufuegen(gezogeneKarte)
        print("Sie haben folgende Karten gezogen: ",kartenhaufen.kartenListe)
        print("Die Karten haben einen Wert von: ",kartenhaufen.wert)
        if kartenhaufen.wert > 21:
            print("Du hast leider verloren.")
            spiel = False
    else:
        spiel = False


"""
Schreiben Sie ein Testprogramm, dass Sie 17 und 4 spielen lässt. Nutzereingaben
sollen darüber entscheiden, ob Sie noch eine Karte ziehen oder nicht und benutzer-
freundliche Ausgaben sollen Sie nach jeder gezogenen Karte über ihre Kartenliste sowie
Ihren Kartenwert informieren. Wenn Sie am Ende über 21 Punkte haben, soll
das Programm ausgeben, dass Sie verloren haben.
"""