"""
Exercise No. 21

Calculate the geometric mean of the following numbers: 4, 3, 4.5, 5 and print result to the console as shown below.

Expected result:

    Geometric average of the given numbers: 4.05
"""
# Solution I
a = 4
b = 3
c = 4.5
d = 5

geometric_mean = (a * b * c * d) ** (1 / 4)

print(f'Geometric average of the given numbers: {geometric_mean:.2f}')

# Solution II
x1, x2, x3, x4 = 4, 3, 4.5, 5

geo = (x1 * x2 * x3 * x4) ** (1 / 4)

print(f'Geometric average of the given numbers: {geo:.2f}')
