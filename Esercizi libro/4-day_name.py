def day_name(d):
    """
    it converts d (an integer) range 0-6 into the name of a day (Sunday-Saturday). Return None if the
    argument is not valid
    """
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    if not 0<=d<=6:
        return

    return days[d]


print(day_name(int(input("Choose a value from 0 to 6: "))))