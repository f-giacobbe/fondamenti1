n = int(input("Digita un numero: "))

prime = 1

i = 2
while i < n and prime == 1:
    if n%i == 0:
        prime = 0

    i += 1

if prime == 1:
    print(n, "è primo")
else:
    print(n, "NON è primo")