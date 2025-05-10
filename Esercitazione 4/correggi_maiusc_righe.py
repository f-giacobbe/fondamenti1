f0 = open("testo.txt", "r")
f1 = open("nuovo_testo.txt", "w")

riga = f0.readline()

last_char = False
while riga:
    riga = riga.split(" ")
    

    #prima stringa
    if len(riga) == 1:
        if last_char:
            f1.write(riga[0].capitalize())
        else:
            f1.write(riga[0])
            
    else:
        if last_char:
            f1.write(riga[0].capitalize() + " ")
        else:
            f1.write(riga[0] + " ")
    last_char = False


    #dalla seconda stringa in poi
    for i in range(1, len(riga)):

        if i == len(riga)-1:
            if riga[i-1][-1] in ".?!":
                f1.write(riga[i].capitalize())
            else:
                f1.write(riga[i])
        else:
            if riga[i-1][-1] in ".?!":
                f1.write(riga[i].capitalize() + " ")
            else:
                f1.write(riga[i] + " ")


        if riga[i][-1] == "\n" and riga[i][-2] in ".?!":
            last_char = True

    riga = f0.readline()


f0.close()
f1.close()
