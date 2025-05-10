#data una matrice ordinata di valori interi, scrivere l'algoritmo di ricerca binaria in questa struttura

m = [
	[3, 4, 6, 9, 12, 15],
	[18, 20, 27, 29, 33, 36],
	[45, 46, 47, 52, 54, 59],
	[61, 67, 74, 81, 89, 93],
	[94, 95, 97, 98, 99, 100]
	]

x = 33
	

def ricerca_binaria_matrice(x, m):
	#linearizzare la matrice (fare della matrice un'intera lista)
	n_righe = len(m) #n. righe
	n_colonne = len(m[0]) #n. colonne

	inf = 0
	sup = (len(m)*len(m[0]))-1
	
	trovato = False
	
	while inf <= sup and not trovato:
		med = (inf+sup)//2

		riga = med//n_colonne
		colonna = med%n_colonne

		if m[riga][colonna] == x:
			trovato = True
		elif m[riga][colonna] < x:
			inf = med + 1
		else:	#m[riga][colonna] > x
			sup = med -1

	if trovato:
		return f"l'elemento di valore {x} si trova in riga {riga} e colonna {colonna}"
	else:
		return -100
	
	
print(ricerca_binaria_matrice(x, m))
