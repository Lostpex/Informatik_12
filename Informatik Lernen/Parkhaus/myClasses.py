class Parkplatz(object):
    def __init__(self, nummer, belegt):
        self.nummer = nummer
        self.belegt = bool(belegt)

    def  einparken(self):
        if not self.belegt:
            self.belegt = True
            print("Parkplatz ist jetzt belegt.")
            return True
        else:
            print("Parkplatz ist bereits belegt.")
            return False
        
    def  ausparken(self):
        if self.belegt:
            self.belegt = False
            print("Parkplatz ist jetzt frei.")
            return True
        else:
            print("Parkplatz ist bereits frei.")
            return False
        
    def status(self):
        if self.belegt:
            print("Parkplatz ist belegt.")
        else:
            print("Parkplatz ist frei.")
    

class Parkhaus(object):
    def __init__(self, anzahl):
        self.anzahl = anzahl
        self.liste = [Parkplatz(i + 1, False) for i in range(anzahl)]

    def zeige_freie_plaetze(self):
        for parkplatz in self.liste:  # Über die Liste der Parkplätze iterieren
            print(f"Nummer = {parkplatz.nummer}, Belegt: {parkplatz.belegt}")

    def einparken(self):
        for parkplatz in self.liste:
            if parkplatz.belegt == False:
                parkplatz.einparken()
                return 
            
    def ausparken(self, nummer):
        for parkplatz in self.liste:
            if parkplatz.nummer == nummer:
                parkplatz.ausparken()
                return 