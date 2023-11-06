"""
Exercise No. 189

The following list is given:

    items = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

Implement a function called flatten(), which takes the nested list and returns the following:

    [1, 2, 3, 4, 5, 6, 7, 8, 9]

Note: You only need to implement this function.
"""
# Solution I
items = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


def flatten(items):
    result = []
    for i in items:
        for j in i:
            result.append(j)
    return result


print(flatten(items))


# Solution II
def flatten(items):
    result = []
    for item in items:
        result.extend(item)
    return result


print(flatten(items))
