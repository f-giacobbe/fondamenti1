""" si vuole sviluppare una funzione che data in input una matrice quadrata e degli indici, aggiunge un elemento
allo stesso solo se le celle adiacenti (area 3x3) sono libere (0) """



#funzione sbagliatissima fatta dal tutor
def aggiungi_pedone(m, riga, colonna):

    #verifico se la matrice è quadrata
    if len(m) != len(m[0]):
        return False
    

    #check celle adiacenti (0 indica cella vuota / 1 indica cella occupata)
        #primo caso: gli indici indicano una cella interna alla matrice (8 intorni)
    if (0 < riga < len(m)-1) and (0 < colonna < len(m)-1):
            #controllo celle sopra
        for j in range(colonna-1, colonna+2):
            if m[riga-1][j] == 1:
                return False
            #controllo celle sotto
        for j in range(colonna-1, colonna+2):
            if m[riga+1][j] == 1:
                return False
            #controllo riga corrente
        for j in range(colonna-1, colonna+2):
            if m[riga][j] == 1:
                return False
            
        m[riga][colonna] = 1
        return True
            

        #secondo caso: vertice alto sx
    elif (riga == 0) and (colonna == 0):
            #elemento a destra
        if m[riga][colonna+1] == 1:
            return False
            #elemento in basso e in basso a destra
        elif (m[riga+1][colonna] == 1) or (m[riga+1][colonna+1] == 1):
            return False
        
        m[riga][colonna] = 1
        return True


        #terzo caso: vertice alto dx
    elif (riga == 0) and (colonna == len(m)-1):
            #elemento a sinistra
        if m[riga][colonna-1] == 1:
            return False
            #elemento sotto e in basso a sinistra
        elif (m[riga+1][colonna] == 1) or (m[riga+1][colonna-1] == 1):
            return False
        
        m[riga][colonna] = 1
        return True


        #quarto caso: vertice basso sx
    elif (riga == len(m)-1) and (colonna == 0):
            #elemento a destra
        if m[riga][colonna+1] == 1:
            return False
            #elementi superiori
        elif (m[riga-1][colonna] == 1) or (m[riga-1][colonna+1] == 1):
            return False
        
        m[riga][colonna] = 1
        return True


        #quinto caso: vertice basso dx
    elif (riga == len(m)-1) and (colonna == len(m)-1):
            #elemento a sinistra
        if m[riga][colonna-1] == 1:
            return False
            #elementi superiori
        elif (m[riga-1][colonna] == 1) or (m[riga-1][colonna-1] == 1):
            return False
        
        m[riga][colonna] = 1
        return True


        #sesto caso: bordo superiore
    elif (riga == 0) and (0 < colonna < len(m)-1):
            #elementi di sotto
        for j in range(colonna-1, colonna+2):
            if m[riga+1][j] == 1:
                return False
            #elementi riga corrente
        for j in range(colonna-1, colonna+2):
            if m[riga][j] == 1:
                return False
            
        m[riga][colonna] = 1
        return True


        #settimo caso: bordo inferiore
    elif (riga == len(m)-1) and (0 < colonna < len(m)-1):
            #riga superiore
        for j in range(colonna-1, colonna+2):
            if m[riga-1][j] == 1:
                return False
            #riga corrente
        for j in range(colonna-1, colonna+2):
            if m[riga][j] == 1:
                return False
            
        m[riga][colonna] = 1
        return True


        #ottavo caso: bordo laterale sx
    elif (0 < riga < len(m)-1) and (colonna == 0):
            #colonna a destra
        for i in range(riga-1, riga+2):
            if m[i][colonna+1] == 1:
                return False
            #colonna corrente
        for i in range(riga-1, riga+2):
            if m[i][colonna] == 1:
                return False
            
        m[riga][colonna] = 1
        return True


        #nono caso: bordo laterale dx
    elif (0 < riga < len(m)-1) and (colonna == len(m)-1):
            #colonna a sinistra
        for i in range(riga-1, riga+2):
            if m[i][colonna-1] == 1:
                return False
            #colonna corrente
        for i in range(riga-1, riga+2):
            if m[i][colonna] == 1:
                return False
            
        m[riga][colonna] = 1
        return True
    


def massimo(l):
	res = l[0]
	for e in l:
		if e > res:
			res = e
			
	return res
	
def minimo(l):
	res = l[0]
	for e in l:
		if e < res:
			res = e
			
	return res
	
	

#funzione molto più compatta
def a2(m, riga, colonna):
	for i in range(massimo([0, riga-1]), minimo([len(m), riga+2])):
		for j in range(massimo([0, colonna-1]), minimo([len(m), colonna+2])):
			if m[i][j] == 1:
				return False
	
	m[riga][colonna] = 1
	return True



m = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

#print(aggiungi_pedone(m, 4, 2))
print(a2(m, 4, 2))
print(*m, sep="\n")
