
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