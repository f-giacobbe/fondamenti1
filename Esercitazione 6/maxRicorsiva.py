"""
si scriva una funzione ricorsiva maxRicorsiva(l) dove venga calcolato il massimo della lista l
"""

lista = [1, 0, 2, 7, -1, 3]


def maxRicorsiva(l):
    if len(l) == 1:
        return l[0]
    else:
        var = maxRicorsiva(l[1:])
        if l[0] > var:
            return l[0]
        else:
            return var

    

print(maxRicorsiva(lista))