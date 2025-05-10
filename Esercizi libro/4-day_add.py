def day_add(day, delta):
    """
    day is the current day, delta is how many days we want to count. it returns what day of the week
    it will be in delta days
    """
    days = ["SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"]

    day = day.upper()
    if day not in days:
        return
    
    day_index = days.index(day)
    future_day_index = (day_index + delta) % 7

    return days[future_day_index]


print(day_add(input("Write a day: "), int(input("How many days will elapse: "))))
