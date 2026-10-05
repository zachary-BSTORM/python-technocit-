"""
exo13-À l’aide d’une boucle, afficher la table de multiplication par 2. 
Ensuite, coder votre algorithme en Python.
- récupérer la table à afficher 
- récupérer le nombre d'éléments à afficher
"""
table = int(input("Entrez la table à afficher : "))
nb = int(input("Indiquez le nombre d'opérations : "))

for i in range(1,nb + 1):
    print(f" {i} * {table} = {i * table}")


"""
exo14-Reprenez l’algorithme du lanceur de balles de tennis et
faites en sorte qu’il lance une balle tant que le stock n’est pas vide.
Il y a donc 2 variables stock_balles et pret , panier_vide

- afficher à chaque balle lancé le nombre de balle restante
- afficher un message lors de l'arret
"""
panier_vide = True
user_ready = False

stock_balles = None
input_user = None


input_user = input("Etes vous prêt ? : y - n")

if input_user == "y":
    user_ready = True
    
stock_balles = int(input("Combien de balles avez vous mis dans la machine ? : "))

if stock_balles > 0:
    panier_vide = False
    
while stock_balles > 0 and user_ready == True:
    print("Balle lancé")
    stock_balles -= 1
    print(f"Il reste {stock_balles} balles")


"""
• exo15-À l’aide de deux boucles, 
afficher les tables de multiplication de 1 à 9. 
Ensuite, coder votre algorithme en Python.
"""
for i in range(1 , 11):
    print(f"Table de {i}")
    for j in range(1,11):
        print(f" {i} * {j} = {i * j}")
    print("=============================")


"""
Jeu du plus ou moins

Génération d'un nombre aléatoire 
- from random import randint
result = randint(1,10)

dans une boucle 
    - demander à l'utilisateur d'entrez une valeur
    - afficher plus ou moins 
    - compter le nombre coups
    
    - afficher un message lorsqu'il à trouvez le nombre avec le nombre de coups
"""
from random import randint


mystery_number = randint(1,100)
input_user = None
coups = 0
victory = False

while not victory:
    input_user = int(input("Devinez le nombre mystère : "))
    coups += 1
    if input_user < mystery_number:
        print('Le nombre mystère est plus grand')
    elif input_user > mystery_number:
        print('Le nombre mystère est plus petit')
    else:
        victory = True
        print(f'Bravo le nombre mystère était : {mystery_number}')
        print(f"Vous avez trouvez en {coups} coups")
        
# ====================================================

from random import randint

again = True

while again:
    mystery_number = randint(1,100)
    input_user = None
    coups = 0
    victory = False

    while not victory:
        input_user = int(input("Devinez le nombre mystère : "))
        coups += 1
        if input_user < mystery_number:
            print('Le nombre mystère est plus grand')
        elif input_user > mystery_number:
            print('Le nombre mystère est plus petit')
        else:
            victory = True
            print(f'Bravo le nombre mystère était : {mystery_number}')
            print(f"Vous avez trouvez en {coups} coups")
            
    input_user = input("Voulez-vous rejouer ? y - n : ")
    if input_user == "n":
        again = False

"""
exo17-À l’aide d’une boucle TantQue … Faire, améliorez l’algorithme du distributeur
de boissons pour qu’il demande au client s’il désire une autre boisson (Tant qu’il en a
envie).
"""
stock_coca = 5
stock_fanta = 5
stock_eau = 5
stock_cafe = 5

choice = None

continue_loop = True

menu = """
coca  : 1
fanta : 2
eau   : 3
café  : 4
stop  : 5
"""


while continue_loop:
    print(menu)
    choice = input("Faites votre selection : ")
    
    match choice:
        case "1":
            if stock_coca > 0:
                print("Voici votre coca ")
                stock_coca -= 1
            else:
                print("Cette boisson n'est plus disponible")
        case "2":
            if stock_fanta > 0:
                print("Voici votre fanta ")
                stock_fanta -= 1
            else:
                print("Cette boisson n'est plus disponible")
        case "3":
            if stock_eau > 0:
                print("Voici votre eau ")
                stock_eau -= 1
            else:
                print("Cette boisson n'est plus disponible")
        case "4":
            if stock_cafe > 0:
                print("Voici votre café ")
                stock_cafe -= 1
            else:
                print("Cette boisson n'est plus disponible")
        case "5":
            continue_loop = False
            print("Merci au revoir")
            
"""
• exo18-À l’aide d’une boucle TantQue … Faire, améliorez l’algorithme de la
calculatrice afin qu’elle demande à l’utilisateur s’il veut faire un autre calcul (tant
qu’il le désire).
"""
nb_1 = None
operator = None
nb_2 = None

continue_loop = True

input_user = None


while continue_loop:
    nb_1 = int(input("Entrez le premier nombre : "))
    operator = input("Entrez l'opérateur : (+ - * / ) : ")
    nb_2 = int(input("Entrez le deuxième nombre : "))
    
    match operator:
        case "+":
            print(f"{nb_1} {operator} {nb_2} = {nb_1 + nb_2}")
        case "-":
            print(f"{nb_1} {operator} {nb_2} = {nb_1 - nb_2}")
        case "*":
            print(f"{nb_1} {operator} {nb_2} = {nb_1 * nb_2}")
        case "/":
            if nb_2 == 0:
                print("La division par zéro n'est pas possible")
            else:
                print(f"{nb_1} {operator} {nb_2} = {nb_1 / nb_2}")
                
    input_user = input("Voulez-vous faire un autre calcul ? y - n :")
    if input_user == "n":
        continue_loop = False
        print("Merci au revoir")
"""
• exo19-À l’aide de la boucle TantQue … Faire, réalisez un algorithme calculant le
résultat de N10. N étant un nombre saisi par l’utilisateur.
"""
n = None
compteur = 0
resultat = 1

n = int(input("Entrez la valeur : "))

while compteur < 10:
    resultat = resultat * n
    compteur += 1
    
print(f"{n}^10 = {resultat}")


"""
• exo20-Reprenez l’exercice précédent et modifiez-le pour que l’utilisateur entre
également l’exposant qu’il désire calculer.
"""
n = None
compteur = 0
resultat = 1
exposant = 10

n = int(input("Entrez la valeur : "))
exposant = int(input("Entrez l'exposant : "))

while compteur < exposant:
    resultat = resultat * n
    compteur += 1
    
print(f"{n}^{exposant} = {resultat}")
"""
• exo21-Améliorez le "C'est plus, c'est moins, c'est gagné" 
pour qu'il tourne en boucle tant que le juste_prix n'a pas été trouvé.
L'ordinateur choisit un nombre aléatoirement entre 1 et 100. 
L'utilisateur est invité à entrer un nombre et 
l'algorithme nous répond "C'est plus" ou "C'est moins". 
Lorsqu'on a trouvé le bon nombre, l'algorithme affiche le nombre de tentatives effectuées pour trouver le résultat
"""
from random import randint

again = True

while again:
    mystery_number = randint(1,100)
    input_user = None
    coups = 0
    victory = False

    while not victory:
        input_user = int(input("Devinez le nombre mystère : "))
        coups += 1
        if input_user < mystery_number:
            print('Le nombre mystère est plus grand')
        elif input_user > mystery_number:
            print('Le nombre mystère est plus petit')
        else:
            victory = True
            print(f'Bravo le nombre mystère était : {mystery_number}')
            print(f"Vous avez trouvez en {coups} coups")
            
    input_user = input("Voulez-vous rejouer ? y - n : ")
    if input_user == "n":
        again = False
"""
Exercices supplémentaires:
• 1) Réalisez un système de connexion à l'aide d'un mot de passe. 
L'algorithme demande à l'utilisateur de saisir son mot de passe. 
Si ce dernier valide de bon mot de passe, on le salue. 
Par contre, si il fait une erreur trois fois de suite, 
un message lui signalera que son compte est bloqué et il ne pourra pas réessayer une quatrième fois
"""
correct_email = "mail@mail.com"
correct_password = "test1234"

tentatives = 0

input_email = None
input_password = None

is_logged = False

while not is_logged and tentatives < 4:
    input_email = input("Entrez votre email : ")
    input_password = input("Entrez votre password : ")
    
    tentatives += 1
    
    if input_email == correct_email and input_password == correct_password:
        is_logged = True
    else:
        print("Les informations sont incorrectes")
        print(f"Il vous reste {4 - tentatives} essais")
        

if is_logged:
    print(f"Bienvenue {input_email}")
else:
    print("Votre compte est bloqué")

"""
• 2) Réalisez un algorithme qui demande un nombre à l'utilisateur et affiche autant de ligne que le nombre spécifié par
l'utilisateur.Exemple : l'utilisateur a rentré le nombre 5 et l'algorithme affiche :
*
**
***
****
*****
"""
nombre = int(input("Entrez le nombre de lignes à afficher : "))


for i in range(1,nombre + 1):
    print("*" * i)

"""
• 3) Ecrire un algorithme qui demande à l’utilisateur de taper 10 entiers et qui affiche le plus petit de ces entiers.

"""
nb = int(input("Entrez un nombre : "))

min = nb

for i in range(2,10 + 1):
    nb = int(input("Entrez un nombre : "))
    
    if nb < min :
        min = nb
        
print(f"Le plus petit nombre est : {min}")

# =====================================================

list_value = []

min = 99999
max = 0

for i in range(1,11):
    value = int(input(f"Entrez un nombre pour la position {i}"))
    list_value.append(value)
    
for v in list_value:
    if v > max:
        max = v
        
    if v < min:
        min = v
        
print(f"La valeur minimum est : {min}")
print(f"La valeur maximum est : {max}")


"""
• 4) Algorithme demandant 3 nombres : nbRep, nbTiret, nbEspace. 
Ce dernier affiche à l'écran autant de tiret que la valeur de nbTiret, 
suivi d'autant d'espace que la valeur de nbEspace. 
Le tout autant de fois que la valeur de nbRep.
Exemple : si nbRep = 2, nbTiret = 1 et nbEspace = 3 le résultat est le suivant :
|- - |
"""

nb_rep = None
nb_tiret = None
nb_espace = None

ligne = ""

nb_rep = int(input("Entrez le nombre de répétition"))
nb_tiret = int(input("Entrez le nombre de tiret"))
nb_espace = int(input("Entrez le nombre d'espace"))

for i in range(1 , nb_rep + 1):
    for t in range(1 , nb_tiret + 1):
        ligne += "-"
        
    for e in range(1 , nb_espace + 1):
        ligne += " "
        
print(ligne)


# ========================================================

ligne_2 = ""

for j in range(nb_rep):
    ligne_2 += "-" * nb_tiret + " " * nb_espace
    
print(ligne_2)



"""
Projet : juste_prix
• Améliorez encore le juste_prix : l'utilisateur a droit à 10 essais après ces 10
essais, il a perdu.
• L'ordinateur affiche le juste_prix
• Ajouter un niveau :
– facile : entre 1 et 10
– moyen : entre 1 et 100
– difficile : entre 1 et 1000
• Tant que la personne veut rejouer, redemandez le niveau et générez un
nombre.
• Vérifiez que tout caractère entré est correct, c'est-à-dire pour que le
programme ne plante jamais.

Indices
• Pour générer un nombre entre 0 et 10, il faut 2
choses :
– import random
– juste_prix = random.randrange(0, 11, 1)
• Pour effacer l'écran, il faut 2 choses :
– import os
– os.system('cls')

Indices
• Pour vérifier qu'une chaine de caractères est
un nombre :
– chaine = "4"
– if chaine.isdigit() :
print("C'est un nombre")
else :
print("Ce n'est pas un nombre")
"""

from random import randint

def get_number(message,min , max):
    value_int = None
    while True:
        value = input(f"Entrez une valeur pour {message}")
        
        try:
            value_int = int(value)
        except:
            print("La valeur doit être un nombre")
            
        if value_int is not None and min < value_int < max:
            return value_int


input_user = None
input_user_price = None
life = 10

continue_game = True
is_correct = False

max_value = 10

menu_level = """
niveau 1 :entre  1 et 10
niveau 2 :entre  1 et 100
niveau 3 :entre  1 et 1000
"""

while continue_game:
    print(menu_level)
    
    input_user = get_number("le niveau de difficulté : ",0,4)
    
    match input_user : 
        case 1 :
            max_value = 10
        case 2 :
            max_value = 100
        case 3 :
            max_value = 1000
    
    
    mystery_price = randint(1,max_value)
    life = 10
    while life > 0:
        input_user_price = get_number(f"votre tentative , essai restant {life}",1,max_value)
        life -= 1
        
        match input_user_price:
            case _ if input_user_price < mystery_price:
                print("Le prix mystère est plus grand")
            case _ if input_user_price > mystery_price:
                print("Le prix mystère est plus petit")
            case _ if input_user_price == mystery_price:
                print("Bravo vous avez trouvé le prix mystère")
                print(f"Vous avez trouvez le prix en {10 - life}coups")
                life = 0

    input_user = input("Voulez-vous recommencer ? y - n")
    if input_user == "n":
        continue_game = False