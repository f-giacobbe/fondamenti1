#da un n intero qualsiasi, se n è pari lo si divide per 2, altrimenti lo moltiplico per 3 e aggiungo 1. La sequenza termina quando raggiunge 1

import time

def isEven(n):	#(non necessaria)
	pari = 0
	if n%2 == 0:
		pari = True
	else:
		pari = False
	return pari
	
def sequenza(n):
	print(n)
	while n != 1:
		if isEven(n):
			n = n//2
		else:
			n = (n*3)+1
		
		time.sleep(0.3)		
		print(n)
		

sequenza(int(input("Digita il numero da cui iniziare: ")))
