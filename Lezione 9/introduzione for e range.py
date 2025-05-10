#introduzione 'for'

for nome in ["Aldo", "Giulia", "Francesca", "Carlo"]:			#<[]> questa è una lista 	<nome> è una loop variable, che assume i valori in lista
	print("Ciao", nome, "sei invitato/a al mio compleanno")
print("-------------------")
	
	
for x in [1, 2, 3, 4, 5]:
	print(x**2)
print("-------------------")
	
	
#funzione range()
for x in range(5):			#equivalente a range(0, 5)
	print(x**2)
print("-------------------")

for x in range(2, 5):
	print(x**2)
print("-------------------")

for x in range(2, 11, 2):			#l'ultimo valore è il 'passo', ovvero ne prende (in questo caso) uno ogni 2
	print(x)
