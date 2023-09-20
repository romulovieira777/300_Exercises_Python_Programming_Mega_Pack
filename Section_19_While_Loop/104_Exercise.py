"""
Exercise No. 104

Write a program that prints to the console the first ten prime numbers separated by comma.

Tip: Use a while loop with break statement.

Expected result:

    2,3,5,7,11,13,17,19,23,29
"""


# Solution I
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


count = 0
num = 2
prime_numbers = []

while count < 10:
    if is_prime(num):
        prime_numbers.append(num)
        count += 1
    num += 1

print(','.join(map(str, prime_numbers)))


# Solution II
counter = 0
number = 2
prime = []

while counter < 10:
    for i in range(2, number):
        if number % i == 0:
            break
    else:
        prime.append(str(number))
        counter += 1
    number += 1

print(','.join(prime))
