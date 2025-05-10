def decimale_base(n, base):
    """
    converte qualsiasi numero decimale a qualsiasi base
    """
    s = ""
    n = int(n)
    base = int(base)

    while n > 0:
        s = s + str(n%base)
        n = n//base
    
    s = s[::-1]

    return s



print(decimale_base(input("Digita numero decimale: "), input("Digita base: ")))