#es. di prima; verificare che la stringa abbia almeno 4 caratteri (se ne ha meno restituire solo la stringa); se ne ha
#almeno 4 sostituire i primi due e gli ultimi due caratteri con una coppia di dollari
#es - gioco -> $$o$$
stringa = input("Scrivi stringa: ")

if len(stringa) < 4:
    print(stringa)
else:
    s1 = stringa[2:]
    s2 = s1[:-2]
    print("$$"+s2+"$$")
