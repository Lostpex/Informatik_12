import random as rnd

gew_ohne_wechsel = gew_mit_wechsel = gew_zufMod = 0
sim = int(input("Wie viele Wiederholungen wollen sie Simulieren ? :"))
türen = {0, 1, 2}

for _ in range(sim):
  auto, wahl, moderator = rnd.randrange(3), rnd.randrange(3), rnd.randrange(3)
  if auto == wahl:
    gew_ohne_wechsel += 1
  ziege = (türen - {auto, wahl}).pop()
  wechsel = (türen - {wahl, ziege}).pop()
  if auto == wechsel:
    gew_mit_wechsel += 1
  if auto == moderator:
    gew_zufMod += 1
  else:
    wechsel = (türen - {wahl, moderator}).pop()
    if wechsel == auto:
      gew_zufMod += 1


print(f'Gewinnwahrscheinlichkeit ohne Wechsel = {gew_ohne_wechsel/sim*100:.2f} %')
print(f'Gewinnwahrscheinlichkeit mit Wechsel (Moderator zeigt Ziege)    = {gew_mit_wechsel/sim*100:.2f} %')
print(f'Gewinnwahrscheinlichkeit mit Wechsel (Moderator wählt zufällig) = {gew_zufMod/sim*100:.2f} %')