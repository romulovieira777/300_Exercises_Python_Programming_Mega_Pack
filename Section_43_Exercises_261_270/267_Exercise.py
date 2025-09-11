"""
Exercise No. 265

Class inheritance. Consider a built-in list class. One of the methods of this class is the append() method, which
appends an item at the end of the list:

    >>> help(list.append)

    Help on method_descriptor:
    append(self, object, /)
        Append object to the end of the list.

An element can be, for example, an object of class int, float, str, bool or NoneType.

By inheriting from a list class create a class named IntList that allows you to append only int objects with the
 append() method. If you try to append an object of a different type raise a TypeError with the message:

    'The value must be an integer.'

Example:

    [IN]: integers = IntList()
    [IN]: integers.append(3)
    [IN]: integers.append(40)
    [IN]: print(integers)
    [OUT]: [3, 40]

Example:

    [IN]: integers.append('sql')
    [OUT]: TypeError: The value must be an integer.

You only need to implement the IntList class. The tests run several test cases to validate the solution.
"""


class IntList(list):

    def append(self, item):
        if not isinstance(item, int):
            raise TypeError('The value must be an integer.')
        super().append(item)


# Example usage:
integers = IntList()
integers.append(3)
integers.append(40)
print(integers)  # Output: [3, 40]

try:
    integers.append('sql')  # This will raise a TypeError
except TypeError as e:
    print(e)    # Output: TypeError: The value must be an integer.


# Solution from the platform
class IntList(list):

    def append(self, value):
        if not isinstance(value, int):
            raise TypeError('The value must be an integer.')
        return list.append(self, value)


# Example usage:
integers = IntList()
integers.append(3)
integers.append(40)
print(integers)  # Output: [3, 40]
