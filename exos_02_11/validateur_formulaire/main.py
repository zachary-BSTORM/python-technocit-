# main.py — Exercice 1 : Méthodes statiques, Validateur de formulaire
from models import Validateur


def tester(titre: str, regle, valeurs: list[str]) -> None:
    """Affiche ✓ ou ✗ pour chaque valeur passée à la règle."""
    print(f"{titre} :")
    for valeur in valeurs:
        symbole = "✓" if regle(valeur) else "✗"
        print(f"  {valeur:<20}{symbole}")


# ---------------------------------------------------------------
# Règles appelées directement sur la classe (jamais d'instance)
# ---------------------------------------------------------------
tester(
    "E-mails",
    Validateur.est_email_valide,
    [
        "alice@exemple.fr",
        "bob@exemple",  # domaine sans point
        "@exemple.fr",  # rien avant le @
        "c d@exemple.fr",  # contient un espace
        "eve@@exemple.fr",  # deux @
    ],
)

tester(
    "Codes postaux",
    Validateur.est_code_postal_valide,
    [
        "75001",
        "7500",  # 4 chiffres
        "75A01",  # contient une lettre
    ],
)

tester(
    "Téléphones",
    Validateur.est_telephone_valide,
    [
        "06 12 34 56 78",
        "06.12.34.56.78",
        "12 34 56 78 90",  # ne commence pas par 0
        "06 12 34",  # trop court
    ],
)

tester(
    "Mots de passe",
    Validateur.est_mot_de_passe_fort,
    [
        "Azerty12!",
        "azerty12!",  # pas de majuscule
        "Azerty!!",  # pas de chiffre
        "Az1!",  # trop court
    ],
)


# ---------------------------------------------------------------
# Formulaires complets
# ---------------------------------------------------------------
formulaire_a = {
    "email": "alice@exemple.fr",
    "code_postal": "69003",
    "telephone": "07 98 76 54 32",
    "mot_de_passe": "Soleil#2026",
}

formulaire_b = {
    "email": "bob@exemple",
    "code_postal": "69003",
    "telephone": "07 98 76",
    # pas de mot de passe : le champ absent doit être signalé
}

for nom, formulaire in (("A", formulaire_a), ("B", formulaire_b)):
    invalides = Validateur.valider_formulaire(formulaire)
    if invalides:
        print(f"Formulaire {nom} : champs invalides → {', '.join(invalides)}")
    else:
        print(f"Formulaire {nom} : valide")
