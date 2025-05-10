""" si scriva una funzione 'verifica' che riceve una matrice M di interi e restituisce True se e solo se
il primo elemento di ogni riga i è il massimo oppure il minimo della riga """



def massimo(l):
    valore = l[0]
    for i in range(len(l)):
        if l[i] > valore:
            valore = l[i]

    return valore

def minimo(l):
    valore = l[0]
    for i in range(len(l)):
        if l[i] < valore:
            valore = l[i]

    return valore


def verifica(m):
    cond = True
    
    i = 0
    while cond and i < len(m):
        
        if (m[i][0] != massimo(m[i])) and (m[i][0] != minimo(m[i])):
            cond = False

        i += 1

    return cond



m = [
    [2, 5, 3, 5, 5],
    [5, 3, 3, 4, 3],
    [9, 2, 4, 5, 4]
]

print(verifica(m))