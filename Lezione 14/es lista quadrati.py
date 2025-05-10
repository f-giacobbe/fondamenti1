#leggere una sequenza di numeri interi chiusa dal numero 0, questi numeri andranno caricati su una lista di interi.
#Produrre in uscita la lista dei quadrati di questi numeri

l1 = []
l2 = []
n = 1

while n!=0:
	n = int(input("Digita numero: "))
	if n != 0:
		l1.append(n)
	
for i in l1:
	l2.append(i**2)
	
print(l2)
