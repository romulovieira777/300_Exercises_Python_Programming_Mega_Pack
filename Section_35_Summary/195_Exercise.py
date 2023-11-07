"""
Exercise No. 195

Implement a function called fill_value() that returns a two-dimensional array of height x width and fills it with a
fixed value.

Arguments:

    - height: natural number, height of the array
    - width: natural number, width of the array
    - value: the value to fill the array

Example:

    [IN]: fill_value(height=2, width=3, value=255)
    [OUT]: [[255, 255, 255], [255, 255, 255]]

    [IN]: fill_value(4, 2, 'a')
    [OUT]: [['a', 'a'], ['a', 'a'], ['a', 'a'], ['a', 'a']]

Note: You only need to implement this function.
"""
# Solution I


def fill_value(height, width, value):
    return [[value] * width for _ in range(height)]


print(fill_value(height=2, width=3, value=255))
print(fill_value(4, 2, 'a'))
