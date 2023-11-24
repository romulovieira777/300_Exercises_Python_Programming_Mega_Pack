"""
Exercise No. 215

Consider a simple number compression algorithm that works as follows:

    111155522500 -> '14_53_22_51_02'

The algorithm goes from left to right through the number and returns an object of type str. Each encountered digit is
stored along with the number of times that digit repeats until another digit is encountered in the number. Each such
pair is separated by the '_' character.

Implement a function called compress() that compresses number as described above.

Examples:

    [IN]: compress(100000)
    [OUT]: '11_05'

    [IN]: compress(9993330)
    [OUT]: '93_33_01'

    [IN]: compress(6540000)
    [OUT]: '61_51_41_04'

Tip: You can use the itertools built-in module and the groupby class in your solution.

You just need to implement the function. The  tests run several test cases to validate the solution.
"""
# Solution I


def compress(number):
    from itertools import groupby
    return '_'.join([f'{key}{len(list(group))}' for key, group in groupby(str(number))])


print(compress(100000))
print(compress(9993330))
print(compress(6540000))


# Solution II
from itertools import groupby


def compress(number):
    result = []
    for key, group in groupby(str(number)):
        result.append((key, str(len(list(group)))))
    result = [''.join(item) for item in result]
    return '_'.join(result)


print(compress(100000))
print(compress(9993330))
print(compress(6540000))


# Solution III
from itertools import groupby


def compress(number):
    result = [
        ''.join((key, str(len(list(group)))))
        for key, group in groupby(str(number))
    ]
    return '_'.join(result)


print(compress(100000))
print(compress(9993330))
print(compress(6540000))
