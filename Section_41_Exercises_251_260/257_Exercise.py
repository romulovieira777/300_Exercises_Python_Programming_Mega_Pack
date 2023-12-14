"""
Exercise No. 257

Monte Carlo methods are a broad class of computational algorithms that rely on repeated random sampling to obtain
numerical results. The underlying concept is to use randomness to solve problems that might be deterministic in
principle. They are often used in physical and mathematical problems and are most useful when it is difficult or
impossible to use other approaches.

Let's use the Monte Carlo method to approximate Pi. Consider the coordinate system in R^2 space and a circle with a
radius of 1 centered (0, 0). The area of the circle is equal to Pi. Let's add a square on this circle with vertices at
(1, 1), (1, -1), (-1, -1), (-1, 1). The side of this square is equal to 2 and its area is equal to 4.

Our task is to draw points from the given square according to the uniform distribution and check whether the drawn point
falls into the circle. The probability of such an event is equal to the area of the circle with radius 1, which is
exactly Pi.

We choose the number of simulations freely, but basically the more simulations we run, the better the approximation of
Pi will be obtained.

The area of a circle can be calculated from the formula:

    area of the circle = area of the square * (number of points drawn inside the circle / number of all points drawn)

Since we know that the area of the circle is equal to Pi, we can substitute:

    Pi = area of the square * (number of points drawn inside the circle / number of all points drawn)

In this exercise, implement a function called generate_random_point() that generates a point with coordinates between
[-1, 1] using the uniform distribution.

Use the built-in random module in your solution.

Example:

    [IN]: generate_random_point()
    [OUT]: (-0.7682761681456314, -0.00899286964820889)

Example:

    [IN]: generate_random_point()
    [OUT]: (-0.7744055968106591, -0.7127923185103238)

You just need to implement the generate_random_point() function. The tests run several test cases to validate the
solution.
"""
import random


def generate_random_point():
    return random.uniform(-1, 1), random.uniform(-1, 1)


print(generate_random_point())
