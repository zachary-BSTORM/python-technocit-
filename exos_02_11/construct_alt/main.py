# main.py — Exercice 4 : Méthodes de classe, constructeurs alternatifs
from models import Produit, ProduitSolde


# ---------------------------------------------------------------
# 1. Quatre produits, construits de quatre façons différentes
# ---------------------------------------------------------------
produits = [
    Produit("CLV01", "Clavier", 49.90, 12),
    Produit.depuis_dict(
        {"reference": "ECR02", "nom": "Écran", "prix": "189.00", "stock": "4"}
    ),
    Produit.depuis_chaine("SOU03: Souris sans fil x25 @19.99"),
    Produit.echantillon("Casque"),
]

for produit in produits:
    print(f"  {produit}")


# ---------------------------------------------------------------
# 2. Données invalides
# ---------------------------------------------------------------
essais = [
    # dictionnaire sans prix
    lambda: Produit.depuis_dict({"reference": "LMP05", "nom": "Lampe", "stock": "3"}),
    # chaîne qui ne respecte pas le format "REF: Nom xQTE @PRIX"
    lambda: Produit.depuis_chaine("Lampe 3 pièces 15 euros"),
]

for essai in essais:
    try:
        essai()
    except ValueError as e:
        print(f"  Erreur : {e}")


# ---------------------------------------------------------------
# 3. Sous-classe : les méthodes de classe héritées renvoient cls(...)
# ---------------------------------------------------------------
tapis = ProduitSolde.depuis_chaine("TAP04: Tapis de souris x5 @9.90")
print(f"  {tapis} → {type(tapis).__name__}")

webcam = ProduitSolde.echantillon("Webcam")
print(f"  {type(webcam).__name__}")