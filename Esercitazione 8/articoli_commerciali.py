"""
si vuole realizzare un'applicazione per la gestione delle informazioni riguardanti acquisti di componenti per la
produzione di articoli commerciali. L'applicazione memorizza i dati relativi alla composizione degli articoli in 
una matrice AC in cui ad ogni articolo è associata la lista dei componenti necessari per la produzione 
dell'articolo stesso. Le offerte effettuate dai fornitori dei componenti sono memorizzate in una matrice 
O avente 3 colonne, in cui la generica riga [comp, forn, pr] rappresenta il fatto che il componente comp 
è offerto dal fornitore forn al prezzo pr. Si assuma che non esistono due righe aventi uguali valori di 
comp e forn - in altri termini, ogni fornitore non può effettuare più offerte per uno stesso componente.
La spesa di fornitura per un articolo è la somma dei prezzi che è necessario spendere per i componenti 
dell'articolo - ovviamente, se più di un fornitore fornisce uno stesso componente, si considera l'offerta 
con prezzo minore. Un componente è detto "speciale" quando è necessario alla produzione di un solo articolo.

Scrivere le seguenti funzioni:
	
	1) articolo_minima_spesa(AC, O), che restituisce l'articolo avente minima spesa di fornitura. 
	Nel caso in cui più
	di un articolo soddisfi la condizione, la funzione ne restituisce uno qualsiasi.
	
	2) miglior_fornitore(AC, O), che restituisce il fornitore che soddisfa entrambe le condizioni:
		a) il fornitore fornisce tutti i componenti necessari alla produzione di tutti gli articoli;
		b) la somma dei prezzi richiesti dal fornitore è minima
		
		Nel caso in cui più di un fornitore soddisfi le condizioni, la funzione ne restituisce uno qualsiasi. 
		Nel caso in cui nessun fornitore soddisfi le condizioni, la funzione restituisce una stringa vuota.
		
	3) componenti_speciali(AC) che restituisce la lista di tutti i componenti speciali
	
	4) componente_comune(O), che restituisce il componente disponibile presso il maggior numero di fornitori,
	cioè il componente per cui sono state effettuate il maggior numero di offerte. Nel caso in cui più di un
	componente soddisfi la condizione, la funzione ne restituisce uno qualsiasi
"""

AC = [
	["Art1", "Art2", "Art3", "Art4"],
	[["Comp1", "Comp2"],
	["Comp2", "Comp3"],
	["Comp4", "Comp5"],
	["Comp4", "Comp5"]]
	]
	
O = [
	["Comp1", "Forn1", 100],
	["Comp1", "Forn2", 70],
	["Comp2", "Forn1", 120],
	["Comp2", "Forn2", 100],
	["Comp2", "Forn3", 70],
	["Comp3", "Forn1", 90],
	["Comp3", "Forn2", 90],
	["Comp3", "Forn3", 80],
	["Comp4", "Forn1", 70],
	["Comp4", "Forn2", 70],
	["Comp5", "Forn1", 90],
	["Comp5", "Forn2", 100]
	]
	


def spesa_min_forn_art(AC, O, art):
	spesa = 0
	
	art_i = AC[0].index(art)
	
	for comp in AC[1][art_i]:

		#inizializzazione minimo
		for i in range(len(O)):
			if O[i][0] == comp:
				min_comp = O[i][2]
		

		for i in range(len(O)):
			if (O[i][0] == comp) and (O[i][2] < min_comp):
				min_comp = O[i][2]
					
		spesa += min_comp
		
	return spesa


	
def articolo_minima_spesa(AC, O):

	#inizializzo il minimo prendendo il primo art. come riferimento
	min_spesa = spesa_min_forn_art(AC, O, AC[0][0])
	art_min = AC[0][0]
	
	for art in AC[0][1:]:	#itero dal secondo elemento in lista (avendo già inizializzato con il primo)
		spesa_art = spesa_min_forn_art(AC, O, art)
		if spesa_art < min_spesa:
			min_spesa = spesa_art
			art_min = art
			
	return art_min
	


def fornisce_tutto(AC, O, forn):

	lista_tutti_componenti = []
	#costruisco la lista di tutti i componenti
	for i in range(len(O)):
		if O[i][0] not in lista_tutti_componenti:
			lista_tutti_componenti.append(O[i][0])


	lista_componenti_forn = []
	#costruisco una lista contenente tutti i componenti venduti da forn
	for i in range(len(O)):
		if (O[i][1] == forn) and (O[i][0] not in lista_componenti_forn):
			lista_componenti_forn.append(O[i][0])


	#verifica
	for comp in lista_tutti_componenti:
		if comp not in lista_componenti_forn:
			return False
		
	return True



def prezzo_forn(AC, O, forn):
	totale = 0

	for i in range(len(O)):
		if O[i][1] == forn:
			totale += O[i][2]

	return totale



def miglior_fornitore(AC, O):

	fornitori = []
	#costruisco una lista contenente tutti i fornitori
	for i in range(len(O)):
		if O[i][1] not in fornitori:
			fornitori.append(O[i][1])


	#rimuovo dalla lista i fornitori che non soddisfano il primo requisito
	for i in range(len(fornitori)):
		if not fornisce_tutto(AC, O, fornitori[i]):
			del fornitori[i]


	#mi trovo il fornitore che ha i prezzi più bassi
	prezzo_min = prezzo_forn(AC, O, fornitori[0])	#inizializzo il minimo col i prezzi del primo fornitore
	forn_min = fornitori[0]

	for fornitore in fornitori[1:]:
		prezzo_forn_var = prezzo_forn(AC, O, fornitore)

		if prezzo_forn_var < prezzo_min:
			prezzo_min = prezzo_forn_var
			forn_min = fornitore

	return forn_min



def occorrenze_comp(AC, comp):
	"""conta in quanti articoli serve un componente"""
	n_articoli = 0

	for i in range(len(AC[0])):
		if comp in AC[1][i]:
			n_articoli += 1

	return n_articoli



def componenti_speciali(AC):
	lista_componenti_speciali = []
	
	lista_tutti_componenti = []
	#costruisco la lista di tutti i componenti
	for i in range(len(O)):
		if O[i][0] not in lista_tutti_componenti:
			lista_tutti_componenti.append(O[i][0])


	#costruisco la lista dei componenti speciali
	for comp in lista_tutti_componenti:
		if occorrenze_comp(AC, comp) == 1:
			lista_componenti_speciali.append(comp)

	return lista_componenti_speciali



def componente_comune(O):
	componente = ""

	lista_tutti_componenti = []
	#costruisco la lista di tutti i componenti
	for i in range(len(O)):
		if O[i][0] not in lista_tutti_componenti:
			lista_tutti_componenti.append(O[i][0])

	
	n_offerte_globale = 0
	for comp in lista_tutti_componenti:
		n_offerte_locale = 0
		for i in range(len(O)):
			if O[i][0] == comp:
				n_offerte_locale += 1

		if n_offerte_locale > n_offerte_globale:
			n_offerte_globale = n_offerte_locale
			componente = comp

	return componente
