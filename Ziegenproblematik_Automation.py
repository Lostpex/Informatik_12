import random
from random import randint, seed
seed()
türZiege = 0
gewonnen = 0
verloren = 0

türen = [1,2,3]
a = [1,2]

wiederholungen = int(input("Wie viele Simulationen sollen durchgeführt werden ?:  "))

for i in range(wiederholungen):

    türAuto = random.choice(türen)

    türKandidat = random.choice(türen)

    if türAuto == 1:
        if random.choice(a) == 1:
            türZiege += 2

        else:

            türZiege += 3

        if türAuto == 2:

            if random.choice(a) == 1:

                 türZiege += 1
            else:
                türZiege += 3

        if türAuto == 3:
            if random.choice(a) == 1:

                 türZiege += 1

            else:

                türZiege += 2


#Entfernen der geöfneten tür
    if türZiege in türen:
        türen.remove(türZiege)

    türKandidat_neu = random.choice(türen)

    if türAuto == türKandidat_neu:
        gewonnen += 1
    else:
        verloren += 1

print("Gewinne: " + str(gewonnen))
#print(gewonnen)
print("Eine Gewinnrate von: ")
print(str(gewonnen/wiederholungen*100) + "%")


print("Niederlagen: " + str(verloren))
#print(verloren)
print("Eine Niederlagenrate von: ")
print(str(verloren/wiederholungen*100) + "%")
