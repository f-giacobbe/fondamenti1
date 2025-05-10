#calcolare i fattoriali di n-numeri di una sequenza chiusa da un numero negativo
n = 0
while n >= 0:
	n = int(input("Inserisci un numero: "))
	fattoriale = 1
	counter = 1
	if n < 0:
		print("fine")
	else:
		while counter <= n:
			fattoriale = fattoriale * counter
			counter = counter + 1
		print("il fattoriale è:", fattoriale)
