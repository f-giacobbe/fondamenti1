def days_in_month(month):
    """
    month is name of a month, it returns the number of days in that month (it ignores leap years)
    """
    months_length = {
        "JANUARY": 31,
        "FEBRUARY": 28,
        "MARCH": 31,
        "APRIL": 30,
        "MAY": 31,
        "JUNE": 30,
        "JULY": 31,
        "AUGUST": 31,
        "SEPTEMBER": 30,
        "OCTOBER": 31,
        "NOVEMBER": 30,
        "DECEMBER": 31
    }

    month = month.upper()
    if month not in months_length:
        return
    
    return months_length[month]


print(days_in_month(input("Choose a month: ")))