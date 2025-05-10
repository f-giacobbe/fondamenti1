import string

def remove_punctuation_and_split(text):
    new_text = ""

    for letter in text:
        if letter not in string.punctuation:
            new_text += letter

    return new_text.split()


def analysis(text):
    """
    this function removes all punctuation from the string, breaks the string into a list of words,
    and counts the number of words in your text that contain the letter e
    """
    text = remove_punctuation_and_split(text)

    word_count = len(text)
    e_count = 0

    for word in text:
        if "e" in word.lower():
            e_count += 1

    e_percentage = round(float((e_count/word_count)*100), 1)

    return f'Your text contains {word_count} words, of which {e_count} ({e_percentage}%) contain an "e"'


my_text = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""

print(analysis(my_text))