from __future__ import annotations

class Produit:
    def __init__(self, reference:str, nom:str, prix:float, stock:int) -> None:
        pass

    @classmethod
    def depuis_dict(cls, donnees:dict[str, str]) -> Produit:
        pass

    @classmethod
    def depuis_chaine(cls, texte: str) -> Produit:
        pass

    @classmethod
    def echantillon(cls, nom:str):
        pass

    def __str__(self) -> str:
        pass

class ProduitSolde(Produit):
    def __str__(self) -> str:
        pass