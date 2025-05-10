#INSERTION SORT
l_0 = [1, 3, 8, 11, 15]


#definizione "passo di insertion"
#se volessi inserire, ad esempio, l'elemento 9 all'interno del vettore, lo confronto con gli elementi finché non trovo
#un elemento più piccolo di esso. Al ché lo inserirò tra il numero subito più piccolo e quello subito più grande

#è necessario partire da un vettore ordinato, per fare ciò individuiamo un sottovettore già ordinato (composto dal solo primo elemento)
#al primo passo, eseguo l'insertion aggiungendo il primo elemento fuori dal sottovettore e continuo aumentando
#la dimensione del sottovettore ordinato

#utlizzato nei casi in cui l'input arriva ordinato o quasi


l1 = [5, 2, 1, 7, 3, 8, 11, 9]


#MIO
def insertion(e, pos, l):
    l.append(0)
    
    i = -2
    while i >= -(len(l)-pos):
        l[i+1] = l[i]
        i -= 1

    l[pos] = e

    return



def insertion_sort(l0):
    l = l0[:1]
    
    for i in range(1, len(l0)):

        j = 0
        stop = False
        while j < len(l) and not stop:

            if l0[i] > l[j]:
                j += 1
            else:
                stop = True


        insertion(l0[i], j, l)


    return l



print(insertion_sort(l1))




#GIUSTO
def insertion_sort_v2(l_old):
	l = l_old[:]
	
	for j in range(1, len(l)):
		x = l[j]
		
		i = j-1
		while (i >= 0) and (l[i] > x):
			l[i+1] = l[i]
			i -= 1
			
		l[i+1] = x
		
	return l
	
	
print(insertion_sort_v2(l1))
