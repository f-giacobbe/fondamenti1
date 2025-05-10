#ITERATIVO - calcolare f(x) = x-1 utilizzando solo il (+1)

def f(x):
	r = 0
	for i in range(1, x):
		r = r+1
		
	return r
	
	
print(f(34))
