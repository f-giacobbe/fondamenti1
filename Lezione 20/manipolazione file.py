#i file possono essere aperti in (apertura/scrittura) e manipolati come (stringhe/liste)

#in Python, il comando per aprire un file è:

### open(<file>, <(r/w)>) ###


#esempio
file = open("dati.txt", "r")

read = file.read()  #il comando READ crea una stringa contenente tutto il testo
                    #è possibile inserire come argomento un intero, e in questo caso verranno letti i prossimi x caratteri del file
print(read)


file.close()
file = open("dati.txt", "r")


read = file.readline()  #il comando READLINE crea una stringa contenente la prima riga di testo
print(read)

read = file.readlines() #il comando READLINES crea una lista contenente tutte le righe del file
print(read)

#notiamo che la seconda print dà come output solo la seconda riga, e non la prima. Questo è perché
#è importante ricordarsi che il cursore avanza nel file, sicché se vogliamo tornare indietro nel file, l'unico
#metodo è quello di chiudere il file e riaprirlo


#una volta che si ha finito di lavorare col file, è buona norma chiuderlo, attraverso la funzione CLOSE()

file.close()


###
print("\n")
###




#manipolazione file vera e propria
file = open("serietv.dat", "r")

for serie in file:
    l_serie = serie.split("-")
    print(l_serie[1])
file.close()




#il valore di una riga di file può essere utilizzata come espressione booleana
#esempio
file = open("serietv.dat", "r")
riga = file.readline()

while riga: #### il loop si interrompe quando il puntatore incontra la prima riga vuota
    print(riga)
    riga = file.readline()

file.close()




#per SCRIVERE su un file, oppure CREARE un nuovo file
file = open("newfile.txt", "w")     #cercando di aprire in scrittura un file che non esiste, viene creato
#ATTENZIONE : aprendo un file già esistente in scrittura, il suo contenuto viene cancellato

file.write("ciao ")
file.write("sono Francesco")
file.close()