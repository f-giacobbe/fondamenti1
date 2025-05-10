#esempio di FUNZIONE NON PURA - in quanto modifica anche il valore del parametro attuale
def es(l):
	l[0] = 2
	print(l)
	
m = [1, 2, 3]
es(m)
print(m)


#esempio di FUNZIONE PURA - il parametro attuale non viene modificato
def es_pura(l):
	l_new = l[:]
	l_new[0] = 2
	print(l_new)
	
m2 = [1, 2, 3]
es_pura(m2)
print(m2)
