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


class Welt(object):
    def __init__(self,x,y):
        self.felderX = x
        self.felderY = y
        self.ziegel =[]

    def getFelderX(self):
        return self.felderX
    
    def getFelderY(self):
        return self.felderY
    
    def incZigel(x,y):
        return
    def decZigel(x,y):
        return
    

w = Welt(10,10)
r1 = Roboter()