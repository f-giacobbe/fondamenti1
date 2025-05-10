#validazione input	-		verificare che l'utente digiti in ingresso un input valido (y, n, Y, N)

#verifica se msg valga uno dei  valori y, Y, n ed N; in caso di valori diversi allora si chiede all'utente di specificare un altro input

def rispostaCorretta(msg):
	input_valido = False
	risposta = input(msg)
	while not input_valido:
		risposta = risposta.upper()		#funzione definita sulla classe <str>
		if (risposta == "Y") or (risposta == "N"):
			input_valido = True
		else:
			risposta = input("Per favore digita Y per 'si', N per 'no'. \n" + msg)	#\n -> new line
	return risposta

rispostaCorretta("Ti piace il cazzo?: ")
