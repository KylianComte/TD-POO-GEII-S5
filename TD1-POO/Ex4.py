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

class triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    def calculer_perimetre(self):
        return self.p1.calculer_distance(self.p2) + self.p2.calculer_distance(self.p3) + self.p3.calculer_distance(self.p1)

#programme principal
p1 = Point()
p2 = Point()
p3 = Point()

p1.setxy(2, -4)
p2.setxy(12, 10)
p3.setxy(5, 7)

t = triangle(p1, p2, p3)
print(t.calculer_perimetre())