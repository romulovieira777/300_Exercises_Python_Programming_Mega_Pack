"""
Exercise No. 269

Class inheritance. Consider the built-in dict class. We can add key: value pairs to the dictionary, for example:

    dict[key] = value

For this purpose, the descriptor dict.__setitem__() is called. Equivalently we have:

    dict.__setitem__(key, value)

Inheriting from the dict class create a class named IntDict that allows you to add only pairs to the dictionary whose
value is an int object. Raise a TypeError with the message otherwise:

    'The value must be an integer.'

Example:

    [IN]: integers = IntDict()
    [IN]: integers['one'] = 1
    [IN]: print(integers)
    [OUT]: {'one': 1, 'two': 2}

Example:

    [IN]: integers['one'] = 'uno'
    [OUT]: TypeError: The value must be an integer.

You only need to implement the IntDict class. The tests run several test cases to validate the solution.
"""


class IntDict(dict):

    def __setitem__(self, key, value):
        if not isinstance(value, int):
            raise TypeError('The value must be an integer.')
        super().__setitem__(key, value)


if __name__ == '__main__':
    integers = IntDict()
    integers['one'] = 1
    integers['two'] = 2
    print(integers)
    try:
        integers['three'] = 'three'
    except TypeError as e:
        print(e)
    try:
        integers['four'] = 4.0
    except TypeError as e:
        print(e)
    try:
        integers['five'] = [5]
    except TypeError as e:
        print(e)
    try:
        integers['six'] = None
    except TypeError as e:
        print(e)
    try:
        integers['seven'] = (7,)
    except TypeError as e:
        print(e)
    try:
        integers['eight'] = {8}
    except TypeError as e:
        print(e)
    try:
        integers['nine'] = {'nine': 9}
    except TypeError as e:
        print(e)
    integers['ten'] = 10
    print(integers)


# Solution from the platform
class IntDict(dict):
 
    def __setitem__(self, key, value):
        if not isinstance(value, int):
            raise TypeError('The value must be an integer.')
        return dict.__setitem__(self, key, value)
