import numpy.random as npr # npr.randint()
from collections import Counter

def fct_occ(tableau):
    print(tableau)
    counter = Counter(tableau)
    return counter

# Un carré - Vérification de 4 valeur identique avec If
# Un full - Vérification des 3 dés avec une boucle conditionnelle if. De même avec les 2 dés.
# Une Petite Suite - Vérification de l'égalité des valeurs entre deux listes

petiteSuite=[1,2,3,4,5]
somme=0
itr=10000

for i in range(0,itr+1):
    tab=[]
    for j in range(0,7):
        tab.append(npr.randint(0,7))
    if()
    print(tab)


moyenne=somme/itr
