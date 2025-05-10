#scrivere una funzione che dato un file di testo restituisca il numero di vocali all'interno del testo

def controlla_vocali(file_path):
    f = open(file_path, "r")
    text = f.read()
    f.close()

    vocali = "aeiouAEIOUàáâäæãåāèéəêëęėēìíîïįīòóôöõœøōùúûüū"
    vocali_count = 0

    for i in range(len(text)):
        if text[i] in vocali:
            vocali_count += 1

    return vocali_count


print("Il numero di vocali nel seguente testo è", controlla_vocali("controlla_vocali.txt"))