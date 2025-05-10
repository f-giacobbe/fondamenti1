prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
    if letter == "O" or letter == "Q":
        print(f"{letter}u{suffix}")
    else:
        print(letter + suffix)