import random
import time

class Subject ():
    def __init__(self):
        self.observers = []

    def addObserver(self,observer):
        self.observers.append(observer)
    
    def removeObserver(self,observer):
        self.observers.remove(observer)

    def notifyObservers(self,presence_detected,info):
        for observer in self.observers :
            observer.update(presence_detected,info)

class Observer ():
    def update():
        pass

class AppIoT (Observer):
    def update(self,presence_detected,info):
        if presence_detected == True :
            print("Présence détectée !","|", info)

class AppSecu (Observer):
    def update(self,presence_detected,info):
        if presence_detected == True :
            print("Alerte","|", info)

class Piece ():
    def __init__ (self, numero, surface):
        self.numero = numero
        self.surface = surface

    def __str__(self) :
        return("Salle n°"+str(self.numero)+" de surface "+str(self.surface)+" m²")

class CapteurPresence (Subject):
    def __init__ (self,seuil,piece):
        super().__init__()
        self.seuil = seuil
        self.pourcentage = 0
        self.piece = piece

    def traiterImage(self):
        self.pourcentage = random.randint(0,100)
    
    def detecterMouvement(self):
        if self.pourcentage >= self.seuil :
            self.notifyObservers(True, self.piece)


### Programme Principal ###

appiot = AppIoT()
appsecu = AppSecu()
salle12 = Piece(12,40)
salle15 = Piece(15,30)
salle25 = Piece(24,38)

captpres12 = CapteurPresence(30,salle12)
captpres15 = CapteurPresence(30,salle15)
captpres25 = CapteurPresence(30,salle25)

captpres12.addObserver(appiot)
captpres12.addObserver(appsecu)
captpres15.addObserver(appiot)
captpres15.addObserver(appsecu)
captpres25.addObserver(appiot)
captpres25.addObserver(appsecu)


while True :
    captpres12.traiterImage()
    captpres12.detecterMouvement()
    captpres15.traiterImage()
    captpres15.detecterMouvement()
    captpres25.traiterImage()
    captpres25.detecterMouvement()

    time.sleep(2)