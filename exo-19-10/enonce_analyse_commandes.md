

Une petite entreprise te transmet un export de son logiciel de gestion : ses **clients**, ses **produits** et ses **commandes**. La direction veut des réponses à plusieurs questions : combien vend-on ? qui sont nos meilleurs clients ? y a-t-il des erreurs dans nos données ?

Ta mission : écrire un programme Python qui lit ces fichiers et répond à ces questions, palier par palier.


---

## Règles du jeu

- Travail **individuel**, dans **un seul fichier** : `analyse.py`.
- Uniquement la **bibliothèque standard** de Python (pas de `pandas`).
- Ton code doit être **découpé en fonctions** : une fonction = une tâche. Pas de gros bloc de code de 200 lignes.
- Chaque fonction commence par un **commentaire** qui explique sa logique en une ou deux phrases.
- Les paliers sont **progressifs** : termine un palier avant de passer au suivant. Personne n'est censé tout finir, va le plus loin possible.

---

## Les fichiers fournis

Les trois fichiers sont au format CSV : séparateur virgule, encodage UTF-8, première ligne = noms des colonnes.

### `clients.csv`

| Colonne | Description | Exemple |
|---|---|---|
| `id` | Identifiant unique du client | `12` |
| `nom` | Nom du client | `Dupont SPRL` |
| `ville` | Ville | `Namur` |
| `type` | `particulier` ou `entreprise` | `entreprise` |

### `produits.csv`

| Colonne | Description | Exemple |
|---|---|---|
| `id` | Identifiant unique du produit | `5` |
| `nom` | Nom du produit | `Chaise de bureau` |
| `categorie` | Catégorie du produit | `Mobilier` |
| `prix_unitaire` | Prix en euros (point décimal) | `149.90` |
| `stock` | Quantité en stock | `20` |

### `commandes.csv`

| Colonne | Description | Exemple |
|---|---|---|
| `id` | Identifiant unique de la commande | `103` |
| `client_id` | Identifiant du client (renvoie à `clients.csv`) | `12` |
| `produit_id` | Identifiant du produit (renvoie à `produits.csv`) | `5` |
| `quantite` | Quantité commandée | `4` |
| `date` | Date au format `AAAA-MM-JJ` | `2026-03-14` |
| `etat` | `brouillon`, `confirmee` ou `annulee` | `confirmee` |

> 💡 Une commande ne contient qu'**un seul produit**. Les fichiers sont **liés par leurs identifiants** : `client_id` et `produit_id` désignent une ligne d'un autre fichier.

---

## Palier 1 : charger et compter

1. Écris une fonction qui lit un fichier CSV et renvoie une **liste de dictionnaires** (une ligne = un dictionnaire).
2. Affiche le nombre de clients, de produits et de commandes.
3. Affiche le nombre de commandes **par état** (combien de brouillons, de confirmées, d'annulées).

**Indice** : regarde le module `csv` et la classe `csv.DictReader`.

**Attention** : tout ce qui est lu dans un CSV est du **texte**. `"4"` n'est pas `4`.

---

## Palier 2 : filtrer

1. Affiche toutes les commandes **confirmées**.
2. Affiche les commandes passées en **mars 2026**.
3. Affiche les clients de type **entreprise** d'une ville donnée (la ville est passée en paramètre de ta fonction).

---

## Palier 3 : calculer

1. Pour chaque commande, calcule son **montant** : `quantité × prix unitaire du produit`.
2. Affiche le montant de chaque commande confirmée, avec le **nom du client** et le **nom du produit** (et pas seulement leurs identifiants).
3. Affiche les commandes confirmées dont le montant dépasse **500 €**.

**Question de réflexion** : pour trouver le prix d'un produit, combien de fois ton programme parcourt-il la liste des produits ? Que se passerait-il avec un million de commandes ?

---

## Palier 4 : indexer

1. Écris une fonction qui transforme une liste de dictionnaires en un **dictionnaire indexé par id** :
   `{ "5": {"id": "5", "nom": "Chaise de bureau", ...}, ... }`
2. Réécris le palier 3 en utilisant cet index pour retrouver un produit ou un client **directement**, sans boucle.

C'est une technique essentielle : retiens-la, tu la réutiliseras partout.

---

## Palier 5 : regrouper ⏱️ *mode examen*

> **Mode examen** : 30 minutes maximum. Avant d'écrire la moindre ligne de code, écris ta **logique en commentaires** (en français, étape par étape). Le formateur regardera d'abord tes commentaires, ensuite ton code.

1. Calcule le **chiffre d'affaires par client** (uniquement les commandes confirmées).
2. Calcule le **chiffre d'affaires par catégorie de produit**.
3. Calcule le **nombre de commandes par mois**.

**Indice** : un dictionnaire qui sert d'**accumulateur**. La méthode `dict.get()` peut t'aider.

---

## Palier 6 : classer

1. Affiche le **top 5 des clients** par chiffre d'affaires, du plus grand au plus petit.
2. Affiche le **produit le plus vendu** (en quantité).
3. Que fait ton programme si deux clients ont exactement le même chiffre d'affaires ? Décide d'une règle (par exemple : ordre alphabétique) et applique-la.

**Indice** : la fonction `sorted()` et son paramètre `key`.

---

## Palier 7 : détecter les anomalies ⏱️ *mode examen*

> Même règle : 30 minutes, logique en commentaires d'abord.

Écris une fonction qui produit une **liste des anomalies** trouvées dans les données, par exemple :

- une commande qui renvoie à un **client inexistant** ;
- une commande qui renvoie à un **produit inexistant** ;
- une **quantité** nulle, négative ou qui n'est pas un nombre ;
- un **état** qui n'est pas l'un des trois états prévus ;
- un **identifiant en double** dans un fichier ;
- un **produit jamais vendu** ;
- un produit dont les commandes confirmées **dépassent le stock**.

Chaque anomalie est affichée avec le fichier, l'identifiant concerné et la raison :

```
[commandes.csv] id 117 : client 999 inexistant
[produits.csv]  id 8   : jamais vendu
```

**Question de réflexion** : les anomalies doivent-elles être exclues des calculs des paliers précédents ? Ton chiffre d'affaires change-t-il ?

---

## Palier 8 (bonus) : produire un rapport

1. Écris un fichier `rapport_clients.csv` avec, pour chaque client : son nom, sa ville, son nombre de commandes confirmées et son chiffre d'affaires total.
2. Ajoute un **menu** en ligne de commande (`while True` + `input()`) pour choisir quelle analyse afficher.

**Indice** : `csv.DictWriter`.

---

## Déroulé de la journée

| Moment | Activité |
|---|---|
| Début de matinée | Présentation du sujet et des fichiers |
| Matinée | Paliers 1 à 4 |
| Fin de matinée | Point collectif : difficultés rencontrées |
| Début d'après-midi | Paliers 5 et 6 |
| Milieu d'après-midi | Palier 7, puis palier 8 pour les plus rapides |
| Fin de journée | Relecture croisée (30 min) puis démo de 2 ou 3 volontaires |

**Relecture croisée** : tu lis le code de ton voisin et tu lui donnes **une chose bien faite** et **une chose à améliorer**.

---

## Ce qui sera regardé

Comme lors d'un test technique, la **logique** compte plus que la syntaxe :

- Ta démarche est-elle claire et expliquée ?
- Ton programme résiste-t-il aux **cas limites** (valeur vide, mauvais type, référence introuvable) ?
- Ton code est-il découpé en fonctions qui font chacune **une seule chose** ?
- Tes noms de variables et de fonctions sont-ils **compréhensibles** ?

