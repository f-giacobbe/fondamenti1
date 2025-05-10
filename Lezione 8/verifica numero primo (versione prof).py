#SOLUZIONE EFFICIENTE --> fermarsi a radice di n.
#		se n non primo allora esiste un divisore di n (n%d==0), d!=1 and d != n, ovvero n==d*quoziente
#		non può essere contemporaneamente vero che d>sqrt(n) e che quoziente > sqrt(n)
#		ovvero d o quoziente sono <= sqrt(n)

import math
n = (int(input("Digita numero: ")))
d = 2 #primo potenziale divisore

while n%d != 0 and d <= math.sqrt(n):
	d += 1
	
if n%d == 0 and n != 2:		#fix "and n != 2"
	print("Non primo")
else:
	print("Primo")
