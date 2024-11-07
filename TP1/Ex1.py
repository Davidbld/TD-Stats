import numpy.random as npr # npr.randint()
from collections import Counter

def fct_occ(tableau):
    print(tableau)
    counter = Counter(tableau)
    return counter

# Génération d'un tableau binaire de taille 10
tableauBinaire=[]
for i in range (0,11):
   tableauBinaire.append(npr.randint(0,2))

# Génération d'un tableau de valeur aléatoire allant de 0 à 6 et de taille 6
tab=[]
for i in range(0,7):
    tab.append(npr.randint(0,7))

# Affichage du nombre d'itérations des valeurs du tableau binaire
iterationTab=fct_occ(tableauBinaire)
print(iterationTab)

# Affichage du nombre d'itérations des valeurs du tableau aléatoire
iterationTabAleatoire=fct_occ(tab)
print(iterationTabAleatoire)
