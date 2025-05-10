def seconds_in(s):
    s = (s%60)%60
    return s


print(seconds_in(9010))