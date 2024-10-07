import math

def calculer_distance(xa, ya, xb, yb) :
    return math.sqrt((xa - xb)**2 + (ya - yb)**2)

#programme principal
x1 = 2
y1 = -4
x2 = 12
y2 = 10
dist = calculer_distance(x1, y1, x2, y2)
print("La distance entre les points A et B est de", dist)

# Question n°2
# La ligne import math permet d'importer le module math qui contient des fonctions mathématiques.
# Le mot def est utilisé pour définir une fonction.
# Il y'a 5 variables dans ce programme : x1, y1, x2, y2 et dist.
# La variable dist sers à stocker la valeur de la distance entre les points A et B.
# Il est possible de ne pas utiliser de variable pour stocker la distance entre les points A et B en ecrivant directement print("La distance entre les points A et B est de", calculer_distance(x1, y1, x2, y2))
# Une definition de fonction est une suite d'instructions qui effectue une tâche ou calcule une valeur.
# Un appel de fonction est une instruction qui demande à une fonction de s'exécuter.
# A l'appel du programme, la valeur affichée est 17.204650534085253

def calculer_distance_origine(x, y) :
    return calculer_distance(0, 0, x, y)
