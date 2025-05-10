def area_of_circle(r):
    import math
    """
    it calculates the area of a circle of radius r
    """
    return float(math.pi * r**2)

print("The circle area is", round(area_of_circle(float(input("Type the circle radius: "))), 2))