""" si vuole realizzare un'applicazione per la gestione delle notifiche di possibile contagio durante una 
pandemia. L'applicazione gestisce i possibili contagi in un ambiente di lavoro open-space; le postazioni in tale
ambiente sono organizzate in una griglia, rappresentata da una matrice posti il cui generico elemento posti[i][j]
contiene la matricola del dipendente che lavora abitualmente il posizione (i,j) all'interno della stanza, oppure
-1 se la postazione è vuota. 
I dati relativi ai dipendenti sono memorizzati in una lista MATRICOLE e le info dei dipendenti in una matrice
INFO_DIPENDENTI con forma [nome, cognome, città, positivo].

Si scrivano le seguenti funzioni:
	1) potenziale_infettto(posti, i, j, matricole, info_dipedenti, k) - che restituisce True se e solo se al posto
	delle coordinate (i,j) c'è un dipendente che si trova a distanza minore o uguale a k da almeno un positivo, cioè
	se all'interno della sottomatrice con estremi (i-k, j-k) e (i+k, j+k) c'è almeno un collega positivo. Il parametro
	k è un numero naturale che chiamiamo indice di contagiosità; più è alto il valore di tale parametro, maggiore
	sarà la capacità del virus di contagiare persone distanti tra loro
	
	2) dipendenti_potenziali_infetti(posti, matricole, info_dipendenti, k), che restituisce una lista contenente le
	matricole dei dipendenti che possono essere infettati, se l'indice di contagiosità è k. La lista non deve contenere
	i dipendenti che sappiamo già essere positivi.
	
	3) infetti_città (posti, matricole, info_dipendenti, k), che restituisce una lista contenente, per ogni città, il
	numero di positivi o potenziali infetti, se l'indice di contagiosità è k
	
	4) contagiosita_critica(posti, matricole, info_dipendenti), che restituisce il più piccolo indice di contagiosità
	tale che in ogni città vi sia almeno un positivo o un potenziale infetto """
	
	
	
matricole = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "L", "M", "N"]
info_dipendenti = [
	["marco", "rossi", "rende", True],
	["carlo", "verdi", "rende", False],
	["gino", "neri", "cosenza", False],
	["franco", "bianchi", "cosenza", True],
	["diego", "viola", "rossano", False],
	["nino", "russo", "rossano", False],
	["peppe", "bruno", "reggio", False],
	["mario", "chiari", "reggio", False],
	["ciro", "ferrara", "napoli", False],
	["rino", "scacchi", "napoli", False],
	["ugo", "fantozzi", "roma", False],
	["andrea", "piaggio", "roma", True]
	]
posti = [
	["A", "B", "C"],
	["D", "E", "F"],
	["G", "H", "I"],
	["L", "M", "N"]
	]
	

	
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
	
	
	
def potenziale_infetto(posti, i, j, matricole, info_dipendenti, k):
	
					#limite inferiore e superiore
	for i1 in range(massimo([i-k, 0]), minimo([i+k+1, len(posti)])):
		
		for j1 in range(massimo([j-k, 0]), minimo([j+k+1, len(posti[0])])):
			
			#verifico che il dipendente preso non è il dipendente stesso
			if not (i1 == i and j1 == j):
				dipendente_matricola = posti[i1][j1]
				dipendente_indice = matricole.index(dipendente_matricola)
				
				if info_dipendenti[dipendente_indice][3]:
					return True
				
	return False
	



def dipendenti_potenziali_infetti(posti, matricole, info_dipendenti, k):
	
	res = []
	
	for i in range(len(posti)):
		for j in range(len(posti[0])):
			
			matricola_indice = matricole.index(posti[i][j])
			#se non sono già positivi
			if not info_dipendenti[matricola_indice][3]:
				
				if potenziale_infetto(posti, i, j, matricole, info_dipendenti, k):
					res.append(posti[i][j])
					
	return res
	


def infetti_citta(posti, matricole, info_dipendenti, k):
	res = []
	lista_citta_uniche = []

	#inserisco città
	for i in range(len(info_dipendenti)):
		if info_dipendenti[i][2] not in lista_citta_uniche:
			lista_citta_uniche.append(info_dipendenti[i][2])

	for i in range(len(lista_citta_uniche)):
		res.append([])
		res[i].append(lista_citta_uniche[i])

	
	#conto numero di positivi o potenziali infetti per ogni città
	for i in range(len(lista_citta_uniche)):
		count = 0

		for j in range(len(info_dipendenti)):

			if info_dipendenti[j][2] == lista_citta_uniche[i]:

				#se è positivo
				if info_dipendenti[j][3]:
					count += 1

				#se è potenziale infetto
				elif matricole[j] in dipendenti_potenziali_infetti(posti, matricole, info_dipendenti, k):
					count += 1

		res[i].append(count)

	return res



def contagiosita_critica(posti, matricole, info_dipendenti):
	#partiamo da k=0
	k = 0

	ok = False
	while not ok:
		ok = True

		lista_citta = infetti_citta(posti, matricole, info_dipendenti, k)

		for i in range(len(lista_citta)):

			#se esiste ancora una città con 0 pericoli
			if lista_citta[i][1] == 0:
				ok = False

		if ok:
			return k
		else:
			k += 1
