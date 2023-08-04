"""
Exercise No. 19

Calculate the distance of two points A = (3, 2), B = (-1, -1) and print result to the console as shown below.

Expected result:

    The distance between points A and B: 5.0
"""
x1 = 3
y1 = 2
x2 = -1
y2 = -1

d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print(f"The distance between points A and B: {d:.1f}")
