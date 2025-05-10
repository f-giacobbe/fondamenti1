def day_name(day):
    """
    it converts a day name and returns its number
    """
    days = ["SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"]

    day = day.upper()

    if day not in days:
        return

    day_index = days.index(day)
    return day_index


print(day_name(input("Write a day: ")))