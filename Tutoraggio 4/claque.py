""" considerata una amtrice A di nxm interi, definiamo 'claque' una sottomatrice 2x2 in cui la somma algebrica
dei valori di una diagonale sia pari a quella dell'altra diagonale

si scriva un programma che acquisisce una matrice nxm e stampa il numero di claque della matrice """


def claque(m):
    claques_counter = 0

    for i in range(len(m)-1):
        for j in range(len(m[0])-1):
                #diag. principale       #diag. secondaria
            if m[i][j] + m[i+1][j+1] == m[i+1][j] + m[i][j+1]:
                claques_counter += 1

    return claques_counter



m = [
    [4, -1, 7, 0, 0],
    [-4, -9, -1, 0, 0],
    [2, 8, 16, 1, 4],
    [-1, 7, 5, 2, 5]
]
#questa matrice contiene 5 claques

print(claque(m))