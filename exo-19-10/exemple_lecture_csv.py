"""Exemple minimal : lire un fichier CSV avec la bibliothèque standard."""

import csv


# Ouvre un fichier CSV et renvoie une liste de dictionnaires.
# Chaque dictionnaire représente une ligne, ses clés sont les noms des colonnes.
def lire_csv(chemin):
    # newline="" est recommandé par la doc du module csv,
    # encoding="utf-8" permet de lire correctement les accents (Liège, Éclairage...).
    with open(chemin, newline="", encoding="utf-8") as fichier:
        lecteur = csv.DictReader(fichier)
        return list(lecteur)


# Convertit un texte en nombre décimal.
# Renvoie None au lieu de planter si la valeur est vide ou invalide.
def vers_float(texte):
    try:
        return float(texte)
    except (ValueError, TypeError):
        return None


def main():
    produits = lire_csv("produits.csv")

    print(f"{len(produits)} produits lus")
    print("Première ligne :", produits[0])
    print()

    # Tout ce qui sort d'un CSV est du texte : il faut convertir avant de calculer.
    for produit in produits:
        prix = vers_float(produit["prix_unitaire"])
        if prix is None:
            print(f"- {produit['nom']:<22} prix invalide : {produit['prix_unitaire']!r}")
        else:
            print(f"- {produit['nom']:<22} {prix:>8.2f} €")


if __name__ == "__main__":
    main()
