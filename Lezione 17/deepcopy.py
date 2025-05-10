#il modo più semplice per clonare una lista senza utilizzare il deepcopy è utilizzare lo slicing

a = [1, 2, 3, 4]
b = a

c = a[:]

a.append(5)

print(a)
print(b)
print(c)


