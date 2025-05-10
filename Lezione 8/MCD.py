#utente fornisce due numeri interi, calcolare MCD
a = int(input("Inserisci il primo numero: "))
b = int(input("Inserisci il secondo numero: "))

maxx = 0
#determinare numero più grande
if a >= b:
	minn = b
else:
	minn = a
	

resto_a = 1
resto_b = 1
while resto_a != 0 and resto_b != 0:
	resto_a = a%minn
	resto_b = b%minn
	
	maxx -= 1
	
print(minn)



#SOLUZIONE --> con m>n, vale MCD(m-n, n)					con m<n, vale MCD(n-m, m)			
while m != n:
	if m > n:
		m = m-n
	else:
		n = n-m
		
print("L'MDC è'", m)
