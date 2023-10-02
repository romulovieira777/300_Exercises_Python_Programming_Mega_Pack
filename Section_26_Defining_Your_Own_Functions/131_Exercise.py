"""
Exercise No. 131

Implement a function called factorial() that calculates the factorial for a given number.

Example:

    [IN]: factorial(6)
    [OUT]: 720

    [IN]: factorial(10)
    [OUT]: 3628800

Note! You only need to define the function.
"""
# Solution I


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print(factorial(6))
print(factorial(10))


# Solution II
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(6))
print(factorial(10))
