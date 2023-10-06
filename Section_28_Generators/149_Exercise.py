"""
Exercise No. 149

Implement a generator called enum() that works just like the enumerate() built-in function.

For simplicity, the function gets an iterable object and returns a tuple (index, element).

Example:

    [IN]: list(enum(['TEN', 'CDR', 'BBT']))
    [OUT]: [(0, 'TEN'), (1, 'CDR'), (2, 'BBT')]

Note! All you have to do is define a generator.
"""
# Solution I


def enum(iterable):
    for i, item in enumerate(iterable):
        yield i, item


print(list(enum(['TEN', 'CDR', 'BBT'])))


# Solution II
def enum(items):
    idx = 0
    for item in items:
        yield idx, item
        idx += 1


print(list(enum(['TEN', 'CDR', 'BBT'])))
