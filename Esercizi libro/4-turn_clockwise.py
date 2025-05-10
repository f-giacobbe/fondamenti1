def turn_clockwise(c):
    """
    c is one of four compass points ("N", "E", "S", "W") and returns the next compass point in the
    clockwise direction
    """
    compass_points = ["N", "E", "S", "W"]
   
    c = c.upper()

    if c not in compass_points:
        return

    c_index = compass_points.index(c)
    c_turned_index = (c_index + 1) % 4 #it wraps up to the beginning of the list if necessary

    return compass_points[c_turned_index]


print(turn_clockwise(input("Type a compass point: ")))