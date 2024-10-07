class Robot () :
    def __init__ (self, nom, vitesse_max) :
        self.nom = nom
        self.vitesse_max = vitesse_max

    def afficher_infos(self):
        print("Nom : " + self.nom)
        print("Vitesse max : " + str(self.vitesse_max))

class RobotNettoyeur(Robot) :
    def __init__ (self,nom, vitesse_max, pos_charge_x, pos_charge_y) :
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