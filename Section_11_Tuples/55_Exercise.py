"""
Exercise No. 55

Sort the given tuple (from A to Z):

    names = ('Monica', 'Tom', 'John', 'Michael')

Print the sorted tuple to the console as shown below.

Expected result:

    ('John', 'Michael', 'Monica', 'Tom')
"""
names = ('Monica', 'Tom', 'John', 'Michael')
sorted_names = tuple(sorted(names))

print(sorted_names)
