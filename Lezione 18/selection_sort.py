#algoritmi di ordinamento QUADRATICI - richiedono mediamente un numero di confronti pari al quadrato del numero di elementi (insertion sort, selection sort, bubble sort) - non molto efficienti

#algoritmi di ordinamento OTTIMI (quick sort, merge sort, heap sort) - mediamente richiedono un numero di confronti logaritmico



#SELECTION SORT
#inizia trovando l'elemento minimo dell'insieme, lo metto al primo posto, e continuo fino a terminare gli elementi
#l'algoritmo funziona scambiando l'elemento minimo con un indice che itera (da pos. 0 a pos. n)
#funziona sia in ordine crescente che decrescente
def selection_sort(l):
	
	for pointer in range(len(l)):
		
		min_index = pointer
		for i in range(pointer, len(l)):
			if l[i] < l[min_index]:
				min_index = i
		
		l[pointer], l[min_index] = l[min_index], l[pointer]
					
	#dato l'aliasing la funzione non restituisce niente lavorando direttamente sulla lista				
	return
	
	
l = [1, 3, 2, 7, 0, 8, 10, 6]
selection_sort(l)
print(l)
