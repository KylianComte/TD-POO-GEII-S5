import pickle
import json

dicoEtu = {
    'Nom': 'Jhon Doe',
    'Groupe': 'S5 POO',
    'Notes': [19,20,18,17,20]
}
pickleData = pickle.dumps(dicoEtu)
print(pickleData)
newDico1 = pickle.loads(pickleData)
print(newDico1)

class Etudiant:
    def __init__(self,nom,groupe):
        self.nom = nom
        self.groupe = groupe
        self.notes = []
    def ajouter_note(self,note):
        self.notes.append(note)
    def ajouter_notes(self,notes):
        self.notes += notes
    def __str__(self):
        return self.nom + " " + self.groupe + " " + str(self.notes)

etu = Etudiant("Jhon Doe","S5 POO")
etu.ajouter_notes([19,20,18,17,20])
"""
jsonEtu = json.dumps(etu) #TypeError: Object of type Etudiant is not JSON serializable
print(jsonEtu)

newEtu = json.loads(jsonEtu)
print(newEtu)
"""

class EtudiantEncoder(json.JSONEncoder):
    def default(self,objEtu):
        if isinstance(objEtu,Etudiant):
            return {
                'Nom': objEtu.nom,
                'Groupe': objEtu.groupe,
                'Notes': objEtu.notes
            }
        return json.JSONEncoder.default(self,objEtu)

jsonEtu = json.dumps(etu,cls=EtudiantEncoder)
print(jsonEtu)#{"Nom": "Jhon Doe", "Groupe": "S5 POO", "Notes": [19, 20, 18, 17, 20]}

newEtu = json.loads(jsonEtu)
print(newEtu)#{'Nom': 'Jhon Doe', 'Groupe': 'S5 POO', 'Notes': [19, 20, 18, 17, 20]}

#Fonctionne comme prevu mais newEtu est un dictionnaire et non un objet de type Etudiant

class EtudiantDecoder(json.JSONDecoder):
    def decode(self,jsonStr):
        dicoEtu = json.JSONDecoder.decode(self,jsonStr)
        etu = Etudiant(dicoEtu['Nom'],dicoEtu['Groupe'])
        etu.ajouter_notes(dicoEtu['Notes'])
        return etu

jsonEtu = json.dumps(etu,cls=EtudiantEncoder)
print(jsonEtu)#{"Nom": "Jhon Doe", "Groupe": "S5 POO", "Notes": [19, 20, 18, 17, 20]}

newEtu = json.loads(jsonEtu,cls=EtudiantDecoder)
print(newEtu)#Jhon Doe S5 POO [19, 20, 18, 17, 20]

#newEtu est bien un objet de type Etudiant