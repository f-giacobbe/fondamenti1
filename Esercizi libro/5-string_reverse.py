def reverse(str):
    new_str = ""

    for i in range(1, len(str)+1):
        new_str += str[-i]

    return new_str



str = "Ciao mi chiamo Francesco"

print(reverse(str))