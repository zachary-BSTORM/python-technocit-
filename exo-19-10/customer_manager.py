# Tout ce qui concerne les clients : lecture de clients.csv, affichage, filtre par ville,
# anomalies et rapport CSV.
# Un client est un dictionnaire : {"customer_id": "1", "name": "Dupont SPRL", "city": "Namur", "type": "entreprise"}

import csv


def read_customers_from_csv() -> list[dict]:
    """
    Lit clients.csv et renvoie la liste des clients (un dictionnaire par client).
    Les colonnes françaises du CSV (id, nom, ville, type) sont renommées en clés anglaises.
    """
    customers = []
    with open("clients.csv", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # row contient les colonnes du CSV (en français) ; on construit notre propre dictionnaire
            customer = {
                "customer_id": row["id"],
                "name": row["nom"],
                "city": row["ville"],
                "type": row["type"],
            }
            customers.append(customer)
    return customers


def get_customers_by_id(customers: list[dict]) -> dict[str, dict]:
    """
    Renvoie un dictionnaire {customer_id: client} pour retrouver un client directement, sans boucle.
    """
    customers_by_id = {}
    for customer in customers:
        # Si un id est en double, le dernier client lu remplace le premier
        customers_by_id[customer["customer_id"]] = customer
    return customers_by_id


def print_customers(customers: list[dict]) -> None:
    """
    Affiche la liste des clients de façon lisible.
    """
    if not customers:
        print("No customer found.")
    for customer in customers:
        # "or '-'" : si la ville est vide (""), on affiche "-" à la place
        print(
            f"Customer ID: {customer['customer_id']}, Name: {customer['name']}, "
            f"City: {customer['city'] or '-'}, Type: {customer['type']}"
        )


def get_count_of_customers(customers: list[dict]) -> int:
    """
    Renvoie le nombre de clients.
    """
    return len(customers)


def get_customers_by_city(customers: list[dict], city: str) -> list[dict]:
    """
    Renvoie les clients d'une ville donnée. La comparaison ignore les majuscules et les espaces ("namur " = "Namur").
    """
    # On met les deux côtés en minuscules et sans espaces pour comparer "Namur" et " namur"
    wanted_city = city.strip().lower()
    return [
        customer
        for customer in customers
        if customer["city"].strip().lower() == wanted_city
    ]


def get_customer_anomalies(customers: list[dict]) -> list[tuple[str, str, str]]:
    """
    Renvoie une liste de (fichier, id, raison) pour les id en double, les villes vides et les types inconnus.
    """
    anomalies = []
    seen_ids = []
    for customer in customers:
        customer_id = customer["customer_id"]

        # Si on a déjà vu cet id plus haut dans la liste, c'est un doublon
        if customer_id in seen_ids:
            anomalies.append(("clients.csv", customer_id, "duplicate id"))
        seen_ids.append(customer_id)

        if customer["city"].strip() == "":
            anomalies.append(("clients.csv", customer_id, "empty city"))
        if customer["type"] not in ["particulier", "entreprise"]:
            anomalies.append(
                ("clients.csv", customer_id, f"unknown type '{customer['type']}'")
            )
    return anomalies


def write_customer_report(
    customers_by_id: dict[str, dict],
    amounts_by_customer: dict[str, float],
    orders_count_by_customer: dict[str, int],
) -> int:
    """
    Écrit rapport_clients.csv avec, pour chaque client : nom, ville, nombre de commandes confirmées
    et montant total. Un client sans commande a 0. Renvoie le nombre de lignes écrites.
    """
    # 1. construire une ligne (un dictionnaire) par client
    rows = []
    for customer_id, customer in customers_by_id.items():
        # .get(customer_id, 0) donne 0 pour un client qui n'a aucune commande
        row = {
            "name": customer["name"],
            "city": customer["city"],
            "confirmed_orders": orders_count_by_customer.get(customer_id, 0),
            "total_amount": f"{amounts_by_customer.get(customer_id, 0):.2f}",
        }
        rows.append(row)

    # 2. écrire le fichier : fieldnames donne l'ordre des colonnes, writeheader() la ligne de titres
    with open("rapport_clients.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file, fieldnames=["name", "city", "confirmed_orders", "total_amount"]
        )
        writer.writeheader()
        writer.writerows(rows)
    return len(rows)


def print_amounts_by_customer(ranking: list[tuple[str, float]]) -> None:
    """
    Affiche une liste de (nom du client, montant) avec le rang de chacun.
    """
    rank = 1
    for name, amount in ranking:
        print(f"{rank}. {name:<22} {amount:>10.2f} €")
        rank += 1
