import math

class Point :
    def __init__(self) :
        self.x = 0
        self.y = 0
        self.ro = 0
        self.theta = 0
    def calculer_distance(self, p) :
        return math.sqrt((self.x - p.x)**2 + (self.y - p.y)**2)
    def calculer_ro_theta(self) :
        self.ro = math.sqrt(self.x**2 + self.y**2)
        self.theta = math.acos(self.x/self.ro)
    def setxy(self, x, y) :
        self.x = x
        self.y = y
    def calculer_x_y(self) :
        self.x = self.ro * math.cos(self.theta)
        self.y = self.ro * math.sin(self.theta)
    def setrotheta(self, ro, theta) :
        self.ro = ro
        self.theta = theta
    def afficher_coordonnees(self) :
        print("Coordonnées cartésiennes : (", self.x, ",", self.y, ")")
        print("Coordonnées polaires : (", self.ro, ",", self.theta, ")")


#programme principal

p1 = Point()
p2 = Point()

p1.setxy(2, -4)
p2.setrotheta(13, 0.5880026035475675)
p2.calculer_x_y()
print(p1.calculer_distance(p2))


