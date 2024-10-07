import math
class Point :
    def __init__(self, abs, ord) :
        self.x = abs
        self.y = ord
    def calculer_distance(self, p) :
        return math.sqrt((self.x - p.x)**2 + (self.y - p.y)**2)
    def reset(self) :
        self.x = 0
        self.y = 0
    def distance_origine(self) :
        return self.calculer_distance(Point(0, 0))

#programme principal
p1 = Point(2, -4)
p2 = Point(12, 10)
dist = p1.calculer_distance(p2)
print(dist)

# Question n°1
#a) Le constructeur de la classe Point est la méthode __init__.
#b) La methode __init__ est appelée lors de la création d'un objet.
#c) Les attributs de la classe Point sont x et y et ses methodes sont __init__ et calculer_distance.
#d) Le mot clef self est utilisé pour faire référence à l'objet lui-même.
#e) Il doit etre dans les methodes pour pouvoir accéder aux attributs de l'objet.
#f) Le paramètre p de la méthode calculer_distance est un objet de la classe Point.
#g) On doit ecrire p1.calculer_distance(p2) pour appeler la méthode calculer_distance de l'objet p1.

# Quesiton n°3 

#nouveau programme principal
p1 = Point(2, -4)
p2 = Point(12, 10)
print(p1.distance_origine())
print(p2.distance_origine())