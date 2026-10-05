a = 5
b = 8

# 1
temp = a
a = b
b = temp

# 2
a = a + b # 13
b = a - b # 5
a = a - b # 8


# 3 astuce python
c = 8
d = 12

x,y,z = 10,12,15

c,d = d,c


# afficher une information
print("Entrez vos informations")

nom = input('Entrez votre nom : ')
prenom = input('Entrez votre prénom : ')
age = input('Entrez votre age : ')

print(f"Bonjour vous êtes {nom} - {prenom} vous avez {age }ans")
print(type(age))

# Conversion de valeurs

age_int = int(age)
print(type(age_int))
print(age_int + 1)