#Question n°1

maListe = [10,3.14,"Paris"]
print(maListe)
maListe.append(True)
print(len(maListe))
print(maListe[2])
maListe.remove("Paris")

#Question n°2

class ListeNombres:
    def __init__(self):
        self.data = []
        self.nbElem = 0
    def afficher(self):
        print("[" + "|".join([str(x) for x in self.data]) + "]")
    def ajouter(self, nb):
        if type(nb) == int :
            self.data.append(nb)
            self.nbElem += 1
        else:
            print("Error: The value must be an integer.")
    def element(self, i):
        if i < self.nbElem:
            return self.data[i-1]
        else:
            print("Error: The index is out of range.")
            return None
    def longueur(self):
        return self.nbElem
    def enlever(self,nb):
        if nb in self.data:
            while nb in self.data:
                self.data.remove(nb)
                self.nbElem -= 1
        else:
            print("Error: The value is not in the list.")