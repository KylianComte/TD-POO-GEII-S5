maListe = [10,3.14,"Paris",True]
it = iter(maListe)

for i in range(len(maListe)):
    print(next(it))

for element in maListe:
    print(element)

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
    def __iter__(self):
        for item in self.data:
            yield item