from TK import Tinker


class Roboter(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.r = 'S'

    def schritt(self):
        if self.x < w.felderX or self.y < w.felderY:
            if self.r == 'O' and self.x < w.felderX:
                self.x = self.x + 1
            elif self.r == 'W' and self.x < w.felderX:
                self.x = self.x - 1
            elif self.r == 'S' and self.y < w.felderY:
                self.y = self.y + 1
            elif self.r == 'N' and self.y < w.felderY:
                self.y = self.y - 1
            else:
                print("Weltende erreicht...")
        else:
            print("Weltende erreicht...")

    def rechts(self):
        if self.r == 'O':
            self.r = 'S'
        elif self.r == 'S':
            self.r = 'W'
        elif self.r == 'W':
            self.r = 'N'
        elif self.r == 'N':
            self.r = 'O'

    def links(self):
        if self.r == 'O':
            self.r = 'N'
        elif self.r == 'S':
            self.r = 'O'
        elif self.r == 'W':
            self.r = 'S'
        elif self.r == 'N':
            self.r = 'W'

    def ziegelHinlegen(self):
        if self.r == 'O' and self.x < self.w.getFelderX()-1:
            self.w.incZiegel(self.x+1, self.y)
        elif self.r == 'S' and self.y < self.w.getFelderY()-1:
            self.w.incZiegel(self.x, self.y+1)
        elif self.r == 'W' and self.x > 0:
            self.w.incZiegel(self.x-1, self.y)
        elif self.r == 'N' and self.y > 0:
            self.w.incZiegel(self.x, self.y-1)

    def ziegelAufheben(self):
        if self.r == 'O' and self.x < self.w.getFelderX()-1:
            self.w.decZiegel(self.x+1, self.y)
        elif self.r == 'S' and self.y < self.w.getFelderY()-1:
            self.w.decZiegel(self.x, self.y+1)
        elif self.r == 'W' and self.x > 0:
            self.w.decZiegel(self.x-1, self.y)
        elif self.r == 'N' and self.y > 0:
            self.w.decZiegel(self.x, self.y-1)


class Welt(object):
    def __init__(self,x,y):
        self.felderX = x
        self.felderY = y
        self.ziegel =[]

    # Erzeugung der Listen
        l = []
        for i in range(self.felderY):
            m = []
            for j in range(self.felderX):
                m = m + [0]
            l = l + [m]
        self.ziegel = l

    def getFelderX(self):
        return self.felderX

    def getFelderY(self):
        return self.felderY

    def incZiegel(self, x, y):
        self.ziegel[y][x] = self.ziegel[y][x] + 1

    def decZiegel(self, x, y):
        if self.ziegel[y][x] > 0:
            self.ziegel[y][x] = self.ziegel[y][x] - 1

    def getZiegel(self, x, y):
        return self.ziegel[y][x]

    def getAlleZiegel(self):
        return self.ziegel
    

w = Welt(10,10)
r1 = Roboter()

