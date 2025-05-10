def verifica_presenza(a,b):
    v = []
    somma = 0
    for el in a:
        somma += el

        if el in b:
            v.append(el)
        else:
            v.append(somma)

    return v


a = [5, 2, 3, 5, 9, 3]
b = [3, 5, 7]
print(verifica_presenza(a,b))