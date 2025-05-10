#funzione dove riceviamo un quantitativo di denaro 'd', una percentuale di interesse 'i', e un numero di anni 'a'
#la funzione ci restituisce il numero di denaro totale con l'interesse incluso

def calcolo_interesse(d, i, a):
    if a == 0:
        return d
    else:
        d = d + (d*i)/100
        return calcolo_interesse(d, i, a-1)
    

print(round(calcolo_interesse(int(input("Inserisci denaro: ")), int(input("Inserisci percentuale interesse: %")), int(input("Inserisci numero anni: "))), 2))