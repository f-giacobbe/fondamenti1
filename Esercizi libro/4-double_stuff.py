def double_stuff(l):
    """
    a function that, given a list, doubles its elements
    """
    doubled_list = []
    for item in l:
        doubled_list.append(item*2)

    return doubled_list


my_list = [2, 3, 4, 5]

print(double_stuff(my_list))