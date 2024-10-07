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

    def afficher_infos(self):
        super().afficher_infos()
        print("pos_charge_x : " + str(self.pos_charge_x))
        print("pos_charge_y : " + str(self.pos_charge_y))
        print("niveau_charge : " + str(self.niveau_charge))

    def nettoyer(self):
        print("Je nettoie !")

    def executer_tache(self):
        self.nettoyer()

class RobotAspirateur(RobotNettoyeur):
    def __init__(self, nom, vitesse_max, pos_charge_x, pos_charge_y):
        super().__init__(nom, vitesse_max, pos_charge_x, pos_charge_y)
        self.etat_reservoir = "vide"

    def aspirer(self):
        print("J'aspire !")

    def nettoyer(self):
        self.aspirer()

### Programme principal ###
robot_aspi1 = RobotAspirateur("Roomba",4,12,30)
robot_aspi1.afficher_infos()
robot_aspi1.nettoyer()