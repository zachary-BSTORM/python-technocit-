# # Exercice : Implémentation d’un démineur en Python

# ## Objectif

# Réaliser une version simplifiée du jeu du démineur en Python (mode console), sans programmation orientée objet.

# Le joueur doit révéler toutes les cases sans tomber sur une mine.

# ---

# ## Règles du jeu

# - La grille est de taille `rows x cols`
# - Certaines cases contiennent des mines (`*`)
# - Les autres cases contiennent un nombre indiquant le nombre de mines adjacentes
# - Le joueur peut :
#   - ouvrir une case
#   - poser ou retirer un drapeau
# - Si une mine est ouverte → défaite
# - Si toutes les cases non minées sont révélées → victoire

# ---

# ## Règle spécifique

# Les mines ne sont pas placées au début.

# - Elles sont générées lors du premier clic
# - La première case ouverte ne peut pas contenir de mine

# ---

# ## Fonctions à implémenter

# ### create_grid

# def create_grid(rows, cols, value):

# Créer une grille (liste de listes) remplie avec la valeur donnée.

# ###  get_neighbors
# def get_neighbors(rows, cols, r, c):

# Retourner la liste des coordonnées des cases voisines (8 directions) en respectant les limites de la grille.

# ###  generate_mines
# def generate_mines(rows, cols, nb_mines, forbidden_cell):

# Générer un ensemble de positions de mines.

# ## Contraintes

# - ne pas placer deux mines au même endroit
# - ne pas placer de mine sur `forbidden_cell`

# ---

# ### create_hidden_grid
# def create_hidden_grid(rows, cols, mines):

# Créer la grille interne du jeu :

# - "*" pour les mines  
# - un entier pour le nombre de mines adjacentes sinon  

# ---

# ### reveal
# def reveal(hidden, visible, r, c):

# Révéler une case :

# - si la case contient un nombre différent de 0 → révéler uniquement cette case  
# - si la case contient 0 → révéler récursivement les cases voisines  

# ---

# ### print_grid
# def print_grid(grid):

# Afficher la grille dans la console.

# ---

# ### has_won
# def has_won(hidden, visible):

# Retourner True si toutes les cases non minées ont été révélées, sinon False.

# ---

# ### minesweeper
# def minesweeper(rows, cols, nb_mines):

# Fonction principale :

# - gère les entrées utilisateur  
# - gère la logique du jeu  
# - appelle les autres fonctions  

# ---

# ### Commandes utilisateur

# - o ligne colonne → ouvrir une case  
# - f ligne colonne → poser ou retirer un drapeau  

# ---

# ### Contraintes

# - utiliser uniquement la bibliothèque standard (random autorisé)  
# - gérer les entrées invalides :
#   - coordonnées hors de la grille  
#   - commandes incorrectes  
# - structurer le code en fonctions (éviter une seule fonction monolithique)  

# ---

# ### Bonus

# - empêcher de poser un drapeau sur une case déjà révélée  
# - améliorer l’affichage de la grille  
# - ajouter un compteur de coups  
# - ajouter un temps de jeu  

# ---

# ### Bonus avancé

# - empêcher la génération de mines autour de la première case  
# - proposer plusieurs niveaux de difficulté  
# - implémenter une interface graphique (optionnel)