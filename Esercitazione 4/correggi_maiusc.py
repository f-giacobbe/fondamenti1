#dato un file di testo (separatore blank), correggere questo testo mettendo le maiuscole dopo i caratteri
# ". ? !"
#restituire lo stesso testo corretto


f = open("testo.txt", "r")
read = f.read()
f.close()

read = read.split(" ")

new_text = ""

for i in range(len(read)):
    if i == 0:
        new_text += read[i] + " "
    else:
        if read[i-1][-1] in ".?!":
            new_text += read[i].capitalize() + " "
        else:
            new_text += read[i] + " "


f = open("nuovo_testo.txt", "w")
f.write(new_text)
f.close()