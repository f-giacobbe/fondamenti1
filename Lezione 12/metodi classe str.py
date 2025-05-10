stringa = "Ciao Mario"
#questa variabile è composta in totale da 10 caratteri, ma la posizione dei caratteri parte dalla posizione 0. Sicché
#il carattere "C" avrà come indice 0, mentre il carattere "o" sarà in posizione 9. È possibile, tuttavia, contare in
#negativo		in questo caso il carattere "o" sarà in posizione -1, mentre "C" in posizione -10

#le parentesi quadre [] ci permettono di indicizzare (si tratta di un METODO della classe <str>)

carattere = stringa[2]
print(carattere)	#>a

print(stringa[-5])	#>M



s = "ciaO"

t = s.upper()	#>CIAO		è un METODO della classe <str> (un' operazione permessa sugli elementi della classe <str>)

print(t)

m = s.lower()	#METODO

print(m)	#>ciao

f = s.capitalize()	#METODO - capitalizza la prima lettera
print(f)	#>Ciao

#METODO .strip()	elimina i blank all'inizio e alla fine della stringa
#METODO .lstrip()	strip solo a sinistra
#METODO .rstrip()	strip solo a destra


#METODO .count(<char>)		conta il numero di volte in cui quel carattere occorre nella stringa data
stringa = "Ciao Francesco"
print(stringa.count("a"))	#>2		(il numero di volte in cui appare "a" in "Ciao Francesco")


#e molti altri...


#METODO len		-chiamato con len(<str>)	-	restituisce la lunghezza (in int) della stringa
print(len(stringa))		#funziona diversamente dagli altri metodi, essendo un metodo "astratto" o "metodo di classe"



#es. per prendere l'ultimo carattere di una stringa
print(stringa[-1])	#>o
#oppure
print(stringa[len(stringa)-1])	#è necessario il (-1), altrimenti dà l'errore out-of-range essendo l'ultimo elemento
								#della stringa in posizione len(str)-1
								


#SLICE operator (serve a "tagliare le stringe")
fruit = "banana"
print(fruit[:3])	#>ban		[n:m]
print(fruit[3:])	#>ana
print(fruit[1:3])	#>an

print(fruit[3:-10])	#non restituisce nulla, perché m < n, pur non determinando errore out-of-range
print(fruit[3:99])	#pur essendo 99 tecnicamente out-of-range, viene comunque restituito fino all'ultimo char utile
