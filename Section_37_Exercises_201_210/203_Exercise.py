"""
Exercise No. 203

All natural numbers divisible by 5 or 7 less than 20 are: [0, 5, 7, 10, 14, 15]. The sum of these numbers is: 51. In
this exercise, we treat zero as a natural number.

Find the sum of all numbers that are divisible by 5 or 7 less than 100.

Present the solution in the form of a function called calculate(). In response, call calculate() function and print the
result to the console.

Expected result:

    1580
"""
# Solution I


def calculate():
    return sum([i for i in range(100) if i % 5 == 0 or i % 7 == 0])


print(calculate())


# Solution II
def calculate():
    numbers = []
    for i in range(100):
        if i % 5 == 0 or i % 7 == 0:
            numbers.append(i)
    total = sum(numbers)
    return total


print(calculate())
