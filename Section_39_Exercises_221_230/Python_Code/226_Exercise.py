"""
Exercise No. 226

Below is an example of a 3x3 square matrix of numbers in spiral order:

    [1, 2, 3]
    [8, 9, 4]
    [7, 6, 5]

An example of a 4x4 square matrix of numbers in spiral order:

    [1,  2,  3,  4]
    [12, 13, 14, 5]
    [11, 16, 15, 6]
    [10, 9,  8,  7]

We move clockwise, starting with the number 1 and increasing by 1.

Implement a function called spiral_matrix() that takes the size of the matrix as an argument and generates the matrix in
spiral order with the given size. Present the solution in the form nested lists.

Tip. You can use the itertools built-in module and the cycle class in your solution.

Example:

    [IN]: spiral_matrix(1)
    [OUT]: [[1]]

Example:

    [IN]: spiral_matrix(2)
    [OUT]: [[1, 2], [4, 3]]

Example:

    [IN]: spiral_matrix(3)
    [OUT]: [[1, 2, 3], [8, 9, 4], [7, 6, 5]]

You just need to implement the spiral_matrix() function. The tests run several test cases to validate the solution.
"""
# Solution I
from itertools import cycle


def spiral_matrix(size):
    if size < 1:
        raise ValueError('The size cannot be less than 1.')
    matrix = [[None] * size for _ in range(size)]
    directions = cycle([(0, 1), (1, 0), (0, -1), (-1, 0)])
    current_direction = next(directions)
    current_position = (0, 0)
    for i in range(1, size ** 2 + 1):
        matrix[current_position[0]][current_position[1]] = i
        next_position = (current_position[0] + current_direction[0], current_position[1] + current_direction[1])
        if not (0 <= next_position[0] < size and 0 <= next_position[1] < size) or matrix[next_position[0]][next_position[1]] is not None:
            current_direction = next(directions)
            next_position = (current_position[0] + current_direction[0], current_position[1] + current_direction[1])
        current_position = next_position
    return matrix


print(spiral_matrix(1))
print(spiral_matrix(2))
print(spiral_matrix(3))


# Solution II
def spiral_matrix(size):
    # Preparing an empty matrix
    matrix = [[None] * size for _ in range(size)]

    # Starting point
    x, y = 0, 0

    # (0, 1) represents moving right along the matrix row
    # (0, -1) represents moving left along the matrix row
    # (1, 0) represents moving down along the matrix column
    # (-1, 0) represents moving up along the matrix column
    movements = cycle(((0, 1), (1, 0), (0, -1), (-1, 0)))
    dx, dy = next(movements)

    for i in range(size**2):
        matrix[x][y] = i + 1
        xdx = x + dx
        ydy = y + dy
        if (
            not 0 <= xdx < size
            or not 0 <= ydy < size
            or matrix[xdx][ydy] is not None
        ):
            dx, dy = next(movements)
        x += dx
        y += dy
    return matrix


print(spiral_matrix(1))
print(spiral_matrix(2))
print(spiral_matrix(3))
