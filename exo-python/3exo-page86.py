"""
exo07-Année bissextile (Pseudo-Code + Python)
Réaliser un petit algorithme qui sur base d’une année donnée va déterminer s’il s’agit d’une année
bissextile. 
Une année est bissextile si elle est divisible par 4, mais non divisible par 100. 
Ou si elle est divisible par 400. 
(ex: 2020, 1600 bissextiles. 1900 pas bissextile)
"""
year = int(input("Entrez une année : "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('Bissextile')
else:
    print("non Bissextile")
    



"""
exo8-Lanceur de balles de tennis (Pseudo-Code + Python)
(Indice : booleen = bool(int(input("Veuillez insérer : 1 = oui / 0 = non"))
Réaliser l’algorithme d’un lanceur de balles de tennis. Ce lanceur possède deux états :
– prêt : permet de savoir si le tennisman est prêt. Il ne faut pas lancer de balles dans le cas contraire
– panier_vide : permet de savoir s’il y a encore des balles disponibles
Le lanceur de balle possède l’opération « lancerBalle » qui, vous l’aurez compris, permet de lancer
une balle.
"""
ready = False
panier_vide = True
    

stock_balls = int(input("Combien de balles avez vous mis : "))

if stock_balls > 0:
    panier_vide = False
    
    response = input("Etes-vous prêt? y-n :")
    if response == 'y':
        ready = True
        
if ready and not panier_vide:
    print('La partie commence !')
    print("Balle lancé")
    stock_balls -= 1
    print(f"il reste {stock_balls}balles")



"""
exo09-Distributeur de boissons (Pseudo-Code + Python)
Réaliser l’algorithme d’un distributeur de boissons. 
Ce dernier propose plusieurs boissons et l’utilisateur choisit celle qu’il désire 
en entrant le numéro correspondant. 
Ne pas oublier de vérifier s’il y a encore des boissons en stock.
86
"""
coca = 5
fanta = 5
eau = 5
cafe = 5

user_choice = None

menu = """
coca    : 1
fanta   : 2
eau     : 3
café    : 4
arret   : 0
"""

print(menu)
user_choice = input("Faites votre choix : ")

match user_choice:
    case "1":
        if coca > 0:
            print("Voici votre coca")
            coca -= 1
        else:
            print("Cette boisson n'est plus disponible!")
    case "2":
        if fanta > 0:
            print("Voici votre fanta")
            fanta -= 1
        else:
            print("Cette boisson n'est plus disponible!")
    case "3":
        if eau > 0:
            print("Voici votre eau")
            eau -= 1
        else:
            print("Cette boisson n'est plus disponible!")
    case "4":
        if cafe > 0:
            print("Voici votre café")
            cafe -= 1
        else:
            print("Cette boisson n'est plus disponible!")
    case "0":
        pass


"""
exo10-Calculatrice (Pseudo-Code + Python)
Réaliser l’algorithme d’une calculatrice basique. 
L’utilisateur est invité à saisir un nombre, un opérateur, et un deuxième nombre. 
La calculatrice affiche ensuite le résultat. (Gérer la division par 0)
"""
nb_1 = None
operator = None
nb_2 = None

nb_1 = int(input("Entrez le premier nombre : "))
operator = input("Entrez un opérateur | + - * / % ")
nb_2 = int(input("Entrez le deuxième nombre : "))

match operator:
    case "+":
        print(f"{nb_1} {operator} {nb_2} = {str(nb_1 + nb_2)}")
    case "-":
        print(f"{nb_1} {operator} {nb_2} = {str(nb_1 - nb_2)}")
    case "*":
        print(f"{nb_1} {operator} {nb_2} = {str(nb_1 * nb_2)}")
    case "/":
        if nb_2 == 0:
            print("La division par zéro n'est pas possible")
        else:
            print(f"{nb_1} {operator} {nb_2} = {str(nb_1 / nb_2)}")
    case "%":
        print(f"{nb_1} {operator} {nb_2} = {str(nb_1 % nb_2)}")


"""
exo11-Note (Pseudo-Code + Python)
Ecrire un algorithme qui met l'appréciation par rapport à des
notes. Ces notes sont comprises entre 0 et 20.
! Gérer les erreurs : ex : -2; 25
87
"""

note = int(input("Entrez votre note : "))

if 0 <= note <= 20:
    match note:
        case _ if note >= 18:
            print("TB")
        case _ if 15 < note < 18:
            print("B")
        case _ if 10 < note <= 15:
            print("S")
        case _ if note <= 10:
            print("I")
        



"""
exo12-Réalisez un algorithme utilisant le convertisseur de
secondes, il reçoit deux durées (jours, heures, minutes et
secondes) et calcule la différence entre ces dernières.

"""
result_diff_secondes = None

secondes_1 = int(input("Entrez les secondes pour la première valeur"))
minutes_1 = int(input("Entrez les minutes pour la première valeur"))
heures_1 = int(input("Entrez les heures pour la première valeur"))
jours_1 = int(input("Entrez les jours pour la première valeur"))

secondes_2 = int(input("Entrez les secondes pour la deuxième valeur"))
minutes_2 = int(input("Entrez les minutes pour la deuxième valeur"))
heures_2 = int(input("Entrez les heures pour la deuxième valeur"))
jours_2 = int(input("Entrez les jours pour la deuxième valeur"))
        
        
sec_1 = secondes_1 + minutes_1 * 60 + heures_1 * 3600 + jours_1 * 86400
sec_2 = secondes_2 + minutes_2 * 60 + heures_2 * 3600 + jours_2 * 86400

if sec_1 > sec_2:
    result_diff_secondes = sec_1 - sec_2
else:
    result_diff_secondes = sec_2 - sec_1
    
jours_diff = result_diff_secondes // 86400
reste = result_diff_secondes % 86400

heures_diff = reste // 3600
reste = reste % 3600

minutes_diff = reste // 60
secondes_diff = reste % 60 

print(f"la différence est de {jours_diff}j {heures_diff}h {minutes_diff}m {secondes_diff}s")


"""
Memory Game
"""

ma_list = list()
points = 0
end_game = False

while not end_game:
    mot = input("Entrez un nouveau mot")
    ma_list.append(mot)
    
    
    print("Entrez les mots un par un dans l'ordre :")
    for i in range(0,len(ma_list),1):
        input_user = input(f"Mot n° {i + 1}")
        if ma_list[i] != input_user:
            end_game = True
            break
        points += 1
        
        
print(f"Vous avez memoriser {points} mots")