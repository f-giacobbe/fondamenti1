"""abbiamo un file contenente dei dati di studenti (MATRICOLA, NOME, COD. ESAME, VOTO)
scrivere un programma che faccia scegliere innanzitutto all'utente 
	calcolo media.
	scegli:
		1. per matricola
		2. per esame
	Digita la tua scelta:	
		
		
		scelta 1) Digita la matricola:			"La media di {nome} è {media}"
		scelta 2) Digita il codice dell'esame:		"La media richiesta è {media}"
			
			
nel caso in cui la matricola non esista, informiamo l'utente """



def media_matricola(file, matricola):
	f = open(file, "r")
	dati = f.readlines()
	f.close()
	
	#rimuovo i \n
	for i in range(len(dati)):
		dati[i] = dati[i][:-1]
	
	
	somma = 0
	voti_presi = 0
	for i in range(len(dati)):
		riga = dati[i].split("\t")
		
		if int(riga[0]) == matricola:
			somma += int(riga[3])
			voti_presi += 1
			
	if voti_presi == 0:
		return 0
	else:
		media = somma/voti_presi
	
	
	return round(media, 2)
	
	
	
def media_esame(file, esame):
	f = open(file, "r")
	dati = f.readlines()
	f.close()
	
	#rimuovo i \n
	for i in range(len(dati)):
		dati[i] = dati[i][:-1]

	
	somma = 0
	volte = 0
	for i in range(len(dati)):
		riga = dati[i].split("\t")
		
		if int(riga[2]) == esame:
			somma += int(riga[3])
			volte += 1
			
	if volte == 0:
		return 0
	else:
		media = somma/volte
	

	return round(media, 2)
	
	

f = "file_studenti.txt"
scelta1 = 0
scelta2 = 0
print("Calcolo media")


#prima interazione
ok = False
while not ok:
	scelta1 = int(input("Scegli:\n1. Per matricola\n2. Per esame\nDigita la tua scelta: "))
	
	if scelta1 == 1 or scelta1 == 2:
		ok = True
	else:
		print(f"{scelta1} non è un input valido. Riprova")


#media per matricola
if scelta1 == 1:
	
	ok = False
	while not ok:
		scelta2 = int(input("Digita la matricola: "))
		
		media = media_matricola(f, scelta2)
		
		if media != 0:
			ok = True
		else:
			print(f"Matricola {scelta2} non trovata. Riprova.")
			
	
	print(f"La media della matricola {scelta2} è {media}")
	
	
	

#media per esame
elif scelta1 == 2:
	
	ok = False
	while not ok:
		scelta2 = int(input("Digita il codice dell'esame: "))
		
		media = media_esame(f, scelta2)
		
		if media != 0:
			ok = True
		else:
			print(f"Esame {scelta2} non trovato. Riprova.")
			
	
	print(f"La media richiesta è {media}")
