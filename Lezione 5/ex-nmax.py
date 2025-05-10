#leggere tre numeri e calcolarne il massimo
a = int(input("Scrivi il primo numero: "))
b = int(input("Scrivi il secondo numero: "))
c = int(input("Scrivi il terzo numero: "))

massimo = 0

#SBAGLIATO
#if a > b:
#	massimo = a
#else:
#	massimo = b
#if c > massimo:
#	massimo = c

if a >= b and a >= c:
	massimo = a
elif b >= a and b >= c:
	massimo = b
else:
	massimo = c
			
print("Il numero più grande è", massimo)
