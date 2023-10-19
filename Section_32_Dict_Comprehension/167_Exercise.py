"""
Exercise No. 167

The following dictionary is given:

    stocks = {'Boombit': 22, 'CD Projekt': 295, 'Playway': 350}

Using dict comprehension, extract a key: value pair from the dictionary with a value greater than 100 and print the
result to the console.

Expected result:

    {'CD Projekt': 295, 'Playway': 350}
"""
stocks = {'Boombit': 22, 'CD Projekt': 295, 'Playway': 350}

data = {key: value for key, value in stocks.items() if value > 100}

print(data)
