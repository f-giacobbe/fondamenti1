#leggere una sequenza di numeri interi in input (terminata dal tappo 0), restituire la somma dei numeri primi della sequenza collocati in posizione pari (primo numero posizione 1)


import math

n = 1
somma = 0
d = 2

i = 1
while n != 0:
	n = int(input("Digita numero: "))
	
	#guardia posizione è pari
	if i%2 == 0:
		
		#guardia n-primo
		while n%d != 0 and d <= math.sqrt(n):
			d += 1
		if n%d != 0 or n == 2:
			somma += n
			
	i += 1
	
print("La somma è", somma)