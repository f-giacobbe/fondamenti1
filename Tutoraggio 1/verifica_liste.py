#la funzione restituisce True se e solo se la lista l non contiene nessuna sottolista di lunghezza k avente
#valori strettamente crescenti

#es. se l = [4, 5, 5, 6, 1, 1, 2, 2, 5, 3] e k=3 è True perché nessuna sottolista di lunghezza 3 ha valori
#strettamente crescenti



#creo una funzione che mi verifichi se una sottolista rispecchia i requisiti
def sottolista_strettamente_crescente(l):
    for i in range(len(l)-1):
        if l[i+1] <= l[i]:
            return False
        
    return True


def verifica_lista(l, k):

    for i in range(len(l)-k+1): #creo le sottoliste

        #mi viene restituito False alla prima sottolista strettamente crescente
        if sottolista_strettamente_crescente(l[i:i+k]):
            return False
        
    return True


l = [4, 5, 5, 6, 1, 1, 2, 2, 5, 3]
k = 3
print(verifica_lista(l, k))
