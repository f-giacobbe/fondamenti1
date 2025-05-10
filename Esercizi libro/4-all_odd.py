def all_odd(l):
    """
    given a list, it returns True only if all integers are odd, else False
    """
    for item in l:
        if item % 2 == 0:
            return False
    else:
        return True
    

my_list = [1, 1, 3, 9, 11]
print(all_odd(my_list))