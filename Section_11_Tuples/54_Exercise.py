"""
Exercise No. 54

The following tuple is geiven:

    default = ('YES', 'NO', 'NO', 'YES', 'NO')

Using the appropriate method return the number of occurrences of the string 'YES' and print the result to the console as
shown below.

Expected result:

    Number of occurrences: 2
"""
default = ('YES', 'NO', 'NO', 'YES', 'NO')
cont = default.count('YES')

print(f'Number of occurrences: {cont}')
