#dato un vettore l, creare un vettore l1 contenente solo gli elementi pari di l

def vettore_pari(l):
    l1 = []
    for n in l:
        if n%2 == 0:
            l1.append(n)

    return l1


l = [1, 2, 3, 4, 5, 7, 9, 8, 12, 13]
print(vettore_pari(l))