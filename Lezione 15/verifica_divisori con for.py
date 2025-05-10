#date due liste di interi, verificare se nella prima lista esista un elemento che è divisore di tutti gli
#elementi della seconda lista (return bool)

def divisore_singolo(x, lista):
    isTrue = True
    for item in lista:
        if item % x != 0:
            isTrue = False
            break
    
    return isTrue


def divisore_tra_liste(l1, l2):
    isTrue = False
    for item in l1:
        if divisore_singolo(item, l2):
            isTrue = True
            break

    return isTrue



l1 = [9, 3, 4, 2]
l2 = [2, 4, 6, 8, 10]

print(divisore_tra_liste(l1, l2))