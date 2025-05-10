
#introduzione LISTE
#un esempio di lista è quella formatasi dalla funzione range()

nomi = ["Aldo", "Anna", "Ugo"]
numeri = [3, 7, 8, 9]

lista_vuota = []

#questi sono esempi di liste omogenee, andiamo adesso a vedere qualche esempio di lista eterogenea:
	
indirizzi = ["Via Roma", 55, "Milano"]

#tra gli elementi di una lista è possibile trovare anche altre liste

CD = [["Bach", "Aria sulla punta corda"], ["RHCP", "Californication"], [3, 4, True], [1, 2, ["a", "b", 7]]]


print(len(CD))	#restituisce la cardinalità della lista (elementi di primo livello di gerarchia)


print(CD[3])	#restituisce l'elemento in pos. 3 della lista CD

print(CD[1][1])	#restituisce l'elemento in pos. 1 della lista in pos. 1 della lista CD

print(CD[1][1][0])	#restituisce "C"



#a differenza delle stringhe, le liste sono MUTEVOLI, ovvero possono essere modificate
M = [[2, 3, 1, 1], [0, 2, 3, 4], [1, 7, 8, 2]]
print(M)

#modificare la lista
M[0][0] = 14
print(M)

M[0] = [3, 8]
print(M)
#in questo caso ho modificato l'intera lista presente all'interno della lista


#è possibile sostituire anche GRUPPI di elementi
l = [1, 2, 3, 4, 5]
l[1:3] = [8, 9]		#da indice 1 a indice 2 compresi
print(l)

l[1:3] = []
print(l)	#gli elementi in posizione 1 e 2 vengono rimossi

l[1:1] = [2, 2, 2]		#INSERISCE gli elementi tra la posizione 1 e la "posizione 0", ovvero la virgola
print(l)



#operatore esplicito di CANCELLAZIONE elemento da lista
del l[2]
print(l)




#in memoria le liste sono gestite diversamente rispetto alle stringhe (essendo mutevoli), per cui notiamo una differenza nel confronto:
x = [1, 2]
y = [1, 2]
print(x == y)	#>True	perché confronta i valori delle listee
#ma
print(x is y)	#>False		perché le liste sono salvate in locazioni di memoria differenti (pur essendo uguali)
