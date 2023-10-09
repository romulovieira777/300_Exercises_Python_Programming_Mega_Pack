"""
Exercise No. 151

Consider the two-roll of the dice. Create the probability space (omega) and count the probability of getting a sum of
points higher than 10. Use set comprehension.

Expected result:

    Probability: 0.08
"""
# Solution I
from itertools import product

omega = {pair for pair in product(range(1, 7), repeat=2) if sum(pair) > 10}

print(f'Probability: {len(omega) / 36:.2f}')


# Solution II
omega = {(i, j) for i in range(1, 7) for j in range(1, 7)}
sum_gt_10 = {pair for pair in omega if pair[0] + pair[1] > 10}

print(f'Probability: {len(sum_gt_10) / len(omega):.2f}')
