# Exercice : Implémentation d'un démineur en Python

## Objectif

Réaliser une version simplifiée du jeu du démineur en Python (mode console),
**sans programmation orientée objet** : le code est structuré en fonctions.

Le joueur doit révéler toutes les cases sans tomber sur une mine.

---

## Règles du jeu

- La grille est de taille `rows x cols`.
- Certaines cases contiennent des mines (`"*"`).
- Les autres cases contiennent un nombre : le nombre de mines **adjacentes**.
- À chaque tour, le joueur peut :
  - **ouvrir** une case ;
  - **poser ou retirer un drapeau** sur une case.
- Ouvrir une mine → **défaite**.
- Toutes les cases non minées révélées → **victoire**.

## Règle spécifique — la génération au premier coup

Les mines ne sont **pas** placées au lancement du jeu :

- elles sont générées au moment du **premier coup** du joueur ;
- la première case ouverte ne peut donc **jamais** contenir de mine.

---

## Les commandes du joueur

```
o ligne colonne     → ouvrir la case (ligne, colonne)
f ligne colonne     → poser ou retirer un drapeau sur la case
```

---

## Fonctions à implémenter

| Fonction | Rôle |
|---|---|
| `create_grid` | fabriquer une grille vierge |
| `get_neighbors` | lister les voisins d'une case |
| `generate_mines` | tirer les positions des mines |
| `create_hidden_grid` | construire la grille interne (mines + compteurs) |
| `reveal` | révéler une case (et ses voisines si 0) |
| `print_grid` | afficher une grille |
| `has_won` | détecter la victoire |
| `minesweeper` | la boucle de jeu principale |

### `create_grid`

```python
def create_grid(rows, cols, value):
```

Créer une grille — une **liste de listes** — remplie avec la valeur donnée.

### `get_neighbors`

```python
def get_neighbors(rows, cols, r, c):
```

Retourner la liste des coordonnées des cases voisines de `(r, c)`
(**8 directions**), en respectant les limites de la grille.

### `generate_mines`

```python
def generate_mines(rows, cols, nb_mines, forbidden_cell):
```

Générer un **ensemble** de positions de mines. Contraintes :

- ne pas placer deux mines au même endroit ;
- ne pas placer de mine sur `forbidden_cell` (la première case ouverte).

### `create_hidden_grid`

```python
def create_hidden_grid(rows, cols, mines):
```

Créer la grille interne du jeu :

- `"*"` pour les mines ;
- sinon, un entier : le nombre de mines adjacentes à la case.

### `reveal`

```python
def reveal(hidden, visible, r, c):
```

Révéler une case :

- si la case contient un nombre **différent de 0** → révéler uniquement cette case ;
- si la case contient **0** → révéler **récursivement** les cases voisines.

### `print_grid`

```python
def print_grid(grid):
```

Afficher la grille dans la console.

### `has_won`

```python
def has_won(hidden, visible):
```

Retourner `True` si toutes les cases **non minées** ont été révélées,
`False` sinon.

### `minesweeper`

```python
def minesweeper(rows, cols, nb_mines):
```

La fonction principale :

- gère les entrées de l'utilisateur ;
- gère la logique du jeu (premier coup, défaite, victoire) ;
- appelle les autres fonctions.

---

## Contraintes

- Utiliser uniquement la **bibliothèque standard** (`random` autorisé).
- Gérer les entrées invalides :
  - coordonnées hors de la grille ;
  - commandes incorrectes.
- Structurer le code en fonctions — pas de fonction monolithique.

---

## Bonus

- Empêcher de poser un drapeau sur une case déjà révélée.
- Améliorer l'affichage de la grille.
- Ajouter un compteur de coups.
- Ajouter un temps de jeu.

## Bonus avancé

- Empêcher la génération de mines **autour** de la première case (pas
  seulement dessus).
- Proposer plusieurs niveaux de difficulté.
- Implémenter une interface graphique (optionnel).
