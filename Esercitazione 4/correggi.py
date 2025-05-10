def correggi_maiusc(filename):
    f = open(filename, "r")
    f_new = open("/Users/francescogiacobbe/Documents/Istruzione/Università/Anno I/Fondamenti di Informatica I/Esercitazione 4/nuovo_testo.txt", "w")

    caratteri = "?!."

    riga = f.readline().split(" ")

    prox_maiusc = False


    while riga:

        #prima str
        if prox_maiusc:
            f_new.write(riga[0].capitalize() + " ")
            prox_maiusc = False
        else:
            f_new.write(riga[0] + " ")

        print(riga)
        #prima e ultima str
        if (len(riga) == 1) and (riga[0][-2] in caratteri):
            prox_maiusc = True

        #dalla seconda str
        for i in range(1, len(riga)):
            if riga[i-1][-1] in caratteri:
                f_new.write(riga[i].capitalize() + " ")
            else:
                f_new.write(riga[i] + " ")

            #ultima str
            if i == (len(riga) - 1):
                if riga[i][-2] in caratteri:
                    prox_maiusc = True

        
        riga = f.readline().split(" ")

    f.close()
    f_new.close()

    return



correggi_maiusc("/Users/francescogiacobbe/Documents/Istruzione/Università/Anno I/Fondamenti di Informatica I/Esercitazione 4/testo.txt")