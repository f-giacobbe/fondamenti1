#Assume the days of the week are numbered 0 - 6 (Sunday - Saturday). Write a program that asks a day number and prints the day name

weekdays = [
    (0, "Sunday"),
    (1, "Monday"),
    (2, "Tuesday"),
    (3, "Wednesday"),
    (4, "Thursday"),
    (5, "Friday"),
    (6, "Saturday")
]
day = int(input("Select a number from 0 to 6: "))
print(weekdays[day])

#I should've used a dictionary