L = [4, 3, 5, 2, 4, 6, 9, 9, 6]

def calcola_lista(L, x):
    
    res = []

    for i in range(len(L)-x+1):
        sottolista = []

        #formazione sottolista di lunghezza x
        somma = 0
        j = i
        ok = True

        while ok and (j < i+x):

            if L[j] < x:
                ok = False
            else:
                somma += L[j]
                sottolista.append(L[j])
                j += 1

        #se ok è ancora True
        if ok and (somma%x == 0):
            res.append(sottolista)


    return res


print(calcola_lista(L, 3))