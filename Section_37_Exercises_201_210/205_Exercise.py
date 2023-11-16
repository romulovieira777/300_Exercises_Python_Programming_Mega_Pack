"""
Exercise No. 205

In number theory, integer factorization is the decomposition of a composite number into a product of smaller integers.
If these factors are further restricted to prime numbers, the process is called prime factorization.

Examples of prime numbers: 2, 3, 5, 7, 11, 13, 17, 19, ...

Reminder: The number 1 is no a prime number.

A number that is greater than 1 and is not prime is called a composite number.

Examples of composite numbers: 4, 6, 8, 9, 10, 12, 14, 15, 16, ...

We can break down a composite number into prime factors. For example:

    - 15 = 3 * 5
    - 36 = 2 * 2 * 3 * 3
    - 48 = 2 * 2 * 2 * 2 * 3

Implement a function that takes a natural number as an argument and returns a list containing the prime factorization of
that number. Present the solution in the form of a function called calculate().

Example:

    [IN]: calculate(48)
    [OUT]: [2, 2, 2, 2, 3]

You just need to implement the function. The tests run several test cases to validate the solution.
"""
# Solution I


def calculate(number):
    factors = []
    divisor = 2
    while number > 1:
        while number % divisor == 0:
            factors.append(divisor)
            number /= divisor
        divisor += 1
    return factors


print(calculate(48))


# Solution II
def calculate(number):
    i = 2
    factors = []
    while i * i <= number:
        if not number % i == 0:
            i += 1
        else:
            number = number // i
            factors.append(i)
    if number > 1:
        factors.append(number)
    return factors


print(calculate(48))
