#calcolo coefficiente binomiale
n = int(input("Digita il valore di n: "))
k = int(input("Digita il valore di k (ricorda che n >= k): "))
nk = int(n - k)
n_count = 1
k_count = 1
nk_count = 1
n_fact = 1
k_fact = 1
nk_fact = 1

#calcolo n!
while n_count <= n:
	n_fact = n_count * n_fact
	n_count += 1

#calcolo k!
while k_count <= k:
	k_fact = k_count * k_fact
	k_count += 1

#calcolo (n-k)!		
while nk_count <= nk:
	nk_fact = nk_count * nk_fact
	nk_count += 1
	
print(int((n_fact) / (k_fact * nk_fact)))

#RENDERLO PIU EFFICIENTE -> k! e (n-k)! sono già impliciti nel calcolo di n!
#														es. n = 10, k = 7, n-k = 3. Calcolo prima il più piccolo, ovvero 3!, dopo calcolo k! come 7x6x5x4x3!(n-k)!, ovvero n! come 10x9x8x7!(k!)
