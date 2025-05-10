def doppiovettori(vec1, vec2):
	"""
	funzione che dati due vettori di n reali restituisce True se per ogni elemento del primo vettore
	il suo doppio appartiene al secondo vettore
	"""
	is_doppio = True
	for v1 in vec1:
		if v1*2 not in vec2:
			is_doppio = False
			break

	return is_doppio
	

print(doppiovettori([1, 2, 3], [2, 4, 6]))



#volendo creare una sottofunzione che verifica se il singolo x appartiene a una lista (senza usare "in")
def appartiene(x, lista):
	trovato = False
	i = 0
	while i < len(lista) and not trovato:
		if lista[i] == x*2:
			trovato = True
		else:
			i += 1

	return trovato


def doppioliste(l1, l2):
	is_doppio = True
	i = 0
	while i < len(l1) and is_doppio:
		if not appartiene(l1[i], l2):
			is_doppio = False
		else:
			i += 1
	
	return is_doppio