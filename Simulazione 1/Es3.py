"""
si vuole realizzare un'applicazione per la gestione dei dati relativi ai clienti di un camping. Le informazioni
sono memorizzate in una matrice M1 avente 5 colonne, in cui la generica riga [modalità, numero, bambini, 
checkin, giorni] rappresenta il fatto che un numero di persone pari a numero, di cui bambini bambini, sono 
entrati nel camping in data checkin per trascorrere un numero di giorni pari a giorni in una delle seguenti
modalità (tenda, camper, bungalow). Per semplicità, la data di checkin viene espressa come una lista di len=2
i cui elementi indicano il giorno e il mese ([28, 7] - 28 luglio).
Il tariffario è memorizzato in una matrice M2 avente 2 colonne, in cui ogni riga rappresenta i prezzi 
giornalieri per persona o per modalità di permanenza per i tre mesi estivi luglio, agosto, settembre.
In particolare, la prima colonna di M2 assume 4 valori (persona, tenda, camper, bungalow), mentre la seconda
colonna contiene la lista dei tre valori interi che indicano il prezzo giornaliero per ognuno dei tre mesi 
in cui è aperto il camping.
Si scrivano le seguenti funzioni:

    -calcola_costo(M1, M2, i)   che restituisce il costo della permanenza nel camping per il gruppo di
    persone registrate alla riga con indice i della matrice M1. Il costo include i costi per ogni persona più
    il costo della tenda/camper/bungalow e deve essere calcolato tenendo in considerazione che il prezzo
    varia a seconda del mese e che i bambini non pagano.

    -statistiche(M1)    che restituisce una matrice di due colonne contenente per ogni riga il numero medio
    di persone adulte per modalità (tenda, camper o bungalow nel caso specifico)

    -classifica(M1, M2) che restituisce una lista contenente gli indici delle righe di M ordinati per costo
    della permanenza, dal più alto al più basso.

    -persone_mese(M1)   che restituisce una matrice 3x2 contenente il numero di persone presenti nel
    camping per ognuno dei tre mesi in cui il camping è aperto
"""

M1 = [
    ["tenda", 4, 2, [29, 7], 10],
    ["camper", 2, 0, [20, 7], 10],
    ["bungalow", 5, 3, [1, 8], 7],
    ["bungalow", 10, 6, [1, 8], 15],
    ["tenda", 3, 1, [26, 8], 9],
    ["camper", 4, 0, [29, 8], 5],
    ["tenda", 2, 0, [1, 9], 10]
]

M2 = [
    ["persona", [10, 15, 8]],
    ["tenda", [5, 10, 3]],
    ["camper", [10, 15, 8]],
    ["bungalow", [20, 25, 18]]
]



def giorni_mesi(M1, i):
    """
    dato un gruppo di indice i nella matrice M1, restituisce una lista di lunghezza 3 contenente i giorni
    trascorsi per ogni mese [giorni_luglio, giorni_agosto, giorni_settembre]
    """

    res = [0, 0, 0]

    mese_inizio = M1[i][3][1]
    giorno_inizio = M1[i][3][0]
    giorni_permanenza = M1[i][4]

    giorno_inizio_piu_permanenza = M1[i][3][0] + giorni_permanenza
    
    if mese_inizio == 7:
        
        if giorno_inizio_piu_permanenza > 31:
            res[0] = 31 - giorno_inizio + 1
            res[1] = giorni_permanenza - res[0]

            if res[1] > 31:
                res[2] = res[1] - 31
                res[1] -= res[2]

        else:
            res[0] = giorni_permanenza
        
    elif mese_inizio == 8:
        
        if giorno_inizio_piu_permanenza > 31:
            res[1] = 31 - giorno_inizio + 1
            res[2] = giorni_permanenza - res[1]

            if res[2] > 31:
                res[3] = res[2] - 31
                res[2] -= res[3]

        else:
            res[1] = giorni_permanenza

    else:
        res[2] = giorni_permanenza

    return res



def calcola_costo(M1, M2, i):
    costo_totale = 0

    n_adulti = M1[i][1] - M1[i][2]

    giorni_mensili = giorni_mesi(M1, i)


    #addebito prezzi persona
    for j in range(3):
        costo_totale += M2[0][1][j] * n_adulti * giorni_mensili[j]


    #addebito modalità campeggio
    if M1[i][0] == "tenda":
        for j in range(3):
            costo_totale += M2[1][1][j] * giorni_mensili[j]
    elif M1[i][0] == "camper":
        for j in range(3):
            costo_totale += M2[2][1][j] * giorni_mensili[j]
    elif M1[i][0] == "bungalow":
        for j in range(3):
            costo_totale += M2[3][1][j] * giorni_mensili[j]


    return costo_totale



def statistiche(M1):
    res = [
        ["tenda", 0],
        ["camper", 0],
        ["bungalow", 0]
    ]

    
    for i in range(len(res)):

        n_adulti = 0
        volte = 0

        for j in range(len(M1)):
            if M1[j][0] == res[i][0]:
                volte += 1
                n_adulti += M1[j][1] - M1[j][2]

        res[i][1] = n_adulti/volte

    return res



def classifica(M1, M2):
    totali_per_indice = []
    res = []

    for i in range(len(M1)):
        totali_per_indice.append([i, calcola_costo(M1, M2, i)])
    

    while len(totali_per_indice) != len(res):
        i_max = 0
        massimo = totali_per_indice[0][1]

        for i in range(len(totali_per_indice)):
            if totali_per_indice[i][1] > massimo:
                i_max = i
                massimo = totali_per_indice[i][1]

        res.append(i_max)
        
        totali_per_indice[i_max][1] = 0


    return res



def persone_mese(M1):
    res = [
        [7, 0],
        [8, 0],
        [9, 0]
    ]

    for i in range(len(M1)):
        persone = M1[i][1]
        giorni = giorni_mesi(M1, i)

        for j in range(3):
            if giorni[j] > 0:
                res[j][1] += persone

    return res