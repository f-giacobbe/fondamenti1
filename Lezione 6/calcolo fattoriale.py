#calcolare il fattoriale di un numero (n <= 0)
n = int(input("Fattoriale di: "))
counter = 1
fattoriale = 1

while n < 0:
	n = int(input("Il fattoriale di questo numero è indeterminato in quanto negativo. Digitane un altro: "))

if n != 0:
	while counter <= n:
		fattoriale = fattoriale * counter
		counter = counter + 1
	
print("Il fattoriale di", n, "è", fattoriale)
