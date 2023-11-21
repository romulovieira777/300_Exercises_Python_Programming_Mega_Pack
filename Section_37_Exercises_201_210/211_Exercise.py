"""
Exercise No. 211

A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers.

Examples of prime numbers: 2, 3, 5, 7, 11, 13, 17, 19, ...

The prime number in position one is 2. The prime number in position two is 3. The prime number in position three is 5.

Implement a function that returns a prime number at position 100.

In the solution, use the function is_prime() from the previous exercise.

    def is_prime(n):

    if n < 2:
        return False

    if n % 2 == 0:
        return n == 2

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2

    return True

Present the solution in the form of a function called calculate(). In response, call calculate() function and print the
result to the console.

Expected result:

    541
"""
# Solution I


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def calculate():
    i = 1
    prime = 1
    while i <= 100:
        prime += 1
        if is_prime(prime):
            i += 1
    return prime


print(calculate())


# Solution II
def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def calculate():
    counter = 0
    number = 2
    while True:
        if is_prime(number):
            counter += 1
            if counter == 100:
                return number
        number += 1


print(calculate())
