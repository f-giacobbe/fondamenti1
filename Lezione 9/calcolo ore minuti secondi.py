#leggi un numero intero in input (secondi), convertendo in ore, minuti e secondi rimanenti
secondi = int(input("Digita il numero di secondi: "))

#calcolo minuti
minuti = secondi//60
secondi = secondi%60

#calcolo ore
ore = minuti//60
minuti = minuti%60

#output finale
print(ore, "ore", minuti, "minuti", secondi, "secondi")