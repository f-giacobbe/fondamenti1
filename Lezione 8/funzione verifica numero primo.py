def primecalculator(n):
    prime = 1
    i = 2
    while i < n and prime == 1:
        if n%i == 0:
            prime = 0
        i += 1

    if prime == 0:
        return n, "non è primo"
    else:
        return n, "è primo"

print(primecalculator(int(input("Digita numero: "))))