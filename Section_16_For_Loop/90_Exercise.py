"""
Exercise No. 90

The following list is given:

    items = [1, 5, 3, 2, 2, 4, 2, 4]

Write a program that removes duplicates from the list (the order must be kept) and print the list to the console.

Expected result:

    [1, 5, 3, 2, 4]
"""
# Solution I
items = [1, 5, 3, 2, 2, 4, 2, 4]
result = []

for num in items:
    if num not in result:
        result.append(num)

print(result)
