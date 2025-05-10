"""
Si scriva una funzione verifica_lista che ricve in ingresso una lista L di interi ed un intero k. La funzione
restituisce True se e solo se la lista L non contiene nessuna sottolista di lunghezza k avente valori 
strettamente crescenti.

Esempio: Se L = [4, 5, 5, 6, 1, 1, 2, 2, 5, 3], allora verifica_lista(L, 3) restituisce True perché nessuna 
delle sottoliste di lunghezza 3 ([4, 5, 5], [5, 5, 6], [5, 6, 1], [6, 1, 1], ...) ha valori strettamente 
crescenti
"""


def strettamente_crescente(l):
	for i in range(len(l)-1):
		if l[i] >= l[i+1]:
			return False
			
	return True


def verifica_lista(L, k):
	
	for i in range(len(L)-k+1):
		sottolista = L[i:i+k]
		if strettamente_crescente(sottolista):
			return False
			
	return True
	
	
L = [4, 5, 5, 6, 1, 1, 2, 2, 5, 3]

print(verifica_lista(L, 3))
