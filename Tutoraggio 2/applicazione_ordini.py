"""si vuole realizzare un'applicazione per la gestione delle informazioni riguardanti clienti e ordini
presso un negozio online. Ogni ordine è effettuato da un cliente. I clienti e gli ordini sono identificati
mediante codici interi: i clienti hanno codice da 1 a p e gli ordini da 1 a k.

I dati relativi ai clienti sono memorizzati in una matrice CL avente 3 colonne, in cui la generica riga
[cc, cg, e] denota il fatto che il cliente con codice cc ha cognome cg ed età e. 

I dati relativi agli ordini sono memorizzati nella matrice OR, con 3 colonne, in cui la generica riga [co, cc, t]
denota il fatto che l'ordine con codice co è stato effettuato dal cliente con codice cc, il quale ha sostenuto
una spesa totale pari a t per tale ordine.

1. Si scriva cognomi_clienti_giovani(CL, s) che restituisce una lista contenente i cognomi dei clienti
di età minore o uguale ad s

2. Si scriva una funzione spesa_totale(CL, OR, cognome) che restituisce la spesa totale sostenuta dai clienti
aventi cognome 'cognome'

3. codici_clienti_simili(OR, ccliente) che restituisce la lista dei codici dei clienti diversi dal cliente con codice
ccliente che hanno effettuato lo stesso numero di ordini di ccliente """


CL = [
    [1, "Rossi", 20],
    [2, "Bianchi", 42],
    [3, "Rossi", 30],
    [4, "Verdi", 27]
]

OR = [
    [1, 4, 50],
    [2, 3, 100],
    [3, 3, 200],
    [4, 1, 150],
    [5, 2, 50],
    [6, 2, 100],
    [7, 4, 200]
]



def cognomi_clienti_giovani(CL, s):
    ris = []

    for i in range(len(CL)):

        if CL[i][2] <= s:
            ris.append(CL[i][1])

    return ris



def spesa_totale(CL, OR, cognome):
    codici_clienti = []

    #mi salvo i codici dei clienti con cognome "cognome"
    for i in range(len(CL)):
        if CL[i][1].lower() == cognome.lower():
            codici_clienti.append(CL[i][0])


    totale = 0

    for i in range(len(OR)):
        if OR[i][1] in codici_clienti:
            totale += OR[i][2]

    
    return totale



def codici_clienti_simili(OR, ccliente):
	lista_altri_clienti = []
	ordini_ccliente = 0
	
	#calcolo n.ordini fatti da ccliente
	for i in range(len(OR)):
		if OR[i][1] == ccliente:
			ordini_ccliente += 1
			
			
	
	#verifica altri clienti
	for i in range(len(CL)):
		totale_temp = 0
		
		if CL[i][0] != ccliente:
			
			for j in range(len(OR)):
				if OR[j][1] == CL[i][0]:
					totale_temp += 1
					
			if totale_temp == ordini_ccliente:
				lista_altri_clienti.append(CL[i][0])
			
			
	return lista_altri_clienti



print(spesa_totale(CL, OR, "Rossi"))
print(cognomi_clienti_giovani(CL, 27))
print(codici_clienti_simili(OR, 4))
