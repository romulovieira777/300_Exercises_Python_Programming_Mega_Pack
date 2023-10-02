"""
Exercise no. 134

Implement a function count_str(), which returns the number of str objects with a length more than 2 characters from an
iterable object (list, tuple, set).

Example:

    [IN]: count_str([1, '#hello', '', 'python', 'go'])
    [OUT]: 2

    [IN]: count_str([1, 2, 3, 'python'])
    [OUT]: 1

Note! You only need to define the function.
"""
# Solution I


def count_str(iterable):
    return sum(isinstance(i, str) and len(i) > 2 for i in iterable)


print(count_str([1, '#hello', '', 'python', 'go']))
print(count_str([1, 2, 3, 'python']))


# Solution II
def count_str(items):
    total = 0
    for item in items:
        if isinstance(item, str):
            if len(item) > 2:
                total += 1
    return total


print(count_str([1, '#hello', '', 'python', 'go']))
print(count_str([1, 2, 3, 'python']))
