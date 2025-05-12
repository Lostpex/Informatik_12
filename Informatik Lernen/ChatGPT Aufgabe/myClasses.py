class Bankkonto(object):
    def __init__(self, kontonummer, besitzer, kontostand):
        self.kontonummer = kontonummer
        self.besitzer = besitzer
        self.__kontostand = kontostand
        
    def einzahlen(self, betrag):
        self.__kontostand = self.__kontostand + betrag
        
    def abheben(self, betrag):
        if betrag <= self.__kontostand:
            self.__kontostand = self.__kontostand - betrag
        else:
            print(f"Nicht genügend Guthaben")
            
    def get_Kontostand(self):
        return self.__kontostand
        
        