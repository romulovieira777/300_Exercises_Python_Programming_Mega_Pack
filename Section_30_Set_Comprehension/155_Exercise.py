"""
Exercise No. 155

Calculate the probability than in three throws of symmetrical cubic dice, the sum of the squares of points will be
divisible by 3. Use set comprehension. Round the result to fourth decimal place and print the result to the console as
shown below.

Expected result:

    Probability: x.xxxx
"""
# Solution I
from itertools import product


def is_divisible_by_3(t):
    return sum([x ** 2 for x in t]) % 3 == 0


omega = {(x, y, z) for x, y, z in product(range(1, 7), repeat=3) if is_divisible_by_3((x, y, z))}
prob = round(len(omega) / 6 ** 3, 4)

print(f'Probability: {prob}')


# Solution II
omega = {
    (x, y, z)
    for x in range(1, 7)
    for y in range(1, 7)
    for z in range(1, 7)
}
a = {
    (x, y, z)
    for x, y, z in omega
    if (x**2 + y**2 + z**2) % 3 == 0
}
prob = round(len(a) / len(omega), 4)

print(f'Probability: {prob}')
