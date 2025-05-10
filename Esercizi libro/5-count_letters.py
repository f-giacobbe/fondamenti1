def count_letters(letter, word):
    count = 0
    for l in word:
        if l == letter:
            count += 1

    return count


word = "francesco"

print(count_letters("c", word))