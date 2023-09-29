"""
Exercise No. 127

Implement a function called maximum() that returns the maximum of three numbers. Use conditional expression.

Example:

    [IN]: maximum(4, 2, 1)
    [OUT]: 4

    [IN]: maximum(-3, 2, 5)
    [OUT]: 5

Note! You only need to define the function.
"""
# Solution I


def maximum(a, b, c):
    return a if a >= b and a >= c else b if b >= a and b >= c else c


print(maximum(4, 2, 1))
print(maximum(-3, 2, 5))


# Solution II
def maximum(x, y, z):
    if x >= y and x >= z:
        return x
    elif y >= z:
        return y
    else:
        return z


print(maximum(4, 2, 1))
print(maximum(-3, 2, 5))
