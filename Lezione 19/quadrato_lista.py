def quadrato(l):
	m = l[:]
	
	if len(m) == 1:
		m[0] = m[0]**2
	else:
		m[0] = m[0]**2
		m[1:] = quadrato(m[1:])
		
	return m
	
	
l = [2, 3, 4, 5]
print(quadrato(l))
print(l)
