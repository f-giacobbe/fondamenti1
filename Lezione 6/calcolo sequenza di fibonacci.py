#utente specifica i; calcolare i-esimo numero della sequenza di fibonacci
import time
i = int(input("Specificare i-esimo numero della sequenza di Fibonacci: "))
i_counter = 1
a = 0
b = 1
c = 0

if i == 0:
	print(1)
else:
	while i_counter <= i:
		c = a+b
		a = b
		b = c
		i_counter += 1
		print(c)
		time.sleep(0.3)
