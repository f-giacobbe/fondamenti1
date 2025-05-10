f = open("/Users/francescogiacobbe/Documents/Istruzione/Università/Anno I/Fondamenti di Informatica I/Lezione 20/voti.dat", "r")

#prima matricola + rimozione \n
riga = f.readline().split("\t")



while riga:
    n_voti = 0
    tot_voti = 0

    for voto in riga[1:]:
        n_voti += 1
        tot_voti += float(voto)

    if n_voti > 0:
        print(int(riga[0]), "\t", round(tot_voti/n_voti, 2))
              
    riga = f.readline().split("\t")
