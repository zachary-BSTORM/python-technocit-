"""
Réaliser un algorithme convertisseur de seconde. 
Ce dernier reçoit un nombre de secondes et détermine 
le nombre de jours, heures, minutes et secondes auquel elles correspondent.

• Exemple :
4561 secondes correspondent à 0 jour 1 heure 16 minutes et 1 seconde.

• Réfléchissez à la méthode que nous devons utiliser.
• Une fois l’algorithme réalisé, testez-le en Python.

"""
DAY_SECONDES = 86400
HOURS_SECONDES = 3600
jours : int = 0
heures : int = 0
minutes : int = 0
secondes : int = 0
reste : int = 0

input_secondes = int(input('Entrez un nombre de secondes'))

jours = input_secondes // DAY_SECONDES
reste = input_secondes % DAY_SECONDES

heures = reste // HOURS_SECONDES
reste = reste % HOURS_SECONDES

minutes = reste // 60
secondes = reste % 60

print(f" {input_secondes} donne : {jours}jours , {heures}heures , {minutes}minutes , {secondes}secondes")

