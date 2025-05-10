#utente fornisce due numeri interi, calcolare MCD
m = int(input("Inserisci il primo numero: "))
n = int(input("Inserisci il secondo numero: "))


#SOLUZIONE --> con m>n, vale MCD(m-n, n)
while m != n:
	if m > n:
		m = m-n
	else:
		n = n-m
		
print("L'MDC è'", m)
