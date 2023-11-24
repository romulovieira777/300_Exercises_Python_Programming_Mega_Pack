"""
Exercise No. 212

Consider the palindromic numbers. A palindromic or symmetric number is a number that does not change when you write its
digits in reverse order.

Some examples of palindromic numbers:

    - 363
    - 2882
    - 29492

Implement a function called is_palindrome() that checks if the passed number is palindromic decimal and binary.

For example, the number 99 is a palindromic number and its binary notation 1100011 is also a palindromic. When these
conditions are met, the function returns True, otherwise False.

Example:

    [IN]: is_palindrome(99)
    [OUT]: True

You just need to implement the function. The tests run several test cases to validate the solution.
"""
# Solution I


def is_palindrome(number):
    if str(number) == str(number)[::-1] and bin(number)[2:] == bin(number)[2:][::-1]:
        return True
    return False


print(is_palindrome(99))


# Solution II
def is_palindrome(number):
    if str(number) != str(number)[::-1]:
        return False
    bin_number = bin(number)[2:]
    return bin_number == bin_number[::-1]


print(is_palindrome(99))
