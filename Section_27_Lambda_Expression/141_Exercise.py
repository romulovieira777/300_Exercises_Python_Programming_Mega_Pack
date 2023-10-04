"""
Exercise No. 141

The func_1() function is defined below:

    def func_1(x, y):
        return x + y + 2

Using the lambda expression, define an analogous function and assign it to the variable func_2.
"""


def func_1(x, y):
    return x + y + 2


func_2 = lambda x, y: x + y + 2

print(func_1(2, 3))
print(func_2(2, 3))
