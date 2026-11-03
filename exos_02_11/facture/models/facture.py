from decimal import Decimal, ROUND_HALF_UP


class Facture:
    def __init__(self, numero: str, client: str) -> None:
        self.numero = numero
        self.client = client
        self.lignes = []  # (designation,quantite , prix_unitaire,taux_tva)

    def ajouter_ligne(
        self,
        designation: str,
        quantite: int,
        prix_unitaire: float,
        taux_tva: float = 0.20,
    ) -> None:

        if quantite <= 0:
            raise ValueError(f"Quantité invalide pour : {designation} : {quantite}")

        if prix_unitaire < 0:
            raise ValueError(f"Prix invalide pour : {designation} : {prix_unitaire}")

        self.lignes.append((designation, quantite, prix_unitaire, taux_tva))

    @staticmethod
    def arrondir_centimes(montant: float) -> float:
        return float(Decimal(str(montant)).quantize(Decimal("0.01"), ROUND_HALF_UP))

    @staticmethod
    def calculer_tva(montant_ht: float, taux: float) -> float:
        return Facture.arrondir_centimes(montant_ht * taux)

    @staticmethod
    def formater_montant(montant: float) -> str:
        centimes = round(montant * 100)
        euros = str(centimes // 100)
        reste = str(centimes % 100).zfill(2)

        blocs = []
        while len(euros) > 3:
            blocs.insert(0, euros[-3:])
            euros = euros[:-3]
        blocs.insert(0, euros)

        return " ".join(blocs) + "," + reste + " €"

    def montant_ligne(self, quantite: int, prix_unitaire: float) -> float:
        return self.arrondir_centimes(quantite * prix_unitaire)

    def total_ht(self) -> float:
        total = 0

        for designation, quantite, prix_unitaire, taux in self.lignes:
            total += self.montant_ligne(quantite, prix_unitaire)
        return self.arrondir_centimes(total)

    def total_tva(self) -> float:
        total = 0

        for designation, quantite, prix_unitaire, taux in self.lignes:
            total += self.calculer_tva(
                self.montant_ligne(quantite, prix_unitaire), taux
            )
        return self.arrondir_centimes(total)

    def total_ttc(self) -> float:
        return self.arrondir_centimes(self.total_ht() + self.total_tva())
