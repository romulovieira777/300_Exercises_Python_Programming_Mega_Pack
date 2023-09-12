"""
Exercise No. 88

Write a program that finds all two-digit numbers divisible by 11 and indivisible by 3 (use a for loop). Print the result
to the console as comma-separated values as shown below.

Expected result:

    11,22,44,55,77,88
"""
# Solution I
divisible_by_11 = []

for num in range(10, 100):
    if num % 11 == 0 and num % 3 != 0:
        divisible_by_11.append(num)

result_str = ','.join(map(str, divisible_by_11))

print(result_str)


# Solution II
result = []

for num in range(10, 100):
    if num % 11 == 0 and num % 3 != 0:
        result.append(str(num))

print(','.join(result))
