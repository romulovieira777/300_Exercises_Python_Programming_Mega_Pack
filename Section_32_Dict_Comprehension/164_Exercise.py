"""
Exercise No. 164

Using dict comprehension, create a dictionary that maps the numbers 1 to 7 into squares and print the result to the
console.

Expected result:

    {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}
"""
data = {number: number ** 2 for number in range(1, 8)}

print(data)
