# Exercice : Résolution de sudoku

## Le jeu

Le sudoku est une grille de **9 lignes sur 9 colonnes**, soit 81 cases.
La grille est aussi découpée en **9 blocs** (ou régions) de 3 cases sur 3.

Chaque case contient un chiffre de 1 à 9. Une grille est **valide** si :

- chaque **ligne** contient les chiffres de 1 à 9, une seule fois chacun ;
- chaque **colonne** contient les chiffres de 1 à 9, une seule fois chacun ;
- chaque **bloc 3×3** contient les chiffres de 1 à 9, une seule fois chacun.

Au départ, une partie de la grille est déjà remplie. Le but est de compléter
les cases vides en respectant les trois règles ci-dessus. Une grille d'énoncé
correcte n'admet qu'**une seule** solution possible.

## Représentation en Python

Une grille est une **liste de 9 listes de 9 entiers**.
Une case vide est notée `0`.

```python
grille[ligne][colonne]      # la case (ligne, colonne), indices de 0 à 8
```

---

## Exercice 1 — Valider une grille complète

Écrire une fonction qui vérifie si une grille **complète** est valide :

```python
def est_valide(grille):     # → True ou False
```

### Grille valide (pour vos tests)

```python
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
```

### Grille invalide (pour vos tests)

Le `3` apparaît deux fois sur la première ligne, deux fois dans le premier
bloc et deux fois dans la première colonne :

```python
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
```

---

## Exercice 2 — Compléter une grille

Écrire une fonction qui **complète** une grille incomplète :

```python
def resoudre(grille):
```

<details>
<summary>Indice (à ne lire que si vous bloquez)</summary>

La stratégie classique est l'**essai-erreur récursif** (*backtracking*) :

1. chercher une case vide — s'il n'y en a plus, la grille est résolue ;
2. pour chaque chiffre de 1 à 9 **compatible** avec la ligne, la colonne et
   le bloc de cette case : le poser, puis tenter de résoudre le reste
   (appel récursif) ;
3. si aucun chiffre ne mène à une solution, remettre la case à `0` et
   **revenir en arrière** — l'erreur est plus haut.

Un morceau de l'exercice 1 resservira : « ce chiffre est-il permis à cette
position ? »
</details>

### Grille 1 (facile)

```python
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
```

### Grille 2 (moyenne)

```python
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
```

### Grille 3 (difficile)

```python
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
```

### Les solutions attendues

La solution de la **grille 1** est la `grille_valide` donnée plus haut.

Les **grilles 2 et 3** ont la même solution :

```python
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
```
