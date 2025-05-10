"""si scriva una funzione confronto_indici che riceve una lista L di interi, di lunghezza n, e una lista
P di interi distinti compresi tra 0 e n-1. La funzione restituisce True se e solo se la somma degli elementi
di L il cui indice non compare in P.

Esempio: se L = [1, 7, 5, 2, -3, 4, 0] e P = [1, 2, 4] allora confronto_indici(L, P) restituisce True perché
L[1] + L[2] + L[4] (pari a 9) è maggiore di L[0] + L[3] + L[5] + L[6] (pari a 7)"""



def confronto_indici(l, p):
    somma_i_presenti = 0
    somma_i_non_presenti = 0

    for i in range(len(l)):

        if i in p:
            somma_i_presenti += l[i]
        else:
            somma_i_non_presenti += l[i]
            

    if somma_i_presenti > somma_i_non_presenti:
        return True
    else:
        return False
    


L = [1, 7, 5, 2, -3, 4, 0]
P = [1, 2, 4]

print(confronto_indici(L, P))