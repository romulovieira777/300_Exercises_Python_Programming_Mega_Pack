"""
Exercise No. 126

Implement a function called maximum() that returns the maximum of two numbers. Use conditional statement.

Example:

    [IN]: maximum(4, 2)
    [OUT]: 4

    [IN]: maximum(-4, 2)
    [OUT]: 2

Note! You only need to define the function.
"""


def maximum(a, b):
    if a >= b:
        return a
    else:
        return b


print(maximum(4, 2))
print(maximum(-4, 2))
