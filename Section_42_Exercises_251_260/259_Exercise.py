"""
Exercise No. 259

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

A function called generate_random_point() has been implemented, which generates a point with coordinates between [-1, 1]
according to the uniform distribution. And we also have the is_in_unit_circle() function.

Random seed is set to 10. Implement the estimate() function which takes the number of simulations as an argument and
returns the approximate value of Pi based on the Monte Carlo method.

Example:

    [IN]: estimate(10000)
    [OUT]: 3.1528

You just need to implement the estimate() function. The tests run several test cases to validate the solution.
"""
# Solution I
import random


random.seed(10)


def generate_random_point():
    return random.uniform(-1, 1), random.uniform(-1, 1)


def is_in_unit_circle(point):
    return point[0] ** 2 + point[1] ** 2 <= 1


def estimate(n):
    points = [generate_random_point() for _ in range(n)]
    flags = [is_in_unit_circle(point) for point in points]
    return 4 * flags.count(True) / len(flags)


print(estimate(10000))


# Solution II
import random


random.seed(10)


def generate_random_point():
    return random.uniform(-1, 1), random.uniform(-1, 1)


def is_in_unit_circle(point):
    return point[0] ** 2 + point[1] ** 2 <= 1


def estimate(simulations):
    points_in_circle = 0

    for _ in range(simulations):
        point = generate_random_point()

        if is_in_unit_circle(point):
            points_in_circle += 1

    result = 4 * points_in_circle / simulations
    return result


print(estimate(10000))
