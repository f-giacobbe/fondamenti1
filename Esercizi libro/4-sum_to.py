#write a fruitful function sum_to(n) that returns the sum of all integer numbers up to and including n

def sum_to(n):
    """
    This function returns the sum of all integers up to and including n
    """
    sum = 0
    for n in range(n+1):
        sum += n
    return sum

print(sum_to(int(input("Type a number: "))))