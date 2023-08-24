"""
Exercise No. 51

Two following tuples are given:

    dji1 = ('AAPL.US', 'IBM.US', 'MSFT.US')
    dji2 = ('HD.US', 'GS.US', 'KIKE.US')

Combine these tuples into one as shown below and print the result to the console.

Expected result:

    ('AAPL.US', 'IBM.US', 'MSFT.US', 'HD.US', 'GS.US', 'KIKE.US')
"""
dji1 = ('AAPL.US', 'IBM.US', 'MSFT.US')
dji2 = ('HD.US', 'GS.US', 'KIKE.US')
result = dji1 + dji2
print(result)
