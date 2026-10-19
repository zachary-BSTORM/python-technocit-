
    


# if __name__ == "__main__":
#     main()
    


# Exemple Class 
class Produit:
    def __init__(self, nom, prix_unitaire, quantite):
        self.nom = nom
        self._prix_unitaire = prix_unitaire
        self.quantite = quantite
        
        
    @property
    def quantite(self):
        return self.__quantite
    
    @quantite.setter
    def quantite(self, value):
        if value > 0:
            self.__quantite = value
        else:
            raise ValueError("La quantité doit être supérieure à 0")
        
new_product = Produit("test", 10, 5)

print("----------------")
print(new_product.nom)
new_product.nom = "test2"
print(new_product.nom)

print("----------------")
print(new_product._prix_unitaire)
new_product._prix_unitaire = 20
print(new_product._prix_unitaire)

print("----------------")

print(new_product.quantite)
new_product.quantite = 50
print(new_product.quantite)

