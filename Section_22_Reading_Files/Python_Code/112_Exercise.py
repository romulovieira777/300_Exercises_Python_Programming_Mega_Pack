"""
Exercise No. 112

Read the currencies.txt file. Each line has a different currency pair. Create a list with the names of currency paits
containing the 'USD' symbol.

Expected result:

    ['ARSUSD', 'AUDUSD']
"""
# Solution I
with open('..\Data\currencies.txt', 'r') as file:
    lines = file.read().splitlines()

usd = []

for line in lines:
    if 'USD' in line:
        usd.append(line)

print(usd)


# Solution II
with open('..\Data\currencies.txt', 'r') as file:
     lines = file.read().splitlines()

indexes = [index for index in lines if 'USD' in index]

print(indexes)
