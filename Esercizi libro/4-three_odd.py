def three_odd(l):
    """
    given a list, it returns True if at least three numbers are odd
    """
    odd_counter = 0
    for item in l:
        if item % 2 != 0:
            odd_counter += 1
            if odd_counter >= 3:
                break
    
    return odd_counter >= 3
    

l = [2, 3, 4, 5, 7]
print(three_odd(l))


#or


def three_odd_v2(l):
    odd_counter = 0
    i = 0
    while odd_counter < 3 and i < len(l):
        if l[i] % 2 != 0:
            odd_counter += 1
        i += 1
    
    return odd_counter >= 3


print(three_odd_v2(l))