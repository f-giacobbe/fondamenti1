def hypotenuse(l1, l2):
    """
    it returns the length of the hypotenuse of a right triangle given the lengths of the two legs as parameters
    """
    h = (l1**2 + l2**2)**0.5
    return h


print(hypotenuse(9, 12))