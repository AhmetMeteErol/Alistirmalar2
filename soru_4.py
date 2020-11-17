# This code prints first thirty number of fibonacci series

def fibonacci(n):                               # function finds n'th fibonacci number
    if n == 1 or n == 0:
        return n

    return fibonacci(n-1) + fibonacci(n-2)

for i in range(1,31):                           # It was struggling to print in recursive function so i used a for loop
    print(fibonacci(i), end= ' ')
