"""
Exercise No. 89

The following list of numbers is given:

    items = [1, 3, 4, 5, 6, 9, 10, 17, 23, 24]

Write a program that removes odd numbers and returns the remaining ones. Print the result to the console.

Expected result:

    [4, 6, 10, 24]
"""
# Solution I
items = [1, 3, 4, 5, 6, 9, 10, 17, 23, 24]
even_numbers = []

for num in items:
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)


# Solution II
items = [1, 3, 4, 5, 6, 9, 10, 17, 23, 24]
even_numbers = []

for num in items:
    if not num % 2 != 0:
        even_numbers.append(num)

print(even_numbers)
