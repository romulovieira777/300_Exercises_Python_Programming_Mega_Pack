"""
Exercise No. 219

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

Part of a class named Matrix implemented:

    class Matrix:
        '''Simple Matrix class.'''

    def __init__(self, string):
        self.matrix = [
            [int(i) for i in row.split()]
            for row in string.splitlines()
        ]

Add an implementation of the __repr__() method to the Matrix class that is a formal representation of a matrix object.

Example:

    [IN]: m1 = Matrix('4 5\n8 6')
    [IN]: m1.__repr__()
    '4 5\n8 6'

Example:

    [IN]: m1 = Matrix('4 5\n8 6')
    [IN]: print(m1.__repr__())
    4 5
    8 6

You only need to implement the __repr__() method. The tests run several test cases to validate the solution.
"""


class Matrix:
    """Simple Matrix class."""

    def __init__(self, string):
        self.matrix = [
            [int(i) for i in row.split()]
            for row in string.splitlines()
        ]

    def __repr__(self):
        return '\n'.join([' '.join([str(i) for i in row]) for row in self.matrix])


m1 = Matrix('4 5\n8 6')
print(m1.__repr__())
print(m1)
print(repr(m1))
print(str(m1))
