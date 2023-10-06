"""
Exercise No. 150

Implement a generator named dayname() that accepts the index of the element from the following list:

    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

and allows us to iterate over 3 days (previous day, present day, next day).

Example:

    [IN]:
        for pair in dayname(30):
            print(pair)

    [OUT]:
        Sun
        Mon
        Tue

Note! All you have to do is define a generator.
"""
# Solution I


def dayname(idx):
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    for i in range(idx - 1, idx + 2):
        yield days[i % 7]


for pair in dayname(30):
    print(pair)


# Solution II
def dayname(index):
    index = index % 7
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    yield days[index - 1]
    yield days[index]
    yield days[(index + 1)]


for pair in dayname(30):
    print(pair)
