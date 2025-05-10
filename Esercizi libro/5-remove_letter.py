def remove_letter(letter, string):
    new_str = ""

    for l in string:
        if l != letter:
            new_str += l

    return new_str


print(remove_letter("b", "banana"))