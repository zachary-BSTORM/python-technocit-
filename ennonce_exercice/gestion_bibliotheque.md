# Exercice : Gestionnaire de bibliothèque

## Objectif

Implémenter une application console pour gérer une bibliothèque : son
catalogue de livres, ses utilisateurs, et la location des livres.

Au lancement, l'application affiche un menu et **boucle** jusqu'à ce que
l'utilisateur choisisse de quitter le programme.

---

## Les entités

### Un livre

| Champ | Type | Rôle |
|---|---|---|
| `id` | `int` | identifiant unique du livre |
| `title` | `str` | le titre |
| `author` | `list[str]` | le ou les auteurs |
| `year` | `int` | l'année de publication |
| `available` | `bool` | `True` si le livre est disponible à la location |

### Un utilisateur

| Champ | Type | Rôle |
|---|---|---|
| `id` | `int` | identifiant unique de l'utilisateur |
| `username` | `str` | son nom d'utilisateur |
| `email` | `str` | son adresse e-mail |
| `booksIds` | `list[int]` | les `id` des livres qu'il loue actuellement |

---

## Les fonctionnalités

### Gestion des livres

- afficher les livres (avec leur disponibilité) ;
- ajouter un livre ;
- modifier un livre ;
- supprimer un livre.

### Gestion des utilisateurs

- ajouter un utilisateur ;
- afficher les livres loués par un utilisateur ;
- louer un livre ;
- rendre un livre.

Le tout est piloté par un programme qui propose ces différentes actions dans
un menu.

---

## La mécanique de location

- **Louer** : le livre doit exister **et** être disponible. Son `id` est
  ajouté à la liste `booksIds` de l'utilisateur, et son champ `available`
  passe à `False`.
- **Rendre** : le livre doit figurer dans la liste `booksIds` de
  l'utilisateur. Son `id` en est retiré, et `available` repasse à `True`.

---

## Contraintes

- La bibliothèque gère les livres et les utilisateurs dans des
  **dictionnaires** dont la clé est l'`id` de l'entité
  (`livres[3]` → la fiche du livre n°3).
- Au lancement, l'application **boucle** sur le menu jusqu'à ce que
  l'utilisateur stoppe le programme.
- Le programme ne plante jamais : un `id` inconnu, un livre déjà loué, une
  saisie invalide → un message, puis retour au menu.

---

## Données de départ proposées

```python
livres = {
    1: {"id": 1, "title": "1984", "author": ["George Orwell"],
        "year": 1949, "available": True},
    2: {"id": 2, "title": "Le Petit Prince", "author": ["Antoine de Saint-Exupéry"],
        "year": 1943, "available": True},
    3: {"id": 3, "title": "Good Omens", "author": ["Terry Pratchett", "Neil Gaiman"],
        "year": 1990, "available": True},
}

users = {
    1: {"id": 1, "username": "alice", "email": "alice@bstorm.be", "booksIds": []},
    2: {"id": 2, "username": "bob", "email": "bob@bstorm.be", "booksIds": []},
}
```

---

## Bonus

- Empêcher la **suppression** d'un livre actuellement loué.
- Générer automatiquement l'`id` d'un nouveau livre ou utilisateur
  (le plus grand `id` existant + 1).
- Rechercher un livre par morceau de titre (insensible à la casse).
