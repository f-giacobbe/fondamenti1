#esempio di funzione chiamata all'interno di un'altra funzione. Essenziale nella suddivisione di problemi in "sottoproblemi"
def fatt(n):
	f = 1
	if n == 0 or n == 1:
		f = 1
	else:
		for i in range(1, n+1):
			f = f*i
	return f
	
def binomio(n, k):
	return fatt(n)//(fatt(k)*fatt(n-k))
	
n = int(input("Digita n: "))
k = int(input("Digita k: "))

if n <= 0 or k <= 0 or n < k:
	print("Input inappropriato")
else:
	print("Il binomio vale:", binomio(n, k))
