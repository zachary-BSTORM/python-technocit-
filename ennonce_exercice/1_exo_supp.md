# Gestionnaire de bibliothèque


## Vous aller implémenter une application pour gérer une bibliothèque

- Entitées : 
    - livres : id(int) - title(str) - author(list[str]) - year(int)- available(bool)
    - user : id(int) - username(str) - email(str)  - booksIds (list[int])


- Gestion des livres : 
    - afficher les livres
    - ajout d'un livre
    - modifier un livre
    - supprimer un livre

- Gestion des utilisateurs :
    - ajout d'un utilisateurs
    - afficher les livres loué par un utilisateurs
    - louer un livre
    - rentrer un livre

- Le tout sera gérer dans un programme qui propose ces différentes actions

## Contraintes

- la bibliothèque gère les livres et les utilisateurs dans des dictionnaires
- lorsque l'application se lance on boucle jusqu'à ce que l'utilisateur stoppe le programme 