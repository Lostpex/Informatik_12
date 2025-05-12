class Onlineshop(object):
    def __init__(self, name, preis, anzahl):
        self.name = name
        self.preis = float(preis)
        self.anzahl = anzahl

    def verkaufen(self, menge):
        if menge > self.anzahl:
            print("Nicht genug Artikel auf Lager.")
            return False
        else:
            self.anzahl -= menge
            print(f"{menge} Artikel verkauft.")
            return True
        
    def auffuellen(self, menge):
        self.anzahl += menge
        print(f"{menge} Artikel aufgefüllt.")

    def info(self):
        return self.name, self.preis, self.anzahl