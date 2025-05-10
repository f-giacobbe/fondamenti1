#data una matrice nxn produce una matrice in cui il triangolo formato da tutti i valori dalla diagonale
#secondaria in sù diventano gli elementi della nuova matrice, mentre sotto la diagonale secondaria della
#nuova matrice devono esserci tutti nulli

m = [
	[2, 3, 4, 5, 6],
	[5, 7, 9, 3, 2],
	[2, 2, 1, 2, 2],
	[0, 9, -2, 21, 2],
	[1, 1, 0, 1, 2]
]


def triangolo_sup(m):
	n = len(m)   #definisce nxn

	i = -1

	while i > -n:
		i_i = -n + abs(i)   #sottoindice di ogni riga

		while i_i <= -1:
			m[i][i_i] = 0

			i_i += 1
		
		i -= 1

	return m
	

#or

def triangolo_sup_v2(m):
	n = len(m)   #definisce nxn

	for i in range(n):
		for j in range(n-i, n):		#alla prima attivazione non va out-of-range perché essendo l'intervallo [5, 4] (compresi), il corpo del for non viene eseguito in quanto viene generato un intervallo nullo
			m[i][j] = 0
	
	return m


print(*triangolo_sup(m), sep="\n")
print("")
print(*triangolo_sup_v2(m), sep="\n")

#side effect -> se stampo la matrice iniziale, anch'essa è stata modificata, in quanto python ha lavorato con il suo indirizzo
print("")
print(*m, sep="\n")