class Auto(object):
    def __init__(self, kennzeichen, marke, topSpeed):
        self.kennzeichen = kennzeichen
        self.tempo = 0
        self.marke = marke
        self.__topSpeed = topSpeed
        self.strecke = 0
        self.fahrtzeit = 0

    def beschleunigen(self, kmh):
        self.tempo = self.tempo + kmh
        if self.tempo > self.topSpeed:
            self.tempo = self.topSpeed

    def bremsen(self, kmh):
        self.tempo = self.tempo - kmh
        if self.tempo < 0:
            self.tempo = 0

    def fahren(self, zeit):
        self.strecke = self.strecke + self.tempo * zeit
        self.fahrtzeit = self.fahrtzeit + zeit

    def tunen(self, topSpeed):
        self.topSpeed = topSpeed

    def get_topSpeed(self):
        return self.__topSpeed
    
    def set_topSpeed(self, topSpeed):
        self.__topSpeed = topSpeed