# Tout ce qui concerne les produits : lecture de produits.csv, affichage et anomalies.
# Un produit est un dictionnaire :
# {"product_id": "5", "name": "Clavier sans fil", "category": "Informatique", "price": 49.9, "stock": 30}
# price et stock valent None si la valeur du CSV est vide ou invalide.

import csv


def text_to_float(text: str) -> float | None:
    """
    Convertit un texte en nombre décimal ("149.90" -> 149.9). Renvoie None s'il est vide ou invalide.
    """
    try:
        return float(text)
    except ValueError:
        return None


def text_to_int(text: str) -> int | None:
    """
    Convertit un texte en nombre entier ("20" -> 20). Renvoie None s'il est vide ou invalide.
    """
    try:
        return int(text)
    except ValueError:
        return None


def read_products_from_csv() -> list[dict]:
    """
    Lit produits.csv et renvoie la liste des produits (un dictionnaire par produit).
    Le prix et le stock sont convertis en nombres ; une valeur invalide devient None au lieu de planter.
    """
    products = []
    with open("produits.csv", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            product = {
                "product_id": row["id"],
                "name": row["nom"],
                "category": row["categorie"],
                # Tout ce qui sort d'un CSV est du texte : on convertit en nombre
                "price": text_to_float(row["prix_unitaire"]),
                "stock": text_to_int(row["stock"]),
            }
            products.append(product)
    return products


def get_products_by_id(products: list[dict]) -> dict[str, dict]:
    """
    Renvoie un dictionnaire {product_id: produit} pour retrouver un produit directement, sans boucle.
    """
    products_by_id = {}
    for product in products:
        products_by_id[product["product_id"]] = product
    return products_by_id


def print_products(products: list[dict]) -> None:
    """
    Affiche la liste des produits de façon lisible.
    """
    if not products:
        print("No product found.")
    for product in products:
        # Le prix peut valoir None (prix vide dans le CSV) : on ne peut pas le formater en euros
        if product["price"] is None:
            price_text = "invalid"
        else:
            price_text = f"{product['price']:.2f} €"
        print(
            f"Product ID: {product['product_id']}, Name: {product['name']}, "
            f"Category: {product['category']}, Price: {price_text}, Stock: {product['stock']}"
        )


def get_count_of_products(products: list[dict]) -> int:
    """
    Renvoie le nombre de produits.
    """
    return len(products)


def get_product_anomalies(products: list[dict], sold_quantities: dict[str, int]) -> list[tuple[str, str, str]]:
    """
    Renvoie une liste de (fichier, id, raison) pour les id en double, les prix ou stocks invalides,
    les produits jamais vendus et ceux dont les ventes confirmées dépassent le stock.
    sold_quantities est un dictionnaire {product_id: quantité vendue}.
    """
    anomalies = []
    seen_ids = []
    for product in products:
        product_id = product["product_id"]
        price = product["price"]
        stock = product["stock"]

        # 1. doublon : cet id a déjà été vu plus haut dans la liste
        if product_id in seen_ids:
            anomalies.append(("produits.csv", product_id, "duplicate id"))
        seen_ids.append(product_id)

        # 2. valeurs du fichier elles-mêmes : prix et stock
        if price is None or price < 0:
            anomalies.append(("produits.csv", product_id, "invalid price"))
        if stock is None or stock < 0:
            anomalies.append(("produits.csv", product_id, "invalid stock"))

        # 3. comparaison avec les ventes : jamais vendu, ou vendu plus que le stock
        sold = sold_quantities.get(product_id, 0)
        if sold == 0:
            anomalies.append(("produits.csv", product_id, "never sold"))
        elif stock is not None and sold > stock:
            anomalies.append(("produits.csv", product_id, f"{sold} sold for a stock of {stock}"))
    return anomalies
