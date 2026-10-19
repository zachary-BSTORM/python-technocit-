# Tout ce qui concerne l'utilisateur : affichage du menu, saisies au clavier
# (qui reposent la question tant que la réponse n'est pas valide) et affichage des anomalies.


def print_menu() -> None:
    """
    Affiche la liste des options disponibles.
    """
    print()
    print("Please select an option:")
    print("1. Read orders")
    print("2. Read customers")
    print("3. Read products")
    print("4. Show confirmed orders")
    print("5. Show orders by date")
    print("6. Show customers by city")
    print("7. Show orders with amount greater than")
    print("8. Show amount by customer")
    print("9. Show amount by product")
    print("10. Show number of orders by month")
    print("11. Show top 5 customers by amount")
    print("12. Show best product")
    print("13. Show anomalies in orders")
    print("14. Show anomalies in products")
    print("15. Show anomalies in customers")
    print("16. Create customer report (CSV)")
    print("17. Exit")


def ask_int(message: str, minimum: int | None = None, maximum: int | None = None) -> int:
    """
    Demande un nombre entier jusqu'à ce que la saisie soit valide (éventuellement entre minimum et maximum).
    """
    # On boucle tant que la saisie n'est pas correcte : on ne sort que par le return
    while True:
        try:
            value = int(input(message))
        except ValueError:
            # "abc" ou "" : int() échoue, on redemande
            print("Invalid input. Please enter a whole number.")
            continue
        if (minimum is not None and value < minimum) or (maximum is not None and value > maximum):
            print(f"Please enter a number between {minimum} and {maximum}.")
            continue
        return value


def ask_float(message: str) -> float:
    """
    Demande un nombre décimal jusqu'à ce que la saisie soit valide. Accepte "500", "500.5" ou "500,5".
    """
    while True:
        try:
            # On remplace la virgule par un point : float() n'accepte que "500.5"
            return float(input(message).replace(",", "."))
        except ValueError:
            print("Invalid input. Please enter a number.")


def ask_text(message: str) -> str:
    """
    Demande un texte non vide et le renvoie sans les espaces autour.
    """
    while True:
        # strip() enlève les espaces autour : " 12 " devient "12"
        text = input(message).strip()
        if text:
            return text
        print("Please enter a value.")


def get_user_choice() -> int:
    """
    Demande le choix du menu jusqu'à obtenir un nombre entre 1 et 17.
    """
    return ask_int("Enter your choice: ", 1, 17)


def print_anomalies(anomalies: list[tuple[str, str, str]]) -> None:
    """
    Affiche une liste de (fichier, id, raison) sous la forme "[fichier] id X : raison".
    """
    if not anomalies:
        print("No anomaly found.")
    # Chaque anomalie est un tuple de 3 éléments qu'on "déballe" directement dans le for
    for file_name, item_id, reason in anomalies:
        # :<16 et :<4 alignent les colonnes à gauche sur 16 et 4 caractères
        print(f"{'[' + file_name + ']':<16} id {item_id:<4} : {reason}")
    print(f"{len(anomalies)} anomalies.")
