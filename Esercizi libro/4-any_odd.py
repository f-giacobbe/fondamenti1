def any_odd(l):
    """
    given a list, this function returns True if there is at least one odd number within the list, else False
    """
    for item in l:
        if item % 2 != 0:
            return True
    else:
        return False
    

print(any_odd([2, 4, 6, 8, 11]))