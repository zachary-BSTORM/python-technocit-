class Convertisseur:
    @staticmethod
    def celsius_vers_fahrenheit(c: float) -> float:
        return c * 9 / 5 + 32

    @staticmethod
    def fahrenheit_vers_celsius(f: float) -> float:
        return (f - 32) * 5 / 9

    @staticmethod
    def celsius_vers_kelvin(c: float) -> float:
        return c + 273.15

    @staticmethod
    def kelvin_vers_celsius(k: float) -> float:
        return k - 273.15

    @staticmethod
    def km_vers_miles(km: float) -> float:
        return km * 0.621371

    @staticmethod
    def miles_vers_km(mi: float) -> float:
        return mi / 0.621371

    @staticmethod
    def kg_vers_livres(kg: float) -> float:
        return kg * 2.20462

    @staticmethod
    def livres_vers_kg(lb: float) -> float:
        return lb / 2.20462

    @staticmethod
    def convertir(valeur: float, de: str, vers: str) -> float:
        temperatures = ["C", "F", "K"]
        unites = ["C", "F", "K", "km", "mi", "kg", "lb"]

        if de not in unites:
            raise ValueError(f"Unité inconnue : {de}")
        if vers not in unites:
            raise ValueError(f"Unité inconnue : {vers}")
                
        if de == vers:
            return valeur
        
        if de in temperatures and vers in temperatures:
            if de == "F":
                valeur = Convertisseur.fahrenheit_vers_celsius(valeur)
                
            if de == "K":
                valeur = Convertisseur.kelvin_vers_celsius(valeur)
                
            if vers == "F":
                valeur = Convertisseur.celsius_vers_fahrenheit(valeur)
                
            if vers == "K":
                valeur = Convertisseur.celsius_vers_kelvin(valeur)
                
            return valeur
        
        if de == "km" and vers == "mi":
            return Convertisseur.km_vers_miles(valeur)
        
        if de == "mi" and vers == "km":
            return Convertisseur.miles_vers_km(valeur)
        
        if de == "kg" and vers == "lb":
            return Convertisseur.kg_vers_livres(valeur)
        
        if de == "lb" and vers == "kg":
            return Convertisseur.livres_vers_kg(valeur)
        
        raise ValueError(f"Conversion impossible de {de} vers {vers}")