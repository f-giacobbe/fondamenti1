#riscrivere la funzione len() in maniera ricorsiva
def lunghezza(l):
	res = 0
	
	#caso di uscita - lista vuota
	if l == []:
		res = 0
	else:
		res = 1 + lunghezza(l[1:])
		
	return res

	
	
print(lunghezza([5, 4, 1, 1]))
