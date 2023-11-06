"""
Exercise No. 190

Implement a function called transfer_zeros() which takes the list as an argument and return list with all zeros at the
end.

Example:

    [IN]: transfer_zeros([3, 4, 0, 2, 0, 5, 1, 6, 2])
    [OUT]: [3, 4, 2, 5, 1, 6, 2, 0, 0]

Note: You only need to implement this function.
"""
# Solution I
items = [3, 4, 0, 2, 0, 5, 1, 6, 2]


def transfer_zeros(items):
    result = []
    for i in items:
        if i != 0:
            result.append(i)
    for i in items:
        if i == 0:
            result.append(i)
    return result


print(transfer_zeros(items))


# Solution II
def transfer_zeros(items):
    result = []
    counter = 0
    for item in items:
        if item == 0:
            counter += 1
        else:
            result.append(item)
    result.extend([0] * counter)
    return result


print(transfer_zeros(items))
