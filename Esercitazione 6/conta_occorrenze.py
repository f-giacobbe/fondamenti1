"""
scrivere una funzione ricorsiva conta_occorrenze(s, c) dove data una stringa s e un carattere c bisogna
contare il numero di occorrenze di c in s
"""


def conta_occorrenze(s, c):
    if len(s) == 0:
        return 0
    else:
        var = conta_occorrenze(s[1:], c)
        if s[0] == c:
            return 1 + var
        else:
            return var
        

print(conta_occorrenze("Francesco", "c"))