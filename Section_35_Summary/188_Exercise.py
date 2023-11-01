"""
Exercise No. 188

Implement a function called relu() (ReLU - Rectified Linear Unit). This function is used in neural networks and is given
by the following formula:

    x e R

    f(x) = max(x, 0)

Note: You only need to implement this function.
"""
# Solution I


def relu(x):
    return max(x, 0)


print(relu(-5))
