# This code finds super prime numbers with five digits
# super prime number is for instance: 7331 --> 733 --> 73 --> 7 all of them are prime.

# We'll use a recursive function and regular functions to solve it

def is_prime(x):                          # Function returns if the argument is prime or not
    if(x > 1):
        for i in range(2,x+1):
            if( x % i == 0):
                return False
            else:
                return True
    else:
        return False

def cutting_last_digit(n):                # Function deletes last digit of prompted number
    n = int(str(n)[:-1])
    return n
    
def Super_primes(number):                 # Recursive function uses two functions ( but not finished yet )
    if len(str(number)) == 1 and is_prime(number):
        return number
    return cutting_last_digit(number)


