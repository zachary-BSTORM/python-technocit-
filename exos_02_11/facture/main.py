# main.py — Exercice 3 : Méthodes statiques au service d'une instance, facture
from models import Facture


# ---------------------------------------------------------------
# 1. Méthodes statiques appelées seules, sans créer de facture
# ---------------------------------------------------------------
print(f"round(2.675, 2)  = {round(2.675, 2)}")
print(f"arrondir_centimes = {Facture.arrondir_centimes(2.675)}")
print(f"formater_montant  = {Facture.formater_montant(1234567.891)}")


# ---------------------------------------------------------------
# 2. Facture F-001
# ---------------------------------------------------------------
facture = Facture("F-001", "Client A")
facture.ajouter_ligne("Écran", 2, 249.90)            # TVA 20 % par défaut
facture.ajouter_ligne("Livre", 3, 32.50, 0.055)
facture.ajouter_ligne("Câble", 5, 8.99, 0.20)


# ---------------------------------------------------------------
# 3. Ligne invalide
# ---------------------------------------------------------------
try:
    facture.ajouter_ligne("Clé USB", 0, 12.00)
except ValueError as e:
    print(f"Ligne refusée : {e}")


# ---------------------------------------------------------------
# 4. Lignes puis totaux
# ---------------------------------------------------------------
fmt = Facture.formater_montant

for designation, quantite, prix_unitaire, taux_tva in facture.lignes:
    montant = facture.montant_ligne(quantite, prix_unitaire)
    print(
        f"  {designation:<9}{quantite} × {fmt(prix_unitaire):>9} "
        f"= {fmt(montant):>9}  (TVA {taux_tva * 100:g} %)"
    )

print(f"  {'Total HT':<13}{fmt(facture.total_ht())}")
print(f"  {'TVA':<13}{fmt(facture.total_tva())}")
print(f"  {'Total TTC':<13}{fmt(facture.total_ttc())}")