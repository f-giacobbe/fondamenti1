#BUBBLE SORT (base)
#si considerano coppie di elementi, ordinandole attraverso gli scambi e lavorando con un singolo indice
#dopo ogni "bubble pass", l'elemento più grande va in ultima posizione, per cui lavorerò con una porzione sempre
#più piccola di lista (ridotta dell'ultimo elemento)
#l'algoritmo si ferma quando la sottolista diventa di len=1


#BUBBLE SORT (ottimizzato)
#1 forma) utilizzo una variabile scambio (booleana) inizializzata a true. Se durante una passata di bubble non eseguo alcuno 
#scambio, vorrà dire che la lista è già ordinata e interromperò l'algoritmo

#2 forma) inoltre, posso ottimizzare riducendo la lista da tutto il pezzo già ordinato, invece che di un indice alla volta
#(quindi, fino all'ultima posizione in cui è avvenuto uno scambio) - NON UTILIZZA VARIABILE BOOLEANA

l = [5, 1, 3, 7, 2, 9, 4]

def bubble_sort_base(l_old):
	l = l_old[:]	#lavoro sul clone
	
	i_max = len(l)-1
	while i_max > 1:
		for i in range(i_max):
			if l[i] > l[i+1]:
				l[i], l[i+1] = l[i+1], l[i]
				
		i_max -= 1
		
	return l
	
	
print(bubble_sort_base(l))


def bubble_sort_ottimizzato1(l_old):
	l = l_old[:]
	
	scambio = True
	i_max = len(l)-1
	while i_max > 1 and scambio:
		scambio = False
		for i in range(i_max):
			if l[i] > l[i+1]:
				l[i], l[i+1] = l[i+1], l[i]
				scambio = True
				
		i_max -= 1
		
	return l
	
print(bubble_sort_ottimizzato1(l))