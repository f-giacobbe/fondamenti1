def substring_extract(text):
    """
    it extracts what's written between angle brackets <...>
    """
    substring = ""

    open_bracket_index = text.index("<")
    close_bracket_index = text.index(">")

    for i in range(open_bracket_index + 1, close_bracket_index):
        substring += text[i]

    return substring


my_text = "This is a text and <this is a substring> within my text"

print(substring_extract(my_text))