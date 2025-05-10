p = float(input("What is your initial investment in US dollars?"))
r = float(input("What is the annual nominal interest rate? (as a decimal)"))
n = float(input("How many times per year is the interest compounded?"))
t = int(input("How many years are you planning to invest for?"))

a = round(p*(1+(r/n))**(n*t))

print(a, " is your compound interest")