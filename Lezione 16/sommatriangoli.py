#data una matrice nxn, creare una funzione che esegua la somma degli elementi presenti nei due triangoli verticali
#(comprese le diagonali)		#sostituisco gli elementi con 0 per debug (funziona sia con n pari che dispari)
def sommatriangoli(mx):
	n = len(mx)
	somma = 0
	
	for i in range(n):
		if i < n/2:
			for j in range(i, (n-i)):
				somma += m[i][j]
				m[i][j] = 0
				
		else:
			for j in range((n-i)-1, i+1):
				somma += m[i][j]
				m[i][j] = 0
				
	return somma
	
m = [
    [2, 3, 4, 5, 6, 7],
    [5, 7, 9, 3, 2, 8],
    [2, 2, 1, 2, 2, 9],
    [5, 9, -2, 21, 2, 7],
    [1, 1, 2, 1, 2, 1],
    [5, 7, 9, 3, 2, 8]
]

print(sommatriangoli(m))
print(*m, sep="\n")
