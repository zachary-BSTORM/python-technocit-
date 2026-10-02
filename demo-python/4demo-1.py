age = int(input("Entrez votre age: "))
poste = input("Entrez votre nom: ")
access = False

if age > 18:
    print("Vous avez accès")
    access = True
else:
    print("Accès refusé")
    
    
if access and poste == "patron":
    print('Vous pouvez rentrez')
elif access and poste == "employé":
    print('Ou est votre badge')
else:
    print("L'accueil est de ce coté")