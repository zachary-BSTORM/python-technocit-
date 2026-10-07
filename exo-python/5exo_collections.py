"""
exo23-Écrire un algorithme demandant à l’utilisateur le nombre de joueurs (max 10
joueurs). Ensuite, l’algorithme doit demander à l’utilisateur le score de chaque
joueur. Une fois ceci fini, il faut afficher la moyenne des scores. Faites de même en
Python
"""
nb_joueurs = 0
scores = []
total = 0

while 1 > nb_joueurs or nb_joueurs > 10 :
    nb_joueurs = int(input("Entrez le nombre de joueurs entre 1 et 10 :"))

for i in range(nb_joueurs):
    score = int(input(f"Entrez le score du joueurs {i + 1} : "))
    scores.append(score)
    
for s in scores:
    total += s
    
print(f"La moyenne est de {total / nb_joueurs}")

"""
• exo24-Inverser un tableau : soit un tableau T. Saisir ce tableau. Changer de place les
éléments de ce tableau de façon à ce que le nouveau tableau soit une sorte de miroir
de l'ancien et afficher le nouveau tableau.
"""
tab_base = []
tab_reversed = []
index_reverse = 0

for i in range(10):
    valeur = int(input(f"Entrez la valeur {i + 1} : "))
    tab_base.append(valeur)

# exemple 1  
# for i in reversed(tab_base):
#     tab_reversed.append(i)
# exemple 2

tab_reversed = tab_base[::-1]
    
for v in tab_base:
    print(f"base : {v}" , end="")

for v in tab_reversed:
    print(f"reverse : {v}" , end="")

"""
• exo25-À l’aide des boucles, réalisez un algorithme permettant de trier un tableau
d’entiers dans l’ordre croissant. Mettez-le ensuite en pratique avec le Python.
"""
def quick_sort(liste_value):
    if len(liste_value) <= 1:
        return liste_value
    
    pivot = liste_value.pop()
    petit = []
    grand = []
    
    for v in liste_value:
        if v < pivot:
            petit.append(v)
        else:
            grand.append(v)
            
    return quick_sort(petit) + [pivot] + quick_sort(grand)

values = [6,45,6,465,46,87,6,7,695,7,687,6,76,87,68,7,687,68,43,5,787]

print(quick_sort(values))


"""
exo26-En considérant deux tableaux d'entiers (non triés), réalisez un algorithme qui
place tous les éléments des deux tableaux dans un troisième. Ce dernier doit être
trié une fois l'algorithme terminé. Notez que le tri doit être fait en même temps que
la fusion des deux tableaux et pas après. (Indice : tab.reverse())
"""
tab_1 = [54,45,68,54,2,14,1,45,100]
tab_2 = [12,45,89,96,36,64]
tab_fusion = []

# def fusion_tri(tab_1 : list[int], tab_2: list[int]) -> list[int]:
    
#     tab_fusion = []
    
#     if len(tab_1) == 0 and len(tab_2) == 0:
#         return tab_fusion
#     elif len(tab_2) == 0 and len(tab_1) > 0:
#         while len(tab_1):
#             bigger = max(tab_1)
#             tab_1.remove(bigger)
            
#             tab_fusion.append(bigger)
#     elif len(tab_1) == 0 and len(tab_2) > 0:
#         while len(tab_2):
#             bigger = max(tab_2)
#             tab_2.remove(bigger)
            
#             tab_fusion.append(bigger)
            
#     else:
#         while len(tab_1) > 0 or len(tab_2) > 0:

#             if len(tab_1) == 0:
#                 bigger = max(tab_2)
#                 tab_2.remove(bigger)
#             elif len(tab_2) == 0 :
#                 bigger = max(tab_1)
#                 tab_1.remove(bigger)
#             elif max(tab_1) > max(tab_2):
#                 bigger = max(tab_1)
#                 tab_1.remove(bigger)
#             else:
#                 bigger = max(tab_2)
#                 tab_2.remove(bigger)
                
#             tab_fusion.append(bigger)
        
#     tab_fusion.reverse()

#     return tab_fusion

# result = fusion_tri(tab_1,tab_2)

# for v in result:
#     print(v)
    
    
def quick_sort(tab_1:list[int],tab_2:list[int] = None) -> list[int]:
    pivot = None
    petit = []
    grand = []
    
    if tab_2 is not None:

        pivot = tab_2.pop()
        
        for v in tab_1:
            if v < pivot:
                petit.append(v)
            else:
                grand.append(v)
        
        for v in tab_2:
            if v < pivot:
                petit.append(v)
            else:
                grand.append(v)
                
        return quick_sort(petit) + pivot + quick_sort(grand)
    else:
        if len(tab_1) <= 0:
            return tab_1
        
        
        pivot = tab_1.pop()
        
        for v in tab_1:
            if v < pivot:
                petit.append(v)
            else:
                grand.append(v)
                
        return quick_sort(tab_1=petit) + [pivot] + quick_sort(tab_1=grand)
    

tab_fusion = quick_sort(tab_1=tab_1,tab_2=tab_2)

for v in tab_fusion:
    print(v)


"""
• exo27-Réalisez un algorithme nous permettant de déplacer un pion dans un tableau
de 10 éléments. Au début, le pion se trouve dans la première case du tableau. Nous
pouvons ensuite le déplacer par la gauche (g), par la droite (d) ou de stopper
l'algorithme (q) (Indice : l'exo doit être exécuté dans la console Windows).
"""
import os

plate = [[0] * 10 for _ in range(10) ]

x = 0
y = 0

plate[0][0] = 1

direction = ""

while direction != "q":
    os.system('cls')    
    for l in plate:
        print(l)
        
    
    direction = input("Entrez une direction : Z : haut , S : bas , Q : gauche , D : droite : ").strip().upper()
    
    plate[x][y] = 0
    match direction:
        case "Z":
            if x > 0:
                x -= 1            
        case "S":
            if x < 9:
                x += 1
        case "Q":
            if y > 0:
                y -= 1
        case "D":
            if y < 9:
                y += 1
        case "q":
            print("Merci au revoir")
            
    plate[x][y] = 1


"""
• exo28-Réalisez un algorithme permettant de rechercher une valeur dans un tableau.
Si la valeur se trouve bien dans la tableau, nous affichons sa position.
"""
tab_find_value = [1,2,3,4,5,6]

def find_index(value:int,liste:list[int]):

    for i in range(0,len(liste)):
        if liste[i] == value:
            return i
        

position = find_index(5,tab_find_value)

print(position)

"""
exo29-Refaites l'algorithme qui demande à l’utilisateur de taper 10 entiers et qui
affiche le plus petit de ces entiers mais cette fois-ci à l'aide d'un tableau et sans
retenir le minimum lors de la saisie.
"""

tab_29 = [12,54,1,24,89,63,3]

for i in range(10):
    value = int(input(f"Entrez une valeur {i} :"))
    tab_29.append(value)
    
min = 9999
for v in tab_29:
    if v < min:
        min = v
        
print(min)


"""
• exo30-En considérant un tableau d'entiers trié dans l'ordre croissant, réaliser un
algorithme étant capable d'insérer une nouvelle valeur dans le tableau de façon à ce
que la tableau reste trié. Le but n'est évidemment pas d'insérer la valeur à la fin et
de trier après mais bien de l'insérer au bon endroit directement.
"""
tab_30 = [1,2,3,4,5,7,8,9,10]


valeur = int(input("Entrez la valeur à ajouter : "))

position = 0

while position < len(tab_30) and tab_30[position] < valeur:
    position += 1
    
tab_30.insert(position,valeur)

for v in tab_30:
    print(v , end=" ")

"""
• exo31-Réalisez un algorithme dans lequel nous devons rechercher une valeur (entrée
par l'utilisateur) dans un tableau d'entiers.
"""

tab_31 = [1,2,3,4,5,7,8,9,10]


def verify(liste : list[int],value : int) -> bool:
    
    if value is None:
        return False
    
    if liste is None:
        return False
    
    for v in liste:
        if v == value:
            return True
        
    return False

def verify_2(liste : list[int],value : int) -> bool:
    set_test = set(liste)
    
    if value in set_test:
        return True
    return False
    
print(verify(tab_31,15))
print(verify_2(tab_31,15))

"""
exo33-Réalisez une fonction de recherche dans un tableau. Cette
fonction va recevoir un tableau, la taille du tableau, et la valeur
recherchée en paramètres et renvoyer l’indice de l’élément dans le
tableau. Si l’élément ne s’y trouve pas, la fonction renvoie -1.
"""


tab_find_value = [1,2,3,4,5,6]

def find_index(value:int,liste:list[int]):

    for i in range(0,len(liste)):
        if liste[i] == value:
            return i
    return -1