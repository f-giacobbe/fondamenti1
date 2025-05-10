m = [
	[2, -4, 7, 14, 4],
	[0, 1, 6, 9, 13],
	[7, 15, 5, 3, 2],
	[3, 25, 6, 0, 10],
	[10, 9, 2, 5, 0]
	]



def maxmin(l):
	massimo = l[0]
	for i in range(1, len(l)):
		if l[i] > massimo:
			massimo = l[i]
			
	return massimo



def minA(m):
	minimo = m[0][0]
	
	#se n è pari
	if len(m)%2==0:
		
		#ragiono per colonna, in modo che l'intervallo decresca strettamente
		for j in range(len(m)//2):
			for i in range(j, len(m)-j):
				if m[i][j] < minimo:
					minimo = m[i][j]
	
	#se n è dispari				
	else:
		for j in range((len(m)//2)+1):
			for i in range(j, len(m)-j):
				if m[i][j] < minimo:
					minimo = m[i][j]
				
	return minimo



#n >= 3
def minB(m):
	minimo = m[-1][1]
	for i in range((len(m)//2)+1, len(m)):
		for j in range(len(m)-i, i):
			if m[i][j] < minimo:
				minimo = m[i][j]

	return minimo



def minC(m):
	minimo = m[0][-1]
	
	#n pari
	if len(m)%2==0:
		for j in range(len(m)//2, len(m)):
			for i in range(len(m)-1-j, j+1):
				if m[i][j] < minimo:
					minimo = m[i][j]
	#n dispari
	else:
		for j in range((len(m)//2)+1, len(m)):
			for i in range(len(m)-1-j, j+1):
				if m[i][j] < minimo:
					minimo = m[i][j]

	return minimo



#n >= 3
def minD(m):
	minimo = m[0][1]

	#n pari
	if len(m)%2==0:
		for i in range((len(m)//2)-1):
			for j in range(i+1, len(m)-1-i):
				if m[i][j] < minimo:
					minimo = m[i][j]

	#n dispari
	else:
		for i in range(len(m)//2):
			for j in range(i+1, len(m)-1-i):
				if m[i][j] < minimo:
					minimo = m[i][j]

	return minimo
	 


def maxminmatrice(m):
	l = []
	l.append(minA(m))
	l.append(minC(m))

	if len(m) >= 3:
		l.append(minB(m))
		l.append(minD(m))
	
	return maxmin(l)
	
	
	
print(maxminmatrice(m))