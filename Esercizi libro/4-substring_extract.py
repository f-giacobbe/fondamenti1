def substring_extract(s):
    """
    suppose s contains at most one substring <...>. this function will extract what is between those brackets
    """
    i1 = s.index("<")
    i2 = s.index(">")

    substring = s[i1+1:i2]

    return substring


s = "questo è un esempio di stringa e <questa invece è una sottostringa> arrivederci."

print(substring_extract(s))