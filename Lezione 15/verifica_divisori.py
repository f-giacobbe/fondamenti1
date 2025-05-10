#date due liste di interi, verificare se nella prima lista esista un elemento che è divisore di tutti gli
#elementi della seconda lista (return bool)

def divisore_di_tutti(x, l):
    cond = True
    i = 0
    while cond and i < len(l):
        if l[i] % x != 0:
            cond = False
        else:
            i += 1

    return cond


def divisore_in_lista(l1, l2):
    cond = False
    i = 0
    while not cond and i < len(l1):
        if divisore_di_tutti(l1[i], l2):
            cond = True
        else:
            i += 1

    return cond


l1 = [2, 3, 4]
l2 = [2, 4, 6, 7, 10]

print(divisore_in_lista(l1, l2))
