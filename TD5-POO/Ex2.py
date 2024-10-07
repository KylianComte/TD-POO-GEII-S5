import random
import time

class Subject ():
    def __init__(self):
        self.observers = []

    def addObserver(self,observer):
        self.observers.append(observer)
    
    def removeObserver(self,observer):
        self.observers.remove(observer)

    def notifyObservers(self,presence_detected):
        for observer in self.observers :
            observer.update(presence_detected)

class Observer ():
    def update():
        pass

class AppIoT (Observer):
    def update(self,presence_detected):
        if presence_detected == True :
            print("Présence détectée !")

class CapteurPresence (Subject):
    def __init__ (self,seuil):
        super().__init__()
        self.seuil = seuil
        self.pourcentage = 0

    def traiterImage(self):
        self.pourcentage = random.randint(0,100)
    
    def detecterMouvement(self):
        if self.pourcentage >= self.seuil :
            self.notifyObservers(True)


### Programme Principal ###

captpres = CapteurPresence(30)
appiot = AppIoT()

captpres.addObserver(appiot)

while True :
    captpres.traiterImage()
    captpres.detecterMouvement()

    time.sleep(2)