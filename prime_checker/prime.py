import math


def prime_checker(num):
    if num == 1:
        is_prime = False

    is_prime = True
    for i in range(2, math.ceil(num/2)+1):
        if num % i == 0:
            is_prime = False
    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")


number = int(input("Enter the number: \n"))
prime_checker(number)
