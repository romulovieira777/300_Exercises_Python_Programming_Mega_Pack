"""
Exercise No. 71

The following dictionary is given:

    stocks = {
        'MSFT.US': {'Microsoft Corp': 184},
        'AAPL.US': {'Apple Inc': 310},
        'MMM.US': {'3M Co': 148},
    }

Get the price for Microsoft (value for the 'Microsoft Corp' key) and print it to the console.

Expected result:

    184
"""
stocks = {
    'MSFT.US': {'Microsoft Corp': 184},
    'AAPL.US': {'Apple Inc': 310},
    'MMM.US': {'3M Co': 148},
}

print(stocks.get('MSFT.US').get('Microsoft Corp'))
print(stocks['MSFT.US']['Microsoft Corp'])
