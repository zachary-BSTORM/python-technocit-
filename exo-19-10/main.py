# Point d'entrée de l'application : charge les données une seule fois,
# puis affiche le menu en boucle et appelle la bonne fonction selon le choix.

from customer_manager import (
    get_count_of_customers,
    get_customer_anomalies,
    get_customers_by_city,
    get_customers_by_id,
    print_amounts_by_customer,
    print_customers,
    read_customers_from_csv,
    write_customer_report,
)
from menu import (
    ask_float,
    ask_int,
    ask_text,
    get_user_choice,
    print_anomalies,
    print_menu,
)
from order_manager import (
    get_amount_by_customer,
    get_best_product,
    get_count_of_orders,
    get_count_of_orders_by_month,
    get_count_of_sales_by_customer,
    get_order_anomalies,
    get_orders_by_customer,
    get_orders_by_date,
    get_orders_by_state,
    get_orders_with_amount_greater_than,
    get_sold_quantities,
    get_top_customers_by_amount,
    get_total_amount_by_product,
    get_valid_sales,
    print_orders,
    read_order_from_csv,
)
from product_manager import (
    get_count_of_products,
    get_product_anomalies,
    get_products_by_id,
    print_products,
    read_products_from_csv,
)


def show_amount_by_customer(
    sales: list[tuple[dict, float]], customers_by_id: dict[str, dict]
) -> None:
    """
    Demande l'id d'un client, puis affiche ses commandes confirmées et leur montant total.
    """
    customer_id = ask_text("Enter customer ID: ")
    # On vérifie que le client existe avant d'aller plus loin
    if customer_id not in customers_by_id:
        print(f"Customer {customer_id} does not exist.")
        return
    customer = customers_by_id[customer_id]

    total = 0
    for order, amount in get_orders_by_customer(sales, customer_id):
        print(
            f"Order ID: {order['order_id']}, Product ID: {order['product_id']}, Quantity: {order['quantity']}, Amount: {amount:.2f} €"
        )
        total += amount
    print(f"Total amount for {customer['name']}: {total:.2f} €")


def show_amount_by_product(
    sales: list[tuple[dict, float]], products_by_id: dict[str, dict]
) -> None:
    """
    Demande l'id d'un produit, puis affiche le montant total de ses commandes confirmées.
    """
    product_id = ask_text("Enter product ID: ")
    if product_id not in products_by_id:
        print(f"Product {product_id} does not exist.")
        return
    product = products_by_id[product_id]
    total = get_total_amount_by_product(sales, product_id)
    print(f"Total amount for {product['name']}: {total:.2f} €")


def main() -> None:
    """
    Charge les données une seule fois, puis affiche le menu jusqu'à ce que l'utilisateur choisisse de quitter.
    """
    # 1. lire les trois fichiers
    try:
        customers = read_customers_from_csv()
        products = read_products_from_csv()
        orders = read_order_from_csv()
    except FileNotFoundError as error:
        # Un des CSV est absent ou mal nommé : message clair au lieu d'une erreur Python
        print(f"CSV file not found: {error.filename}")
        return

    # 2. créer les index {id: dictionnaire} pour retrouver un client / produit sans boucle
    customers_by_id = get_customers_by_id(customers)
    products_by_id = get_products_by_id(products)

    # 3. calculer une fois pour toutes les ventes valides (commande confirmée + montant)
    sales = get_valid_sales(orders, customers_by_id, products_by_id)

    print("Welcome to csvReader")
    print(
        f"{get_count_of_customers(customers)} customers, {get_count_of_products(products)} products, {get_count_of_orders(orders)} orders loaded."
    )

    stop_app = False
    while not stop_app:
        print_menu()
        # get_user_choice() redemande jusqu'à obtenir un nombre entre 1 et 17
        choice = get_user_choice()

        # match/case : chaque "case" correspond à une option du menu
        match choice:
            case 1:
                print_orders(orders)
            case 2:
                print_customers(customers)
            case 3:
                print_products(products)
            case 4:
                confirmed_orders = get_orders_by_state(orders, "confirmee")
                print_orders(confirmed_orders, products_by_id)
                print(f"{len(confirmed_orders)} confirmed orders.")
            case 5:
                year = ask_int("Enter year (YYYY): ", 1900, 2100)
                month = ask_int("Enter month (MM): ", 1, 12)
                print_orders(get_orders_by_date(orders, year, month), products_by_id)
            case 6:
                city = ask_text("Enter city: ")
                print_customers(get_customers_by_city(customers, city))
            case 7:
                minimum = ask_float("Enter amount: ")
                for order, amount in get_orders_with_amount_greater_than(
                    sales, minimum
                ):
                    customer_name = customers_by_id[order["customer_id"]]["name"]
                    print(
                        f"Order ID: {order['order_id']}, Customer: {customer_name}, Amount: {amount:.2f} €"
                    )
            case 8:
                show_amount_by_customer(sales, customers_by_id)
            case 9:
                show_amount_by_product(sales, products_by_id)
            case 10:
                # sorted() trie les (mois, nombre) par mois : "2026-01", "2026-02"...
                for month, count in sorted(
                    get_count_of_orders_by_month(orders).items()
                ):
                    print(f"{month:<14} {count}")
            case 11:
                print_amounts_by_customer(
                    get_top_customers_by_amount(sales, customers_by_id)
                )
            case 12:
                sold_quantities = get_sold_quantities(
                    orders, customers_by_id, products_by_id
                )
                best = get_best_product(sold_quantities, products_by_id)
                if best is None:
                    print("No product sold.")
                else:
                    name, quantity = best
                    print(f"Best product: {name} ({quantity} sold)")
            case 13:
                print_anomalies(
                    get_order_anomalies(orders, customers_by_id, products_by_id)
                )
            case 14:
                sold_quantities = get_sold_quantities(
                    orders, customers_by_id, products_by_id
                )
                print_anomalies(get_product_anomalies(products, sold_quantities))
            case 15:
                print_anomalies(get_customer_anomalies(customers))
            case 16:
                amounts = get_amount_by_customer(sales)
                counts = get_count_of_sales_by_customer(sales)
                number_of_lines = write_customer_report(
                    customers_by_id, amounts, counts
                )
                print(
                    f"Report created: rapport_clients.csv ({number_of_lines} customers)"
                )
            case 17:
                print("Exiting the application. Goodbye!")
                stop_app = True


if __name__ == "__main__":
    main()
