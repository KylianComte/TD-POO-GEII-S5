import random
import time

class CapteurPresence ():
    def __init__ (self,seuil):
        self.seuil = seuil
        self.pourcentage = 0

    def traiterImage(self):
        self.pourcentage = random.randint(0,100)
    
    def detecterMouvement(self):
        if self.pourcentage >= self.seuil :
            return True
        else :
            return False

### Prog Principal ###

capPresence = CapteurPresence(30)

while True :
    capPresence.traiterImage()
    if capPresence.detecterMouvement() == True :
        print("Mouvement détecté !")
    time.sleep(2)

