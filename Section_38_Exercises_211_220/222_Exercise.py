"""
Exercise No. 222

Let's consider vectors consisting of only ones and zeros. Let us also assume an additional convention for representing
such a vector. For example, a vector:

    u = [0, 1, 1, 0, 1, 0, 1, 0]

we will present as a sequence:

    '01101010'

For the vectors so defined, we can determine the Hamming distance. The Hamming distance of vectors u and v is the number
of elements where the vectors u and v are different.

Example: The Hamming distance of the vectors '1100100', '1010000' is equal to 3.

Implement a function called hamming_distance() that returns the Hamming distance of two vectors. To calculate the
Hamming distance, the vectors must be of the same length. If the vectors are of different lengths raise the ValueError
with the following message:

'Both vectors must be the same length.'

Example:

    [IN]: hamming_distance('01101010', '11011011')
    [OUT]: 4

Example:

    [IN]: hamming_distance('110', '10100')
    [OUT]: ValueError: Both vectors must be the same length.

You just need to implement the hamming_distance() function. The tests run several test cases to validate the solution.
"""
# Solution I


def hamming_distance(u, v):
    if len(u) != len(v):
        raise ValueError('Both vectors must be the same length.')
    return sum([1 for i, j in zip(u, v) if i != j])


print(hamming_distance('01101010', '11011011'))


# Solution II
def hamming_distance(u, v):
    if len(u) != len(v):
        raise ValueError('Both vectors must be the same length.')
    distance = 0
    for i in range(len(u)):
        if u[i] != v[i]:
            distance += 1
    return distance


print(hamming_distance('01101010', '11011011'))
