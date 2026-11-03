def rotation_90(matrice: list[list[int]]) -> list[list[int]]:
    n = len(matrice)

    for i in range(n):
        for j in range(i + 1, n):
            matrice[i][j], matrice[j][i] = matrice[j][i], matrice[i][j]

    for l in matrice:
        l.reverse()

    return matrice


def rotation_90_second(matrice):
    n = len(matrice)

    new = []

    for _ in range(n):
        new.append([0] * n)

    for i in range(n):
        for j in range(n):
            new[j][n - 1 - i] = matrice[i][j]
    return new


def rotation_90(m):
    return [list(r) for r in zip(*m[::-1])]


print(rotation_90([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(rotation_90_second([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


l_1 = [1, 2, 3]
l_2 = [4, 5, 6]
l_3 = [7, 8, 9]

result = []

for r in zip(l_1, l_2, l_3):
    result.append(list(r)[::-1])

for l in result:
    print(l)
