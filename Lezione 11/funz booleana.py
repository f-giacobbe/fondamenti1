#esempio di funzione che restituiscre valore booleano

def isEven(n):
	pari = 0
	if n%2 == 0:
		pari = True
	else:
		pari = False
	return pari
		
#è più elegante che una funzione abbia un solo return	
	
print(isEven(int(input("Digita: "))))
