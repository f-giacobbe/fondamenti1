"""si scriva una funzione verifica_liste che riceve due liste L1 ed L2 di interi e un intero k e restituisce
True se e solo se L1 contiene una sottolista di lunghezza k i cui elementi sono presenti in L2 nello
stesso ordine (anche se in posizioni non consecutive)

esempio: se L1 = [3, 1, 2, 5, 7, 3, 5, 3], L2 = [8, 1, 7, 4, 2, 6, 3, 5, 4] e k = 3, allora la funzione
restituisce True perché la lista L1 contiene [1, 2, 5] i cui elementi sono presenti in L2 nello stesso ordine
"""


def sottolista_trovata(l_target, l2):
    """
    verifica se gli elementi di l_target sono presenti in l2 (nello stesso ordine anche non consecutivo)
    """

    #scorriamo la lista un'unica volta
    j = 0
    for elem in l_target:
        #variabile flag
        trovato = False

        while not trovato and j < len(l2):

            if elem == l2[j]:
                trovato = True

            j += 1

        #se anche un solo elemento di l_target non è presente, restituiamo direttamente False
        if not trovato:
            return False
        
    return True



def verifica_liste(l1, l2, k):
    
    for i in range(len(l1)-k+1):
        if sottolista_trovata(l1[i:i+k], l2):
            return True
        
    return False



L1 = [3, 1, 2, 5, 7, 3, 5, 3]
L2 = [8, 1, 7, 4, 2, 6, 3, 5, 4]
k = 3

print(verifica_liste(L1, L2, k))