#funzione ricorsiva con due input(a, b), e restituisce la somma dei due valori
#la funzione può solo sommare e sottrarre il valore 1

#a,b >= 0
def somma(a, b):
    tot = 0
    if b == 0:
        tot = a
    else:
        tot = somma(a+1, b-1)
    return tot


print(somma(10, 5))
