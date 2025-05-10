# input = sequenza di numeri fino a input=0; calcolare il massimo
a = int(input("Scrivi il primo numero: "))
massimo = a

while a != 0:
	if a > massimo:
		massimo = a
	a = int(input("Scrivi un altro numero"))

print("Il numero più grande è", massimo)
