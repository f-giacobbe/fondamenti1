#es. calcolare prodotto scalare tra due vettori (di uguale dimensione). Leggere da input i due vettori e produrre
#il prodotto scalare in uscita. Occorre verificare che i due vettori in input abbiano la stessa dimensione. 
#La verifica va fatta nel main, e la funzione va chiamata solo se i due vettori sono di uguale dimensione

def prodottoscalare(vec1, vec2):
	r = 0
	for i in range(len(vec1)):
		r += vec1[i]*vec2[i]
	return r

vec1 = []
vec2 = []
v1 = 1
v2 = 1

while v1 != 0:
	v1 = int(input("Digita elemento primo vettore: "))
	if v1 != 0:
		vec1.append(v1)
while v2 != 0:
	v2 = int(input("Digita elemento secondo vettore: "))
	if v2 != 0:
		vec2.append(v2)
		
if len(vec1) != len(vec2):
	print("Prodotto tra vettori non disponibile")
else:
	print(prodottoscalare(vec1, vec2))
