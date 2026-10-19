Résolution de sudoku :

Le sudoku est une grille de 9 lignes sur 9 colonnes, soit 81 cases.
La grille est aussi découpée en 9 blocs (ou régions) de 3 cases sur 3.

Chaque case contient un chiffre de 1 à 9.
Une grille est valide si :
 - chaque ligne contient les chiffres de 1 à 9, une seule fois chacun
 - chaque colonne contient les chiffres de 1 à 9, une seule fois chacun
 - chaque bloc de 3x3 contient les chiffres de 1 à 9, une seule fois chacun

Au départ, une partie de la grille est déjà remplie. Le but est de compléter
les cases vides en respectant les trois règles ci-dessus. Une grille d'énoncé
correcte n'admet qu'une seule solution possible.

En Python, une grille est représentée par une liste de 9 listes de 9 entiers.
Une case vide est notée 0.


Exercice 1 : écrire une fonction qui vérifie si une grille complète est valide.

Grille valide :

grille_valide = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
]

Grille invalide (le 3 apparaît deux fois sur la première ligne, deux fois
dans le premier bloc et deux fois dans la première colonne) :

grille_invalide = [
    [3, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
]


Exercice 2 : écrire une fonction qui complète une grille incomplète.

Grille 1 (facile) :

grille_1 = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

Grille 2 (moyenne) :

grille_2 = [
    [0, 0, 4, 5, 3, 0, 2, 7, 1],
    [2, 0, 1, 8, 0, 4, 0, 0, 0],
    [0, 3, 0, 0, 0, 0, 0, 6, 0],
    [3, 0, 0, 7, 0, 0, 0, 0, 5],
    [6, 4, 0, 0, 9, 2, 0, 0, 0],
    [0, 1, 0, 0, 0, 5, 0, 9, 2],
    [0, 8, 6, 0, 5, 3, 9, 0, 7],
    [0, 2, 0, 1, 8, 6, 0, 5, 0],
    [4, 0, 0, 9, 0, 0, 0, 0, 0],
]

Grille 3 (difficile) :

grille_3 = [
    [0, 6, 0, 5, 0, 9, 0, 0, 1],
    [2, 0, 0, 0, 0, 0, 0, 3, 0],
    [5, 0, 0, 0, 0, 1, 0, 0, 0],
    [3, 9, 2, 0, 0, 0, 6, 0, 5],
    [0, 4, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 8, 0, 0, 5, 3, 9, 0],
    [0, 8, 6, 0, 0, 3, 0, 0, 0],
    [0, 0, 0, 1, 8, 6, 0, 5, 0],
    [0, 5, 0, 9, 2, 0, 1, 8, 0],
]

Les grilles 2 et 3 ont la même solution :

solution_2_3 = [
    [8, 6, 4, 5, 3, 9, 2, 7, 1],
    [2, 7, 1, 8, 6, 4, 5, 3, 9],
    [5, 3, 9, 2, 7, 1, 8, 6, 4],
    [3, 9, 2, 7, 1, 8, 6, 4, 5],
    [6, 4, 5, 3, 9, 2, 7, 1, 8],
    [7, 1, 8, 6, 4, 5, 3, 9, 2],
    [1, 8, 6, 4, 5, 3, 9, 2, 7],
    [9, 2, 7, 1, 8, 6, 4, 5, 3],
    [4, 5, 3, 9, 2, 7, 1, 8, 6],
]

La solution de la grille 1 est la grille valide donnée plus haut.
