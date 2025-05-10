#mediamente gli algoritmi iterativi sono più efficienti della loro controparte ricorsiva


#posso definire ricorsivamente il calcolo del fattoriale come (n*fattoriale(n-1))
def fattoriale(n):
	res = 0
	
	if n == 0:	#caso di uscita
		res = 1
	else:
		res = n * fattoriale(n-1)	#ricorsione
		
	return res

		
print(fattoriale(4))



#calcolo fibonacci
def fibonacci(n):
	if n == 0 or n == 1:
		fib = 1
	else:
		fib = fibonacci(n-1) + fibonacci(n-2)
		
	return fib
	

print(fibonacci(9))



#torri di Hanoi	-	output stringhe con mosse (sposta da x a x)
def hanoi(n, x, y, z):
	"""
	sposta n dischi da A a B utilizzando C (xyz)
	"""
	#uscita banale
	if n == 1:
		print(f"sposta da {x} a {y}")
	else:
		hanoi(n-1, x, z, y)
		print(f"sposta da {x} a {y}")
		hanoi(n-1, z, y, x)
		
	return
	
hanoi(3, "A", "B", "C")
