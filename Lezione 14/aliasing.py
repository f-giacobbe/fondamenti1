x = [2, 3]
y = [2, 3]

print(x[0])
x = y ###
y[0] = 7
print(x[0])

#per capire come vengono gestiti gli indirizzi di memoria da python (aliasing)

#modificando un elemento della lista y, chiedendo una variabile della lista x viene comunque restituito quel valore,
#in quanto la variabile x non fa altro che reindirizzare alla stessa locazione della variabile y
