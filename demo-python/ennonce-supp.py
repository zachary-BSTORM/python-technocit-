
def get_number(message : str):
    while True:
        input_user = input(f"Entrez un nombre pour {message}")
        try:
            value_int = int(input_user)
            if isinstance(value_int,int):
                return value_int
        except:
            print("La valeur est incorrecte")
            
get_number("test")