text = "Hallo Welt"

rev_text = ""

for i in text:
    rev_text = text[0]
    #rev_text = text[::-1]


print(rev_text)





# Text teilweise rückwärts ausgeben
text = 'Montag'
textNeu = ''
textNeu = text[0] + textNeu
textNeu = text[1] + textNeu
textNeu = text[2] + textNeu
print(textNeu)

# Text mit Schleife rückwärts ausgeben
text = 'Montag'
textNeu = ''
for i in range(len(text)):
    textNeu = text[i]+textNeu
print(textNeu)

# Algorithmus zur Verschlüsselung
text = input("Geben Sie einen Text ein: ")
blocklaenge = int(input("Geben Sie eine Blocklänge ein: "))
text = text.lower().replace(" ","")
restText = text
neuerText = ""


while len(restText) > 0:
    teilwort = restText[0:blocklaenge]
    restText = restText[blocklaenge:]
    umkehrung = ''
    for i in range(len(teilwort)):
        umkehrung = teilwort[i]+umkehrung
    if len(neuerText)==0:
        neuerText = umkehrung
    else:
        neuerText = neuerText + ' ' + umkehrung
print(neuerText)