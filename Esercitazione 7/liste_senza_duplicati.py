""" si scriva una funzione f che riceve in ingresso due liste L1 ed L2 di stringhe e restituisce una lista che contiene
gli elementi di L1 ed L2 in ordine crescente, senza elementi duplicati. La funzione non deve utilizzare la funzione
sort della libreria standard. """


L1 = ["albero", "mare", "zebra", "casa"]
L2 = ["abaco", "albero", "barca", "casa", "mare", "verde", "zebra"]



def bubble_sort(l):
	#ordina direttamente la lista di riferimento (funzione non pura)
	scambio = True
	i_max = len(l)-1
	while scambio and i_max > 1:
		scambio = False
		
		for i in range(i_max):
			if l[i] > l[i+1]:
				l[i], l[i+1] = l[i+1], l[i]
				scambio = True
				
		i_max -= 1
		
	return
	


def f(L1, L2):
	l_new = []
	for elemento in L1:
		if elemento not in l_new:
			l_new.append(elemento)
	for elemento in L2:
		if elemento not in l_new:
			l_new.append(elemento)
			
	bubble_sort(l_new)
	return l_new
	
	
print(f(L1, L2))
