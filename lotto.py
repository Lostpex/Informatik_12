from random import randint, seed
seed()

simulationen = int(input("Wie viele simulationen möchtest du durchführen?: "))

# Funktion einer einzigen Ziehung und eines Tipps
def ziehung_und_tip():
    
    ziehung = []
    tip = []
    
    while len(tip) != 6:
        los = randint(1, 49)
        if los not in tip: 
            tip.append(los)

    while len(ziehung) != 6:
        zahl = randint(1, 49)
        if zahl not in ziehung:
            ziehung.append(zahl)
    #Anzahl der Richtigen
    treffer = len(set(ziehung) & set(tip))
    return treffer

def simulationen_haeufigkeit(simulationen):
    haeufigkeitsliste = [0] * 7  # Liste für Treffer von 0 bis 6

    for i in range(simulationen):
        # Führe eine Ziehung und einen Tipp aus und erhalte die Trefferanzahl
        treffer = ziehung_und_tip()
        
        # Aktualisiere die Häufigkeitsliste basierend auf den Treffern
        haeufigkeitsliste[treffer] += 1

    return haeufigkeitsliste


ergebnisse = simulationen_haeufigkeit(simulationen)

#Ergebnisse
print("Anzahl der Übereinstimmungen: " + str(ziehung_und_tip()))
print("Häufigkeitsliste für Treffer von 0 bis 6:")
print(ergebnisse)