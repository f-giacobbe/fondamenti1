l_disordinata = ["F", 1, 2, 8, 4, 5]
x = 8

#voglio stabilire se x è presente o meno all'interno della lista

#se la lista NON è ordinata, utilizzo la RICERCA LINEARE, confrontando ogni elemento della lista finché non troviamo il target
def ricerca_lineare(x, l):
	trovato = False
	i = 0
	while i < len(l) and not trovato:
		if l[i] == x:
			trovato = True
		else:
			i += 1
	
	if trovato:
		return i
	else:
		return -100
		

print(ricerca_lineare(x, l_disordinata))


#questo algoritmo richiede in media n/2 operazioni, e al massimo n operazioni (in base alla posizione di n nella lista)
