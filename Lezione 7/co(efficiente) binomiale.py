n = int(input("Digita il valore di n: "))
k = int(input("Digita il valore di k (ricorda che n >= k): "))
nk = int(n - k)
n_count = 1
n_fact = 1
k_fact = 1
nk_fact = 1

while n_count <= n:
	n_fact = n_count * n_fact
	if n_count == k:
		k_fact = n_fact
	if n_count == nk:
		nk_fact = n_fact
	n_count += 1
	
print(int((n_fact) / (k_fact * nk_fact)))
