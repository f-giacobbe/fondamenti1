#metodo APPEND	- aggiunge elementi all'estremità della lista
l = []
l.append(7)
print(l)	#>[7]
l.append(4)
print(l)	#>[7, 4]
l.append(4)	#>[7, 4, 4]


#metodo COUNT	- restituisce il numero di volte in cui l'elemento (4) appare nella lista
print(l.count(4))


#metodo INSERT(posizione, elemento)	- inserisce il valore (9) in posizione (2)	(SENZA SOSTITUZIONE, shiftando)
l.insert(2, 9)
print(l)


#metodo INDEX	- restituisce la posizione dell'elemento indicato. In caso ci fossero più elementi uguali, restituisce
				  #l'indice del primo che trova
print(l.index(4))


#metodo REVERSE		- restituisce la stessa lista, ma invertita
l.reverse()
print(l)


#metodo SORT	- ordina gli elementi della lista in ordine crescente
l.sort()
print(l)


##per i metodi SORT, APPEND, REVERSE, non è possibile fare ciò:
l = l.sort()
print(l)	#>None
#perché questi metodi hanno come uscita None, sicché assegnando a l uno di questi metodi viene ANNULLATA l'intera lista
#bisogna chiamare il metodo senza assegnarlo alla lista stessa, proprio come una funzione


#metodo POP - rimuove un elemento dalla lista e lo assegna a una nuova variabile
lista = ["ciao"]
item = lista.pop(lista.index("ciao"))	#pop prende come parametro esclusivamente l'indice numerico
print(item)
print(lista)
