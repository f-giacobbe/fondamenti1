#scrivere una funzione che riceva un intero n, e costruisce una matrice nxn composta da valori booleani
#dopo, data la matrice m, restituisce la matrice 2xn, dove la riga 0 conterrà l'and delle colonne,
#mentre la riga 1 conterrà l'or delle colonne

#AND diventa F al primo F; OR diventa T al primo T

def costruisci_matrice(n):
    m = []

    for riga in range(n):
        r = []

        for colonna in range(n):
            ok = False

            #verifica input valido
            while not ok:
                e = input(f"Inserisci valore booleano (T/F) in posizione riga {riga} e colonna {colonna}: ")
                e = e.upper()

                if e == "T":
                    r.append(True)
                    ok = True
                elif e == "F":
                    r.append(False)
                    ok = True

        m.append(r)

    return m



def and_or_mat(m):
    #costruiamo matrice 2xn (conoscendo già il numero di righe)
    m_res = [[], []]

    for colonna in range(len(m)):
        res_and = m[0][colonna]
        res_or = m[0][colonna]

        riga = 1
        while riga < len(m) and (res_and or not res_or):#

            if res_and and (not m[riga][colonna]):
                res_and = False

            if (not res_or) and (m[riga][colonna]):
                res_or = True

            riga += 1

        m_res[0].append(res_and)
        m_res[1].append(res_or)


    return m_res


print(*and_or_mat(costruisci_matrice(int(input("Inserisci dimensione matrice: ")))), sep="\n")
