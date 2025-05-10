#stesso esercizio, senza però toccare la matrice di partenza (creando una copia di m)
m = [
    [2, 3, 4, 5, 6],
    [5, 7, 9, 3, 2],
    [2, 2, 1, 2, 2],
    [0, 9, -2, 21, 2],
    [1, 1, 0, 1, 2]
]


#import copy		-> si può fare direttamente così

def triangolo_sup(m_old):
	#m_new = copy.deepcopy(m_old)
	m_new = []
	for i in range(len(m_old)):		#qui lo faccio manualmente senza funzione deepcopy
		m_new.append([])

		for item in m_old[i]:
			m_new[i].append(item)

	
		
	n = len(m_new)
	
	for i in range(n):
		for j in range(n-i, n):
			m_new[i][j] = 0
			
	return m_new


print(*triangolo_sup(m), sep="\n")
print("")
print(*m, sep="\n")
