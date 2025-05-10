""" si vuole realizzare un'applicazione per la gestione delle informazioni riguardanti i biglietti emessi
da un'agenzia viaggi.
Ogni biglietto è ordinato da un cliente. I clienti sono identificati mediante i loro codici fiscali, le città
mediante codici interi da 1 a m.
I dati relativi ai biglietti sono memorizzati in una matrice OR avente 3 colonne, in cui la generica riga
[cf, c1, c2] denota il fatto che il cliente con codice fiscale cf ha richiesto un biglietto dalla città c1
alla città c2.
I prezzi dei biglietti sono memorizzati in una matrice PR, di dimensioni mxm, il cui generico elemento 
PR[i][j] contiene il prezzo del viaggio dalla città i alla città j. La matrice PR non è simmetrica in quanto
il viaggio da una città i alla città j potrebbe avere un prezzo diverso rispetto al viaggio da j ad i.
Ovviamente, la diagonale principale di PR contiene solo zeri.

Si scriva un modulo che metta a disposizione le funzioni:
    1) clienti_simili (OR, PR, cf1, cf2) che restituisce True se e solo se i clienti con codici fiscali cf1
     e cf2 hanno sostenuto una spesa totale simile (cioè la differenza tra le due spese totali è inferiore
     al 10%) -> FORMULA DIFFERENZA PERCENTUALE
      
    2) spesa_totale_clienti(OR, PR, CF), dove CF è una lista di codici fiscali di clienti, che restituisce
     la spesa totale sostenuta dai clienti il cui codice fiscale comparae in CF
      
    3) verifica(PR) che restituisce True se e solo se il viaggio diretto tra due città è sempre più conveniente
    rispetto al viaggio che attraversa una terza città. In altri termini, la funzione restituisce True se e 
    solo se comunque si scelgano tre città diverse i, j, e k, si ha sempre PR[i][j]+PR[j][k] > PR[i][k] """


OR = [
    ["ABC", 0, 3],
    ["ABC", 1, 0],
    ["DEF", 2, 3],
    ["DEF", 2, 4],
    ["GHI", 4, 3],
    ["JKL", 4, 2],
    ["ABC", 0, 2],
    ["JKL", 1, 2]
]

PR = [
    [0, 30, 50, 40, 30],
    [40, 0, 60, 50, 50],
    [30, 30, 0, 10, 20],
    [50, 50, 30, 0, 40],
    [20, 20, 60, 50, 0]
]



def spesa_cf(OR, PR, cf):
    lista_viaggi = []
    totale_spesa = 0

    for i in range(len(OR)):
        if OR[i][0] == cf:
            lista_viaggi.append([OR[i][1], OR[i][2]])

    for i in range(len(lista_viaggi)):
        totale_spesa += PR[lista_viaggi[i][0]][lista_viaggi[i][1]]

    return totale_spesa


def massimo(l):
    res = l[0]
    for e in l:
        if e > res:
            res = e

    return res



def minimo(l):
    res = l[0]
    for e in l:
        if e < res:
            res = e

    return res



def differenza_percentuale(a, b):
    maxx = massimo([a, b])
    minn = minimo([a, b])


    return abs((maxx-minn)/minn)*100



def clienti_simili(OR, PR, cf1, cf2):
    spesa1 = spesa_cf(OR, PR, cf1)
    spesa2 = spesa_cf(OR, PR, cf2)

    return differenza_percentuale(spesa1, spesa2) < 10



def spesa_totale_clienti(OR, PR, CF):
    totale = 0

    for codice in CF:
        totale += spesa_cf(OR, PR, codice)

    return totale



def verifica_singola(PR, i, j):
    for k in range(len(PR)):
        if (PR[i][k] + PR[k][j] < PR[i][j]) and (PR[i][k] != 0) and (PR[k][j] != 0):
            return False
        
    return True



def verifica(PR):
    for i in range(len(PR)):
        for j in range(len(PR)):
            if (i != j) and (not verifica_singola(PR, i, j)):
                return False
            
    return True
