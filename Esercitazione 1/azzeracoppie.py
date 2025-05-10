#funzione che prende in ingresso un vettore v e crea un nuovo vettore w contenente gli elementi singoli del
#vettore v, mentre vengono azzerate le coppie di numeri


#funziona anche per sequenze di più di tre elementi uguali in quanto il confronto avviene nel vettore v, mentre
#le modifiche nel vettore w
def azzeracoppie(v):
    w = v[:]

    for i in range(1, len(v)-1):    #perché l'ultimo elemento non ha successori
        inCoppia = False

        #confronto elemento con il suo predecessore
        if v[i] == v[i-1]:
            w[i-1] = 0
            inCoppia = True
        #confronto elemento con il suo successore
        if v[i] == v[i+1]:
            w[i+1] = 0
            inCoppia = True

        #azzero l'elemento stesso
        if inCoppia:
            w[i] = 0

    return w
        



v = [1, 3, 3, 2, 1, 5, 5, 5, 7]
print(azzeracoppie(v))


#la prima versione però non funziona per liste di lunghezza 2
def azzeracoppie_v2(v):
    w = v[:]

    for i in range(len(v)):
        inCoppia = False

        if i>0 and v[i] == v[i-1]:
            w[i-1] = 0
            inCoppia = True

        if i < len(v)-1 and v[i] == v[i+1]:
            w[i+1] = 0
            inCoppia = True

        if inCoppia:
            w[i] = 0

    return w

print(azzeracoppie_v2(v))
print("!" in "?!.")