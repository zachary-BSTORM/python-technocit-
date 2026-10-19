# Exercices progressifs : Horaires et réunions

Cinq exercices progressifs autour des horaires de travail et des réunions
(heures entières, pas d'AM/PM). Le format utilisé partout :

```python
start_work = 8                              # début de la journée (int)
end_work = 17                               # fin de la journée (int)
meetings = [[9, 10], [11, 13], [15, 16]]    # réunions : [[début, fin], ...]
```

Chaque exercice réutilise le précédent — l'exercice 5 assemble le tout.

---

## Exercice 1 — Trouver les plages libres

Écrivez une fonction qui reçoit `start_work`, `end_work` et `meetings`, et
qui retourne **toutes les plages horaires libres** pendant les heures de
travail, sous la forme `[[début, fin], ...]`.

Pour cet exercice, les réunions sont supposées **déjà triées et sans
chevauchement**.

```python
def free_slots(start_work, end_work, meetings):
```

**Exemple**

```python
start_work = 8
end_work = 17
meetings = [[9, 10], [11, 13], [15, 16]]
# → [[8, 9], [10, 11], [13, 15], [16, 17]]
```

**Cas supplémentaire** — une réunion colle au début et une autre à la fin de
la journée :

```python
start_work = 8
end_work = 17
meetings = [[8, 10], [12, 14], [15, 17]]
# → [[10, 12], [14, 15]]
```

---

## Exercice 2 — Fusionner les réunions qui se chevauchent

Écrivez une fonction qui reçoit une liste de réunions et qui **fusionne**
toutes celles qui se chevauchent. Cette fois, les réunions ne sont **pas
forcément triées**.

```python
def merge_meetings(meetings):
```

**Exemple 1**

```python
meetings = [[9, 11], [10, 13], [14, 16], [15, 17]]
# → [[9, 13], [14, 17]]
```

**Exemple 2**

```python
meetings = [[11, 13], [5, 8], [7, 10], [15, 16]]
# → [[5, 10], [11, 13], [15, 16]]
```

> Objectif pédagogique : réfléchir au **tri**, puis au **parcours** du
> tableau trié.

---

## Exercice 3 — Réunions à l'intérieur des heures de travail

Écrivez une fonction qui reçoit `start_work`, `end_work` et `meetings`.
Certaines réunions peuvent commencer **avant** le début du travail ou finir
**après** la fin. Retournez uniquement les périodes occupées **pendant** les
heures de travail (les réunions sont tronquées, celles entièrement en dehors
disparaissent).

```python
def clip_meetings(start_work, end_work, meetings):
```

**Exemple 1**

```python
start_work = 8
end_work = 17
meetings = [[5, 9], [11, 13], [15, 20]]
# → [[8, 9], [11, 13], [15, 17]]
```

**Exemple 2** — le résultat peut encore contenir des chevauchements :

```python
start_work = 9
end_work = 18
meetings = [[6, 10], [8, 12], [16, 20]]
# → [[9, 10], [9, 12], [16, 18]]
```

> Bonus : combinez ensuite avec l'exercice 2 pour éliminer ces
> chevauchements.

---

## Exercice 4 — Planning libre

Écrivez une fonction qui reçoit `start_work`, `end_work` et `meetings`, et
qui retourne les **heures libres**, en tenant compte de réunions qui peuvent
se chevaucher et déborder de la journée. Suivez ces 5 étapes :

1. garder uniquement la partie des réunions comprise dans les heures de
   travail *(exercice 3)* ;
2. trier les réunions ;
3. fusionner celles qui se chevauchent *(exercice 2)* ;
4. trouver les espaces libres entre les réunions *(exercice 1)* ;
5. prendre en compte le début et la fin de la journée de travail.

### Contraintes

- `start_work` et `end_work` sont des `int` ;
- une réunion est représentée par `[début, fin]` ;
- les réunions peuvent être dans n'importe quel ordre ;
- les réunions peuvent se chevaucher ;
- certaines réunions peuvent commencer avant `start_work` ;
- certaines réunions peuvent terminer après `end_work` ;
- deux réunions **qui se touchent** (`[13, 14]` et `[14, 16]`) forment une
  seule plage occupée ;
- le résultat doit être trié.

**Exemple décortiqué**

```python
start_work = 8
end_work = 17
meetings = [[5, 8], [7, 10], [9, 12], [13, 14], [13, 16], [16, 18]]

# Les réunions deviennent, après traitement (étapes 1 à 3) :
#   [[8, 12], [13, 17]]
# Les heures libres sont donc :
#   [[12, 13]]
```

---

## Exercice 5 — Planning complet ⭐

Assemblez le tout dans **la** fonction finale :

```python
def get_free_time(start_work, end_work, meetings):
```

qui retourne toutes les plages libres pendant la journée de travail, quelles
que soient les réunions reçues (mêmes contraintes qu'à l'exercice 4).

**Exemple 1**

```python
start_work = 8
end_work = 17
meetings = [[5, 8], [9, 11], [10, 13], [14, 15], [15, 16]]
# → [[8, 9], [13, 14], [16, 17]]
```

**Exemple 2**

```python
start_work = 8
end_work = 17
meetings = [[5, 10], [8, 12], [11, 14], [16, 20]]
# → [[14, 16]]
```

**Exemple 3**

```python
start_work = 9
end_work = 18
meetings = [[12, 13], [9, 10], [15, 17], [10, 12], [16, 18]]
# → [[13, 15]]
```

### Difficulté supplémentaire

Refaites l'exercice 5 **sans fonction toute faite** pour fusionner les
tableaux : uniquement du tri, des parcours, des conditions et des tableaux —
le format typique d'un exercice d'algorithmique d'examen.
