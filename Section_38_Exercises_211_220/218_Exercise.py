"""
Exercise No. 218

Consider the problem below. We have an application in which at some point we get a matrix in the form of a string (an
object of the str type). For example, the following string:

    string = ''4 2 7
    1 5 4
    2 6 8''

represents a 3 X 3 matrix. Each row of the matrix is stored on a separate line. Each element of a row is separated from
another element by a space.

It's hard to work with these matrices and perform some additional operations. We will transform such a matrix into
nested lists:

    [[4, 2, 7], [1, 5, 4], [2, 6, 8]]

Implement a class named Matrix that takes the matrix as a string in the __init__() method and sets the value of the
instance attribute called matrix as nested lists.

Examples:

    [IN]: m = Matrix('3 4\n5 6')
    [IN]: m.matrix
    [OUT]: [[3, 4], [5, 6]]

    [IN]: m = Matrix('3 4\n5 6\n7 8')
    [IN]: m.matrix
    [OUT]: [[3, 4], [5, 6], [7, 8]]

You just need to implement the class. The tests run several test cases to validate the solution.
"""
# Solution I


class Matrix:
    def __init__(self, matrix):
        self.matrix = [[int(j) for j in i.split()] for i in matrix.split('\n')]

    def __repr__(self):
        return f'{self.__class__.__name__}({self.matrix})'

    def __str__(self):
        return f'{self.__class__.__name__}({self.matrix})'


m = Matrix('3 4\n5 6')
print(m)
print(repr(m))
print(m.matrix)


# Solution II
class Matrix:
    """Simple Matrix class."""

    def __init__(self, string):
        self.matrix = [
            [int(i) for i in row.split()]
            for row in string.splitlines()
        ]


m = Matrix('3 4\n5 6')
print(m)
print(repr(m))
print(m.matrix)
