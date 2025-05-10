#This is how you remove duplicates from a list while still maintaining the order:

old = ["a", "b", "a", "c", "c", "b"]

new = []

for item in old:
    if item not in new:
        new.append(item)

print(new)