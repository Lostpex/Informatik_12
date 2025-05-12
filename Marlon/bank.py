class Bank(object):
    def init(self, kontonummer, besitzer, kontostand):
        self.kontonummer = kontonummer
        self.besitzer = besitzer
        self.kontostand = kontostand

    def einzahlen(self, betrag):
        self.kontostand = self.kontostand + betrag

    def abheben(self, betrag):
        if self.kontostand >= betrag():
            self.kontostand = self.kontostand - betrag
        else: 
            print("Sie haben nicht genug Geld")

    def get_kontostand(self):
        return self.kontostand