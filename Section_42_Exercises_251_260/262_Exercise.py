"""
Exercise No. 262

Binary number system is a positional numeral system employing 2 as the base and so requiring only two different symbols
for its digits, 0 and 1, instead of the usual 10 different symbols needed in the decimal system. The numbers from 0 to
10 are thus in binary 0, 1, 10, 11, 100, 101, 110, 111, 1000, 1001 and 1010.

For example, the number 10 in binary can be represented as 1010 because:

    1 * 2^3 + 0 * 2^2 + 1 * 2^1 + 0 * 2^0 = 8 + 0 + 2 + 0 = 10

A function called decimal_to_binary() that converts a number from decimal to binary has been implemented:

    def decimal_to_binary(number: int) -> str:
        if number == 0:
            return "0"
        result = ""
        while number > 0:
            result += str(number % 2)
            number = number //= 2
        return result[::-1]

Now consider a bitwise AND operation on binary numbers. The operation is
"""