"""
Exercise No. 17

The quadratic equation is given with the following formula:

    x2 + 5x + 4 = 0

Using Vieta's formulas calculate the sum and product of the roots of this quadratic equation. Print the result to the
console as shown below.

Expected result:

    x1 + x2 = -5.0
    x1x2 = 4.0
"""
a = 1
b = 5
c = 4

x1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
x2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

print(f"x1 + x2 = {x1 + x2}")
print(f"x1x2 = {x1 * x2}")
