#verificare se una matrice nxn è una scacchiera (1 e 0 alternati):
    #sono presenti solo 0 e 1
    #i valori si alternano tra di loro


m = [
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1]
]



def is_scacchiera(m):
    ok = True

    inizio = m[0][0]
    if inizio == 1:
        opp_inizio = 0
    elif inizio == 0:
        opp_inizio = 1
    else:
        ok = False

    i = 0
    while i < len(m) and ok:
        j = 0
        while j < len(m) and ok:
            if i%2==0 and j%2==0 and m[i][j] != inizio:
                ok = False
            elif i%2==0 and j%2==1 and m[i][j] != opp_inizio:
                ok = False
            elif i%2==1 and j%2==0 and m[i][j] != opp_inizio:
                ok = False
            elif i%2==1 and j%2==1 and m[i][j] != inizio:
                ok = False

            j += 1

        i += 1

    return ok



print(is_scacchiera(m))