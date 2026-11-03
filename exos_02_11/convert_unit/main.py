# main.py — Exercice 2 : Méthodes statiques, convertisseur d'unités
import math

from models import Convertisseur


# ---------------------------------------------------------------
# Méthodes simples appelées directement sur la classe
# ---------------------------------------------------------------
print(f"100 °C = {Convertisseur.celsius_vers_fahrenheit(100)} °F")
print(f"42.195 km = {Convertisseur.km_vers_miles(42.195):.2f} mi")


# ---------------------------------------------------------------
# Conversions génériques (les erreurs sont capturées)
# ---------------------------------------------------------------
conversions = [
    (98.6, "F", "C"),
    (300, "K", "F"),      # K → C → F : passage obligé par les Celsius
    (26.2, "mi", "km"),
    (75, "kg", "lb"),
    (20, "C", "C"),       # même unité : valeur renvoyée telle quelle
    (5, "km", "kg"),      # familles différentes → ValueError
    (12, "m", "km"),      # unité inconnue → ValueError
]

print("Conversions :")
for valeur, de, vers in conversions:
    try:
        resultat = Convertisseur.convertir(valeur, de, vers)
    except ValueError as e:
        print(f"  {valeur} {de} → {vers} : {e}")
    else:
        print(f"  {valeur} {de} → {resultat:.2f} {vers}")


# ---------------------------------------------------------------
# Aller-retour C → K → C
# ---------------------------------------------------------------
depart = 37.5
en_kelvin = Convertisseur.convertir(depart, "C", "K")
retour = Convertisseur.convertir(en_kelvin, "K", "C")

# isclose plutôt que == : les flottants peuvent différer d'un infime arrondi
assert math.isclose(retour, depart), f"Aller-retour raté : {retour} ≠ {depart}"
print(f"Aller-retour : {depart} C → {en_kelvin:.2f} K → {retour:.2f} C")