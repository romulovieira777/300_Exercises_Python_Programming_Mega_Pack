"""
Exercise No. 125

Count the number of ones in the binary representation of the number:

    number = 234

Print the result to the console.

Tip: Use bin() built-in functions.

Expected result:

    5
"""
# Solution I
number = 234

print(bin(number).count('1'))


# Solution II
number = 234
binary = bin(number)
binary = binary[2:]

print(binary.count('1'))
