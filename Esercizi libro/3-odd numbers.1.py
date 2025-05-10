#Check a list of n-numbers and print True if AT LEAST 3 of the numbers are odd

numbers = [1, 3, 0, 0, 0, 8, 2]
odd_counter = 0

for n in numbers:
    if n % 2 == 1:
        odd_counter += 1
    if odd_counter == 3:
        break

print(odd_counter == 3)