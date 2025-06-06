from auto import Auto

a1 = Auto("M-AB 123", "BMW", 250)
a2 = Auto("M-XY 456", "Audi", 280)

a1.beschleunigen(100)
a1.fahren(1)
a1.bremsen(20)
a1.fahren(2)


a1.bremsen(a1.tempo)
while a2.strecke < a1.strecke:
    a2.beschleunigen(10)
    a2.fahren(1)

#Ergebnis
print(f"Auto 1 hat eine Strecke von {a1.strecke} km zurückgelegt in {a1.fahrtzeit} h zurückgelegt..")
print(f"Auto 1 hat eine Strecke von {a2.strecke} km zurückgelegt in {a2.fahrtzeit} h zurückgelegt..")