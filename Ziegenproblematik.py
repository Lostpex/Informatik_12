from random import randint, seed
seed()
tuerZiege = 0
# Schritt 1: Auto wird versteckt
tuerAuto = randint(1, 3)
# Schritt 2: Kandidat waehlt eine Tuer aus
tuerKandidat = int(input('Wähle eine Tür (1, 2, 3): '))
# Schritt 3: Moderator oeffnet eine Tuer
if tuerAuto == 1:
    if randint(1,2) == 1:
         print("Tür 2 ")
         tuerZiege += 2
    else:
        print("Tür 3 ")
        tuerZiege += 3
    
if tuerAuto == 2:
    if randint(1,2) == 1:
         print("Tür 1 ")
         tuerZiege += 1
    else:
        print("Tür 3 ")
        tuerZiege += 3
if tuerAuto == 3:
    if randint(1,2) == 1:
         print("Tür 1 ")
         tuerZiege += 1
    else:
        print("Tür 2 ")
        tuerZiege += 2


print('Hinter Tür', tuerZiege, 'befindet sich eine Ziege!')
# Schritt 4: Kandidat waehlt erneut eine Tuer aus
print('Willst du bei deiner Wahl bleiben oder umwählen?')
tuerKandidat = int(input('Wähle eine Tür (1, 2, 3): '))
# Schritt 5: Gewinn wird ermittelt
if tuerAuto == tuerKandidat:
    print('Du hast ein Auto gewonnen! :) ')
else:
    print('Du hast verloren! :( ')