# This function returns sum of the numbers through 
# prompted argument N


def one_2_N(n):
    if n < 1:
        print("Not valid number dude!")
    elif n == 1:
        return 1
    else:
        return n + one_2_N(n-1)

print(one_2_N(-1))
print(one_2_N(8))
