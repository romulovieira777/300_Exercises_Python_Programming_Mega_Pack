"""
Exercise No. 201

Implement a function called count_none() that counts all missing values in the list.

Example:

    [IN]: count_none([1, None, None, 5, None, 2])
    [OUT]: 3

Note: You only need to implement this function.
"""
# Solution I


def count_none(array):
    return array.count(None)


print(count_none([1, None, None, 5, None, 2]))


# Solution II
def count_none(array):
    counter = 0
    for item in array:
        if not item:
            counter += 1
    return counter


print(count_none([1, None, None, 5, None, 2]))
