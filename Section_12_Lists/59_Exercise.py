"""
Exercise No. 59

The following list is given:

    idx = ['001', '002', '001', '003', '001']

Using the appropriate method count the occurrences of '001'. Print the result to the console as shown below.

Expected result:

    Number of occurrences: 3
"""
# Solution I
idx = ['001', '002', '001', '003', '001']
cont = idx.count('001')

print(f'Number of occurrences: {cont}')


# Solution II
idx = ['001', '002', '001', '003', '001']

print(f"Number of occurrences: {idx.count('001')}")
