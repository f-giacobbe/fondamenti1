def sommasequenza(n_sq):
    somma = 0
    for i in range(n_sq):
        n = int(input("Digita numero da sommare:"))
        if n == 0:
          return somma, True
        else:
            somma += n
    return somma, False

n_sq = 1
stop = False
risultato = 0
while n_sq != 0 and stop == False:
    n_sq = int(input("Digita il numero di valori da sommare: "))
    risultato, stop = sommasequenza(n_sq)
    print(risultato, "è la somma")
