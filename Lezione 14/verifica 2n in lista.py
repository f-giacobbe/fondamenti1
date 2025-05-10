#scrivere funzione booleana che dato un valore reale e una lista di valori reali, verifica se il doppio di quel valore
#sia presente in quella lista. True se è presente, False se non è presente

def doppio(n, lista):
	return n*2 in lista
		
print(doppio(5, [1, 3, 10])) #esempio