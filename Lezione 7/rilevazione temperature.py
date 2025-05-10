#stazione metereologica rileva temperature. user specifica nt -> numero di rilevazioni di temperatura di suo interesse			input sogliaMax = soglia di allarme superiore			input sogliaMin = soglia di allarme inferiore				ultimo input -> valori (in numero di nt) di temperatura
#OUTPUT
		#a) la media delle temperature
		#b) la temperatura minima e massima
		#c) il numero di violazioni della soglia massima
		#d) il numero di violazioni della soglia minima

				
#input utente		
nt = int(input("Specifica il numero di rilevazioni di suo interesse: "))
sogliaMin = int(input("Specifica il valore della soglia minima di allarme: "))
sogliaMax = int(input("Specifica il valore della soglia massima di allarme: "))

temp = 0
temp_sum = 0
temp_max = 0
temp_min = 0
max_violations = 0
min_violations = 0

counter = 0
while counter < nt:
	#input nt-temperature
	temp = int(input("Inserisci temperatura: "))
	temp_sum += temp
	
	#verifica violazione soglia
	if temp > sogliaMax:
		max_violations += 1
	elif temp < sogliaMin:
		min_violations += 1

	#min e max assoluti per il primo valore
	if counter == 0:
		temp_max = temp
		temp_min = temp

	#max e min assoluti dopo il secondo valore		
	if temp > temp_max:
		temp_max = temp
	elif temp < temp_min:
		temp_min = temp
	
	counter += 1

#output	
print("La media delle temperature è di", float(temp_sum/nt))
print("La temperatura minima è", temp_min)
print("La temperatura massima è", temp_max)
print("La soglia di allarme minima è stata superata", min_violations, "volte")
print("La soglia di allarme massima è stata superata", max_violations, "volte")
