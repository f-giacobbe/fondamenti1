def reverse_str(s):
	if len(s) == 0:
		t = ""
	elif len(s) == 1:
		t = s
	else:
		t = reverse_str(s[1:]) + s[0]
		
	return t
	
	
	
print(reverse_str("Francesco"))
