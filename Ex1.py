class Robot() :
    def __init__ (self, nom, vitesse_max) :
        self.nom = nom
        self.vitesse_max = vitesse_max

    def afficher_infos(self):
        print("Nom : " + self.nom)
        print("Vitesse max : " + str(self.vitesse_max))

class RobotNettoyeur(Robot) :
    def nettoyer(self):
        print("Je nettoie !")

### Prog principal ###

robot1 = Robot("robot 1",5)
robot_nettoyeur1 = RobotNettoyeur("robot nettoyeur 1",2)

robot1.afficher_infos()
robot_nettoyeur1.afficher_infos()

robot_nettoyeur1.nettoyer()