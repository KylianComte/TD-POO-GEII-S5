class UserList :
    def __init__() :
        pass
    def __str__() :
        pass   
    def __len__() :
        pass
    def __getitem__() :
        pass
    def append() :
        pass
    def remove() :
        pass

class ListeNombresV2 (UserList):
    def __init__(self) :
        self.data = []
        self.nbElem = 0
    def __str__(self) :
        return ("[" + "|".join([str(x) for x in self.data]) + "]")    
    def __len__(self) :
        return self.nbElem
    def __getitem__(self,i) :
        if i < self.nbElem:
            return self.data[i-1]
        else:
            print("Error: The index is out of range.")
            return None
    def append(self,nb) :
        if type(nb) == int :
            self.data.append(nb)
            self.nbElem += 1
        else:
            print("Error: The value must be an integer.")
    def remove(self,nb) :
        if nb in self.data:
            while nb in self.data:
                self.data.remove(nb)
                self.nbElem -= 1
        else:
            print("Error: The value is not in the list.")

#Programme principal

maListe = ListeNombresV2()
maListe.append(10)
maListe.append(3)
maListe.append(5)
maListe.append(1)
maListe.append(5)

print(maListe)
len(maListe)
print(maListe[1])

# La facon d'invoquer la methode __str__, __len__ et __getitem__ est speciale car elle utilise des methodes natives de python (print, len, []).

maListe.remove(5)
print(maListe)