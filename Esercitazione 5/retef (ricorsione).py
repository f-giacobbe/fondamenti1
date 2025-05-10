""" MATRICE DELLE ADIACENZE (modo per rappresentare un grafo orientato) - rappresentiamo i nodi con gli indici
scrivere una funzione raggiungibile(st1, st2, retef) che date due stazioni (due numeri) fornisca come risultato True se esiste un modo per raggiungere
la seconda stazione a partire dalla prima stazione """

#una riga e una colonna per ogni stazione
#nella casella ij c'è un 1 se tra i e j esiste un collegamento
#diagonale principale uguale a 1, in quanto è sempre possibile andare nella stessa stazione di partenza
retef = [
	[0, 1, 0, 0, 0, 0, 0],#0
	[0, 0, 1, 0, 1, 0, 0],#1
	[1, 0, 0, 0, 0, 0, 0],#2
	[0, 0, 0, 0, 0, 0, 0],#3
	[0, 0, 0, 1, 0, 1, 0],#4
	[0, 0, 0, 0, 1, 0, 1],#5
	[0, 0, 0, 0, 0, 0, 0]#6
	#0	1  2  3  4  5  6
	]
	
	
def direzioni_possibili(st, retef):
	res = []
	for i in range(len(retef)):
		if retef[st][i] == 1:
			res.append(i)
			
	return res

		
	
def raggiungibile(st1, st2, retef):
	res = False
	if st1 == st2 or (st2 in direzioni_possibili(st1, retef)):
		return True
	else:
		for st in direzioni_possibili(st1, retef):
			if raggiungibile(st, st2, retef):
				return True
			
	return False
	
	
	
print(raggiungibile(4, 0, retef))
