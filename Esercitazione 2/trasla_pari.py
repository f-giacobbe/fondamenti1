#funzione che riceve una matrice m (di qualsiasi dimensione nxm) in input, e nelle righe di indice pari gli
#elementi vengono traslati di una posizione a destra (l'ultimo diventa il primo) - funzione NON PURA

m = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]



def trasla_pari(m):
    for i in range(0, len(m), 2):
        temp = m[i][-1]
        
        j = -1
        while j > -len(m[0]):
            m[i][j] = m[i][j-1]
            j -= 1
        m[i][0] = temp

    return



trasla_pari(m)
print(*m, sep="\n")