import csv

def get_products():
    pass

def read_file():
    # with : permet une gestion automatique du fichier (ouverture et fermeture)
    with open("produits.csv",newline="",encoding="utf-8") as fichier:
        result = csv.DictReader(fichier) # dictReader : permet de lire le fichier CSV et de le transformer en dictionnaire
        return list(result)
    
def main():
    result = read_file()
    
    for p in result:
        print(p)
        p["prix_unitaire"] = float(p.get("prix_unitaire"))
        print(f" {p.get("prix_unitaire")} type : {type(p.get("prix_unitaire"))}")