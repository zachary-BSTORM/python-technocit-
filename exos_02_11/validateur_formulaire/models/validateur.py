class Validateur:
    
    @staticmethod
    def est_email_valide(email: str) -> bool:
        if email.count("@") != 1 or " " in email:
            return False

        avant, apres = email.split("@")
        if avant == "":
            return False

        return "." in apres and not apres.startswith(".") and not apres.endswith(".")

    @staticmethod
    def est_code_postal_valide(code: str) -> bool:
        return len(code) == 5 and code.isdigit()

    @staticmethod
    def est_telephone_valide(numero: str) -> bool:
        result = numero.replace(" ", "").replace(".", "")
        return len(result) == 10 and result.isdecimal() and result.startswith("0")

    @staticmethod
    def est_mot_de_passe_fort(mdp: str) -> bool:
        if len(mdp) < 8:
            return False

        majuscule = any(c.isupper() for c in mdp)
        minuscule = any(c.islower() for c in mdp)
        numerique = any(c.isdecimal() for c in mdp)
        special = any(not c.isalnum() for c in mdp)

        return majuscule and minuscule and numerique and special

    @staticmethod
    def valider_formulaire(formulaire: dict) -> list[str]:
        erreurs = []

        if not Validateur.est_email_valide(formulaire.get("email", "")):
            erreurs.append("email")

        if not Validateur.est_code_postal_valide(formulaire.get("code_postal", "")):
            erreurs.append("code_postal")

        if not Validateur.est_telephone_valide(formulaire.get("telephone", "")):
            erreurs.append("telephone")

        if not Validateur.est_mot_de_passe_fort(formulaire.get("mot_de_passe", "")):
            erreurs.append("mot_de_passe")
        return erreurs
