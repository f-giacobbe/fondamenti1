#verificare in maniera ricorsiva se una data stringa è palindroma
def is_palindroma(s):
	val = False
	
	if (len(s) == 0) or (len(s) == 1):
		val = True
	else:
		val = (s[0] == s[-1]) and (is_palindroma(s[1:-1]))
		
		
	return val
	


stringa = "pikip"
print(is_palindroma(stringa))
