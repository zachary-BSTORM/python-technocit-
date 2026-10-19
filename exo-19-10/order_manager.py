# Tout ce qui concerne les commandes : lecture de commandes.csv, filtres, calcul des montants,
# regroupements (par client, par mois...), classements et anomalies.
#
# Une commande est un dictionnaire :
# {"order_id": "103", "customer_id": "12", "product_id": "5", "quantity": 4, "raw_quantity": "4",
#  "date": date(2026, 3, 14), "raw_date": "2026-03-14", "state": "confirmee"}
#
# Une "vente" est un tuple (commande, montant) : une commande confirmée dont le montant
# a pu être calculé. Toutes les statistiques sont faites sur ces ventes.

import csv
from datetime import date


def text_to_int(text: str) -> int | None:
    """
    Convertit un texte en nombre entier ("4" -> 4). Renvoie None s'il est vide ou invalide ("deux").
    """
    try:
        return int(text)
    except ValueError:
        return None


def text_to_date(text: str) -> date | None:
    """
    Convertit un texte "AAAA-MM-JJ" en date. Renvoie None s'il est vide ou invalide ("2026-13-02").
    """
    try:
        return date.fromisoformat(text)
    except ValueError:
        return None


def read_order_from_csv() -> list[dict]:
    """
    Lit commandes.csv et renvoie la liste des commandes (un dictionnaire par commande).
    La quantité devient un int et la date une date ; une valeur invalide devient None au lieu de planter.
    Les textes d'origine sont gardés ("raw_quantity", "raw_date") pour les afficher dans les anomalies.
    """
    orders = []
    with open("commandes.csv", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            order = {
                "order_id": row["id"],
                "customer_id": row["client_id"],
                "product_id": row["produit_id"],
                # Valeur convertie pour les calculs (None si "deux" ou "")...
                "quantity": text_to_int(row["quantite"]),
                # ...et texte d'origine, pour pouvoir afficher POURQUOI c'est invalide
                "raw_quantity": row["quantite"],
                "date": text_to_date(row["date"]),
                "raw_date": row["date"],
                "state": row["etat"],
            }
            orders.append(order)
    return orders


def print_orders(
    orders: list[dict], products_by_id: dict[str, dict] | None = None
) -> None:
    """
    Affiche la liste des commandes de façon lisible.
    Si products_by_id est fourni, le montant de chaque commande est aussi affiché.
    """
    if not orders:
        print("No order found.")
    for order in orders:
        line = (
            f"Order ID: {order['order_id']}, Customer ID: {order['customer_id']}, "
            f"Product ID: {order['product_id']}, Quantity: {order['raw_quantity'] or '-'}, "
            f"Date: {order['raw_date'] or '-'}, State: {order['state']}"
        )
        # Le montant n'est ajouté que si on a reçu l'index des produits (paramètre optionnel)
        if products_by_id is not None:
            amount = get_total_price(order, products_by_id.get(order["product_id"]))
            if amount is None:
                line += ", Amount: invalid"
            else:
                line += f", Amount: {amount:.2f} €"
        print(line)


def get_count_of_orders(orders: list[dict]) -> int:
    """
    Renvoie le nombre de commandes.
    """
    return len(orders)


def get_orders_by_state(orders: list[dict], state: str) -> list[dict]:
    """
    Renvoie les commandes dont l'état est exactement celui demandé (annulee, confirmee, brouillon).
    """
    # Comparaison stricte : "Confirmee" (avec majuscule) n'est PAS considérée comme "confirmee"
    return [order for order in orders if order["state"] == state]


def get_orders_by_date(orders: list[dict], year: int, month: int) -> list[dict]:
    """
    Renvoie les commandes d'un mois donné. Les commandes avec une date invalide sont ignorées.
    """
    result = []
    for order in orders:
        # Une date invalide vaut None : on la saute, sinon .year planterait
        if order["date"] is None:
            continue
        if order["date"].year == year and order["date"].month == month:
            result.append(order)
    return result


def get_count_of_orders_by_month(orders: list[dict]) -> dict[str, int]:
    """
    Compte toutes les commandes (tous états) par mois "AAAA-MM". Les dates invalides sont regroupées sous "invalid date".
    """
    counts = {}
    for order in orders:
        if order["date"] is None:
            key = "invalid date"
        else:
            # strftime("%Y-%m") transforme la date 2026-03-14 en texte "2026-03" : c'est la clé du groupe
            key = order["date"].strftime("%Y-%m")
        # .get(key, 0) : 0 la première fois qu'on voit ce mois, puis on ajoute 1
        counts[key] = counts.get(key, 0) + 1
    return counts


def get_total_price(order: dict, product: dict | None) -> float | None:
    """
    Renvoie quantité x prix unitaire d'une commande, ou None si le produit, le prix
    ou la quantité est absent ou invalide (la quantité doit être > 0 et le prix >= 0).
    """
    # On vérifie chaque ingrédient du calcul avant de multiplier
    if product is None:
        return None
    if product["price"] is None or product["price"] < 0:
        return None
    if order["quantity"] is None or order["quantity"] <= 0:
        return None
    return order["quantity"] * product["price"]


def get_valid_sales(
    orders: list[dict],
    customers_by_id: dict[str, dict],
    products_by_id: dict[str, dict],
) -> list[tuple[dict, float]]:
    """
    Renvoie les commandes confirmées utilisables dans les calculs, sous forme de liste de (commande, montant).
    Une commande est gardée si elle est confirmée, que son client existe et que son montant peut être calculé.
    """
    sales = []
    for order in get_orders_by_state(orders, "confirmee"):
        # "in" sur un dictionnaire est immédiat : pas besoin de reparcourir la liste des clients
        if order["customer_id"] not in customers_by_id:
            continue
        amount = get_total_price(order, products_by_id.get(order["product_id"]))
        if amount is not None:
            sales.append((order, amount))
    return sales


def get_orders_with_amount_greater_than(
    sales: list[tuple[dict, float]], minimum: float
) -> list[tuple[dict, float]]:
    """
    Renvoie les ventes valides dont le montant est strictement supérieur au minimum donné.
    """
    return [(order, amount) for order, amount in sales if amount > minimum]


def get_orders_by_customer(
    sales: list[tuple[dict, float]], customer_id: str
) -> list[tuple[dict, float]]:
    """
    Renvoie les ventes valides d'un client donné.
    """
    return [
        (order, amount)
        for order, amount in sales
        if order["customer_id"] == customer_id
    ]


def get_total_amount_by_product(
    sales: list[tuple[dict, float]], product_id: str
) -> float:
    """
    Renvoie le montant total des ventes valides d'un produit donné.
    """
    total = 0
    for order, amount in sales:
        if order["product_id"] == product_id:
            total += amount
    return total


def get_amount_by_customer(sales: list[tuple[dict, float]]) -> dict[str, float]:
    """
    Additionne le montant des ventes valides pour chaque id de client.
    """
    # Dictionnaire accumulateur : {customer_id: total}
    totals = {}
    for order, amount in sales:
        customer_id = order["customer_id"]
        totals[customer_id] = totals.get(customer_id, 0) + amount
    return totals


def get_count_of_sales_by_customer(sales: list[tuple[dict, float]]) -> dict[str, int]:
    """
    Compte les ventes valides pour chaque id de client.
    """
    counts = {}
    for order, amount in sales:
        customer_id = order["customer_id"]
        counts[customer_id] = counts.get(customer_id, 0) + 1
    return counts


def get_top_customers_by_amount(
    sales: list[tuple[dict, float]], customers_by_id: dict[str, dict], limit: int = 5
) -> list[tuple[str, float]]:
    """
    Renvoie les meilleurs clients sous forme de liste de (nom, montant), du plus grand au plus petit montant.
    En cas d'égalité, les clients sont départagés par ordre alphabétique du nom.
    """
    # 1. transformer {customer_id: total} en liste de (nom, total arrondi à 2 décimales)
    ranking = []
    for customer_id, total in get_amount_by_customer(sales).items():
        ranking.append((customers_by_id[customer_id]["name"], round(total, 2)))

    # 2. trier : -montant pour avoir le plus grand d'abord, puis nom de A à Z en cas d'égalité
    ranking.sort(key=lambda item: (-item[1], item[0]))

    # 3. ne garder que les premiers
    return ranking[:limit]


def get_sold_quantities(
    orders: list[dict],
    customers_by_id: dict[str, dict],
    products_by_id: dict[str, dict],
) -> dict[str, int]:
    """
    Additionne les quantités des commandes confirmées pour chaque id de produit.
    Le prix n'est pas nécessaire ici : un produit sans prix sort quand même du stock.
    """
    quantities = {}
    for order in get_orders_by_state(orders, "confirmee"):
        # On ignore les quantités invalides et les commandes qui pointent vers un client/produit inconnu
        if order["quantity"] is None or order["quantity"] <= 0:
            continue
        if (
            order["customer_id"] not in customers_by_id
            or order["product_id"] not in products_by_id
        ):
            continue
        product_id = order["product_id"]
        quantities[product_id] = quantities.get(product_id, 0) + order["quantity"]
    return quantities


def get_best_product(
    sold_quantities: dict[str, int], products_by_id: dict[str, dict]
) -> tuple[str, int] | None:
    """
    Renvoie (nom, quantité) du produit le plus vendu, ou None si rien n'a été vendu.
    """
    best_id = None
    best_quantity = 0
    # On garde en mémoire le meilleur trouvé jusqu'ici et on le remplace si on trouve mieux
    for product_id, quantity in sold_quantities.items():
        if quantity > best_quantity:
            best_id = product_id
            best_quantity = quantity

    if best_id is None:
        return None
    return products_by_id[best_id]["name"], best_quantity


def get_order_anomalies(
    orders: list[dict],
    customers_by_id: dict[str, dict],
    products_by_id: dict[str, dict],
) -> list[tuple[str, str, str]]:
    """
    Renvoie une liste de (fichier, id, raison) pour les id en double, les clients ou produits inconnus,
    les quantités invalides, les états inconnus et les dates invalides.
    """
    anomalies = []
    seen_ids = []
    # Une même commande peut avoir plusieurs problèmes : chaque contrôle est un "if" séparé (pas de elif)
    for order in orders:
        order_id = order["order_id"]

        if order_id in seen_ids:
            anomalies.append(("commandes.csv", order_id, "duplicate id"))
        seen_ids.append(order_id)

        if order["customer_id"] not in customers_by_id:
            anomalies.append(
                (
                    "commandes.csv",
                    order_id,
                    f"customer {order['customer_id']} does not exist",
                )
            )
        if order["product_id"] not in products_by_id:
            anomalies.append(
                (
                    "commandes.csv",
                    order_id,
                    f"product {order['product_id']} does not exist",
                )
            )
        if order["quantity"] is None or order["quantity"] <= 0:
            anomalies.append(
                (
                    "commandes.csv",
                    order_id,
                    f"invalid quantity '{order['raw_quantity']}'",
                )
            )
        if order["state"] not in ["brouillon", "confirmee", "annulee"]:
            anomalies.append(
                ("commandes.csv", order_id, f"unknown state '{order['state']}'")
            )
        if order["date"] is None:
            anomalies.append(
                ("commandes.csv", order_id, f"invalid date '{order['raw_date']}'")
            )
    return anomalies
