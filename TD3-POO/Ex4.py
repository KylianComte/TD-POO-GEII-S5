import math

class Robot():
    def __init__(self, nom, vitesse_max):
        self.nom = nom
        self.vitesse_max = vitesse_max

    def afficher_infos(self):
        print("Nom : " + self.nom)
        print("Vitesse max : " + str(self.vitesse_max))

    def executer_tache(self):
        pass


class RobotNettoyeur(Robot):
    def __init__(self, nom, vitesse_max, pos_charge_x, pos_charge_y):
        super().__init__(nom, vitesse_max)
        self.pos_charge_x = pos_charge_x
        self.pos_charge_y = pos_charge_y
        self.niveau_charge = 0
        self.salle=0

    def afficher_infos(self):
        super().afficher_infos()
        print("pos_charge_x : " + str(self.pos_charge_x))
        print("pos_charge_y : " + str(self.pos_charge_y))
        print("niveau_charge : " + str(self.niveau_charge))
        if self.salle != 0 :
            print("Le robot est associé à la salle n°", self.salle.numero)
            print("La salle n°",self.salle.numero," fait ",self.salle.surface," m²" )
        else :
            print("ce robot n'est pas associé à une salle")


    def nettoyer(self):
        print("Je nettoie !")

    def executer_tache(self):
        self.nettoyer()

    def affecter_salle(self,salle):
        self.salle = salle


class RobotAspirateur(RobotNettoyeur):
    def __init__(self, nom, vitesse_max, pos_charge_x, pos_charge_y):
        super().__init__(nom, vitesse_max, pos_charge_x, pos_charge_y)
        self.etat_reservoir = 0

    def aspirer(self):
        print("J'aspire !")

    def nettoyer(self):
        self.aspirer()

class RobotRondier(Robot) :
    def __init__(self, nom, vitesse_max):
        super().__init__(nom,vitesse_max)
        self.alerte = False

    def executer_tache(self):
        print("Je fais ma ronde !")

class RobotSerpillere(RobotNettoyeur) :
    def executer_tache(self):
        print("Je serpille !")

class Salle() :
    def __init__(self, numero, surface):
        self.numero = numero
        self.surface = surface

### Prog principal ###

liste_robot = []
liste_salles = []

for i in range(10):
    liste_robot.append(RobotAspirateur("Roomba n°"+str(i), i+1, i, 9-i))
    liste_salles.append(Salle(i+1, i**2))

for i in range(len(liste_robot)):
    liste_robot[i].affecter_salle(liste_salles[i])

for robot in liste_robot:
    robot.afficher_infos()
