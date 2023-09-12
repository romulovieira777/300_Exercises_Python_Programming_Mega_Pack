"""
Exercise No. 87

Write a program that finds all two-digit numbers divisible by 11 (use a for loop). Print the result to the console as
comma-separated values as shown below.

Expected result:

    11,22,33,44,55,66,77,88,99
"""
# Solution I
divisible_by_11 = []

for num in range(10, 100):
    if num % 11 == 0:
        divisible_by_11.append(num)

result_str = ','.join(map(str, divisible_by_11))

print(result_str)


# Solution II
result = []

for num in range(10, 100):
    if num % 11 == 0:
        result.append(str(num))

print(','.join(result))
