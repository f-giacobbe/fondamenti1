#Check a list of n-numbers and print True only if all the numbers are odd

numbers = [1, 3, 5, 7, 9, 11, 2]
are_all_n_odd = ""

for n in numbers:
    if n % 2 == 0:
        are_all_n_odd = False
        break
else:
    are_all_n_odd = True

print(are_all_n_odd)