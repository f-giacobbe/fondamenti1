"""
si scriva una funzione calcola_elementi_comuni che riceve in ingresso una lista L in cui ogni elemento
è una lista di numeri interi distinti, ordinata in modo crescente. La funzione restituisce una lista contenente
i numeri comuni a tutte le liste presenti in L

es. se L = [[4, 9, 15, 22], [3, 4, 9, 15, 18, 22, 27, 55], [4, 9, 10, 15, 18, 22], [4, 9, 15, 19, 22],
[4, 5, 6, 9, 15, 16]]

la funzione restituisce la lista [4, 9, 15]
"""

def calcola_elementi_comuni(L):
    l_res = []
    
    for e in L[0]:

        presente_in_tutte_le_liste = True
        i = 1
        while (i < len(L)) and presente_in_tutte_le_liste:
            if e not in L[i]:
                presente_in_tutte_le_liste = False

            i += 1

        if presente_in_tutte_le_liste:
            l_res.append(e)

    return l_res


L = [[4, 9, 15, 22], [3, 4, 9, 15, 18, 22, 27, 55], [4, 9, 10, 15, 18, 22], [4, 9, 15, 19, 22],
[4, 5, 6, 9, 15, 16]]

print(calcola_elementi_comuni(L))