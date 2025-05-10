#input valore voto (18-30), convertirlo in stringa 18-20 - sufficiente, 21-23 - discreto, 24-27 - buono, 28-30 - ottimo

voto = int(input("Digita voto: "))
voto_str = 0

if 18 <= voto <= 20:
	voto_str = "sufficiente"
elif 21 <= voto <= 23:
	voto_str = "discreto"
elif 24 <= voto <= 27:
	voto_str = "buono"
elif 28 <= voto <= 30:
	voto_str = "ottimo"
	
print(voto_str)
