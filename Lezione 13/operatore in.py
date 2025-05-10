#l'"in" funge anche da operatore booleano, per verificare la presenza o meno di un valore in una stringa/lista
print("a" in "Bach")	#>True
print("d" in "Bach")	#>False
print("ac" in "Bach")	#>True
print("ca" in "Bach")	#>False
print("Bach" in "Bach") #>True

#la stringa vuota appartiene a qualsiasi stringa
print("" in "Bach")		#>True
#però
print(" " in "Bach")	#>False


#molto utile anche la negazione, ovvero l'operatore "not in"
print("ca" not in "Bach")	#>True
