def to_secs(h, m, s):
    """
    h is hours, m is minutes, s is seconds. It returns the total number of seconds as an integer
    """
    m += h*60
    s += m*60

    return int(s)


h = float(input("Hours: "))
m = float(input("Minutes: "))
s = float(input("Seconds: "))

print(to_secs(h, m, s))