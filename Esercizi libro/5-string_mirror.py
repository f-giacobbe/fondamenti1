def mirror(str):
    new_str = str

    for i in range(1, len(str)+1):
        new_str += str[-i]

    return new_str


my_str = "good"

print(mirror(my_str))