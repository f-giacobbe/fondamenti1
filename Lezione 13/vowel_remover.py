def vowel_remover(s):
	"""
	this function removes vowels from a string
	"""
	vowels = "aeiouAEIOU"
	no_vowels = ""
	
	for c in s:
		if c not in vowels:
			no_vowels += c
			
	return no_vowels
			
			
print(vowel_remover(input("Type string: ")))
