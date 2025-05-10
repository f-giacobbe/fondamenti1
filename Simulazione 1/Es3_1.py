R = [
    [10, 1, 15, 17, "Vendite"],
    [10, 1, 17, 18, "Progetti"],
    [16, 2, 10, 12, "Vendite"],
    [16, 2, 13, 15, "Progetti"],
    [5, 3, 10, 13, "Progetti"]
]


def argomento_comune(R):

    tempo_max = 0
    arg_max = ""

    #creo una lista contenente tutti gli argomenti distinti
    arg_list = []
    for i in range(len(R)):
        if R[i][4] not in arg_list:
            arg_list.append(R[i][4])

    for arg in arg_list:
        max_locale = 0
        for i in range(len(R)):
            if R[i][4] == arg:
                max_locale += R[i][3]-R[i][2]

        if max_locale > tempo_max:
            tempo_max = max_locale
            arg_max = arg

    return arg_max



def controlla(R, g, m):

    #creo una lista contenente delle liste di len.2 contenenti ora di inizio e di fine per ogni riunione
    #in più, eseguo il primo controllo
    l_orari = []
    for i in range(len(R)):
        if (R[i][0] == g) and (R[i][1] == m):
            l_orari.append([R[i][2], R[i][3]])

            if R[i][3] < R[i][2]:
                return False
            
    #controllo sovrapposizioni
    for i in range(len(l_orari)):
        for j in range(i+1, len(l_orari)):
            if l_orari[i][0] < l_orari[j][0] < l_orari[i][1]:
                return False
            
    return True



def sposta(R, g, m, arg):

    #creo una sottomatrice contenente solo le riunioni di quel giorno
    subR = []
    lista_indici_estratti = []
    for i in range(len(R)):
        if (R[i][0] == g) and (R[i][1] == m):
            subR.append(R[i][:])
            lista_indici_estratti.append(i)

    #eseguo gli spostamenti sulla sottomatrice
    for i in range(len(subR)):
        if subR[i][4] == arg:
            subR[i][2] += 1
            subR[i][3] += 1


    #controllo ed eventuale aggiornamento matrice R
    if not controlla(subR, g, m):
        return False
    else:
        for i in lista_indici_estratti:
            R[i] = subR[0]
            del subR[0]

        return True
    

print(*R, sep="\n")
print(argomento_comune(R))
print(controlla(R, 10, 1))
print(sposta(R, 10, 1, "Vendite"))
print(*R, sep="\n")