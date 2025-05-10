#leggere una sequenza di numeri interi in input (terminata dal tappo 0), restituire la somma dei numeri primi della sequenza collocati in posizione pari (primo numero posizione 1)

def primecalculator(n):
    prime = True
    i = 2
    while i < n and prime == True:
        if n%i == 0:
            prime = False
        i += 1

    if prime == False:
        return False
    else:
        return True

n = 1
somma = 0

i = 1
while n != 0:
	d = 2
	n = int(input("Digita numero: "))
	
	#guardia posizione pari
	if i%2 == 0:
		
		#guardia n-primo
		if primecalculator(n) == True:
        	
			somma += n
			
	i += 1
	
print("La somma è", somma)
