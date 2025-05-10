#leggere sequenza n positivi chiusa da n negativo. Output -> n volte in cui un numero è più grande del precedente nella sequenza
n = int(input("Digita un numero (la sequenza termina al primo numero negativo): "))
counter = 0
m = n

while n >= 0:
	n = int(input("Digita un numero: "))
	if n > m:
		counter = counter + 1
	m = n
	
print(counter)
