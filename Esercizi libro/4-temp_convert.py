def fahrenheit_to_celsius(f):
    c = (f-32)*(5/9)
    return int(c)


print(fahrenheit_to_celsius(36))



def celsius_to_fahrenheit(c):
    f = (c*(9/5)) + 32
    return int(f)


print(celsius_to_fahrenheit(18))