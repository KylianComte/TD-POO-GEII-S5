import math

def calculer_perimetre(rayon):
    return 2 * math.pi * rayon

def calculer_aire(rayon):
    return math.pi * rayon**2

#Programme principal
rayon = float(input("Entrez le rayon du cercle: "))
perimetre = calculer_perimetre(rayon)
aire = calculer_aire(rayon)
print(f'Le rayon du cercle : {rayon}')
print(f'Le perimetre du cercle : {perimetre}')
print(f'L aire du cercle : {aire}')

#Question 1
class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def calculer_perimetre(self):
        return 2 * math.pi * self.rayon

    def calculer_aire(self):
        return math.pi * self.rayon**2
    
    def afficher(self):
        print(f'Le rayon du cercle : {self.rayon}')
        print(f'Le perimetre du cercle : {self.calculer_perimetre()}')
        print(f'L aire du cercle : {self.calculer_aire()}')

#Programme principal question 2
cercle = Cercle(1)
cercle.afficher()