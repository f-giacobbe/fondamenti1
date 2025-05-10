#nel caso di una ricerca ordinata è meglio utilizzare quest'altro tipo di ricerca, detta RICERCA BINARIA

l_ordinata = [1, 3, 6, 9, 11, 15, 18]
x = 3

#considero l'elemento mediano della lista (in questo caso l'elemento di valore 6), e confronto x con questo elemento
#considero tre casi: ==, <, >

#in questo caso siccome 3 < 6, escludo la seconda metà della lista, continuando con questo algoritmo nella prima metà della lista finché non trovo x

#vengono richiesti 3 variabili: inf, sup, med((inf+sup//2))

	#se x == l[med] -> med
	#se x > l[med] -> inf = med+1
	#se x < l[med] -> sup = med-1
	
#nel momento in cui sup diventa strettamente più piccolo di inf, ci possiamo fermare perché vorrà dire che x non è presente

def ricerca_binaria(x, l):
	inf = 0
	sup = len(l)-1
	
	trovato = False
	
	while inf <= sup and not trovato:
		med = (inf+sup)//2
		
		if x == l[med]:
			trovato = True
		elif x > l[med]:
			inf = med+1
		else:	#x < l[med]
			sup = med-1
			
	if trovato:
		return med
	else:
		return -100
		
		
		
print(ricerca_binaria(11, l_ordinata))


#a livello di efficienza, nel caso peggiore questo algoritmo risulta essere più efficiente rispetto alla sua controparte lineare, con un massimo di log in base 2 di n

#pertanto, se abbiamo una lista GIÀ ordinata, conviene utilizzare questo algoritmo, altrimenti ne utilizziamo un altro, in quanto
#ordinare una lista disordinata costa molte risorse; a meno che non dobbiamo fare tante ricerche binarie
