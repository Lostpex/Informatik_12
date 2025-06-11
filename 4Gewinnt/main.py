from random import randint

class Player(object):
    def __init__(self, name="", playerID="", gameMode=0):
        
        self.name = name
        self.playerID = playerID
        self.gameMode = gameMode

    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name

    def getPlayerID(self):
        return self.playerID
    
    def setPlayerID(self, playerID):
        self.playerID = playerID

    def getGameMode(self):
        return self.gameMode
    
    def playDraw(self, game):
        pass#########

class Field(object):
    def __init__(self):
        self.fields = []
        self.lastRow = 0
        self.lastCol = 0

    def getFields(self):
        return self.fields
    
    def setFields(self):
        pass#############

    def getLastRow(self, col, row):
        pass#############

    def getLastCol(self):
        pass#############

    