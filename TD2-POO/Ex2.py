import math

class Robot :
    def __init__(self, vitesse_max, nom_robot, posx, posy):
        self.nom_robot = nom_robot
        self.vitesse_max = vitesse_max
        self.posx = posx
        self.posy = posy
    def calculer_temps(self, posx, posy):
        distance = math.sqrt((posx - self.posx)**2 + (posy - self.posy)**2)
        return distance / self.vitesse_max

#Programme principal
robot1 = Robot(2, "Rapidor", 0, 0)
robot2 = Robot(0.5, "Escargor", 0, 0)
temps1 = robot1.calculer_temps(12, 5)
temps2 = robot2.calculer_temps(12, 5)
if temps1 < temps2:
    print("Rapidor est le plus rapide")
else:
    print("Escargor est le plus rapide")