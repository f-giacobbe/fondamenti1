#confronto tra stringhe		---> 	avviene in ordine LESSICOGRAFICO (ordine alfabetico + cifre e altri caratteri)
a = "Giuseppe"
b = "Giuda"
#b precede a, ma solo perché G è maiuscola, altrimenti il caso sarebbe diverso		# A < a
# b<a


print("apple" < "banana")	#>True
print("apple" == "apple")	#>True
print("apple" < "Apple")	#>False
print("apple" != "Apple")	#>True


#è possibile "accedere" alla posizione UNICODE del carattere attraverso la funzione ord()
print(ord("A"))		#>65 - la posizione UNICODE del carattere "A"
print(ord("B"))		#>66
print(ord("5"))		#>53
print(ord("a"))		#>97	#"a" viene dopo "A"


#chr() è la funzione inversa di ord():
print(chr(65))		#>A
print(chr(ord("B")))	#>B		"proprietà di identità"



#è necessario ricordare che le stringhe sono oggetti IMMUTABILI (nei singoli caratteri che la compongono)
#ovvero, una volta che assegnamo un valore a una variabile di tipo stringa, esso non può essere più modificato, a
#differenza degli altri tipi di variabile
#es.
s = "ciao"
#s[0] = "m" NON SI PUÒ FARE, ma bisogna utilizzare un' altra stringa
t = "m" + s[1:]		#ovvero aggiungo la stringa "m" alla stringa s troncata del primo elemento
print(t)	#>miao

#le stringhe sono ovvero oggetti da cui si può leggere, ma in cui non si può scrivere senza rimpiazzare l'intera
#stringa



#l'operatore "is" confronta due stringhe, senza però guardare il valore effettivo della stringa (a differenza di ==),
#ma andando a verificare se la locazione di memoria in cui le due stringhe sono salvate è la stessa
a = "Ciao"
b = "Ciao"
print(a is b)	#>True
