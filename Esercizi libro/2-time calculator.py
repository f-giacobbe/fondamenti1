time_now = 100*int(input("What hour is it now? (24-hour format 0-23)"))
time_interval = 100*int(input("How many hours will pass by?"))

time_final = (time_now + time_interval)%2400

print(int(time_final/100), ":00 will be the time in", int(time_interval / 100), "hours")
