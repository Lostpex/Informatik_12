from myClasses import Bankkonto

k1 = Bankkonto("123456789", "Max Mustermann", 0)
k2 = Bankkonto("987654321", "Erika Mustermann", 0)

k1.einzahlen(500)
k2.einzahlen(1000)

k1.get_Kontostand()
k2.get_Kontostand()

k1.abheben(499)
k2.abheben(999)

k1.get_Kontostand()
k2.get_Kontostand()

print(f"Kunde 1 hat {k1.get_Kontostand()} Euro auf dem Konto")
print(f"Kunde 2 hat {k2.get_Kontostand()} Euro auf dem Konto")