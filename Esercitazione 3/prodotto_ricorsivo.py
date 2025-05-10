#scrivere una funzione prodotto_ricorsivo(x, y), utilizzando soltanto le somme

#x, y >= 0
def prodotto_ricorsivo(x, y):
	if y == 0 or x == 0:
		return 0
	elif y == 1:
		return x
	elif x == 1:
		return y
	else:
		return x + prodotto_ricorsivo(x, y-1)
		
		
print(prodotto_ricorsivo(3, 4))
