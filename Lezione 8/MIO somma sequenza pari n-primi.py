#leggere una sequenza di numeri interi in input (terminata dal tappo 0), restituire la somma dei numeri primi della sequenza collocati in posizione pari (primo numero posizione 1)

n = 1
somma = 0

i = 1
while n != 0:
	d = 2
	prime = True
	n = int(input("Digita numero: "))
	
	#guardia posizione pari
	if i%2 == 0:
		
		#guardia n-primo
		while d < n and prime == True:
			if n%d == 0:
				prime = False
			d += 1
		if prime == True:
			somma += n
			
	i += 1
	
print("La somma è", somma)
