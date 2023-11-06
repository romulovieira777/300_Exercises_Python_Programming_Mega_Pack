"""
Exercise No. 191

Foe any:

    x = [x1, x2, ..., xn] e R^
    y = [y1, y2, ..., yn] e R^

We define the Euclidean distance by the formula:

    d(x, y) = sqrt((x1 - y1)^2)

Implement a function called euclidean_distance() that computes the distance between two points.

Example:

    [IN]: euclidean_distance([0, 3], [4, 0])
    [OUT]: 5.0

Note: You only need to implement this function.
"""
# Solution I
from math import sqrt


def euclidean_distance(x, y):
    return round(sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2), 1)


print(euclidean_distance([0, 3], [4, 0]))


# Solution II
def euclidean_distance(x, y):
    squared_diff = [(i - j) ** 2 for i, j in zip(x, y)]
    return (sum(squared_diff)) ** 0.5


print(euclidean_distance([0, 3], [4, 0]))
