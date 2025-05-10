#scrivere una funzione che dato il file voti.dat dia in output la media dei voti di ogni matricola

f = open("/Users/francescogiacobbe/Documents/Istruzione/Università/Anno I/Fondamenti di Informatica I/Lezione 20/voti.dat", "r")
righe = f.readlines()[1:]
f.close()


#rimuove i \n
for i in range(len(righe)):
    if righe[i][-1] == "\n":
        righe[i] = righe[i][:-1]



#sostituisco a ogni riga (str) una lista formata dai singoli elementi separati da "-"
for i in range(len(righe)):
    righe[i] = righe[i].split("-")



for i in range(len(righe)):
    somma = 0

    for j in range(1, len(righe[i])):
        somma += int(righe[i][j])

    media = round(somma/(len(righe[i])-1), 2)
    print(righe[i][0], "\t", media)
