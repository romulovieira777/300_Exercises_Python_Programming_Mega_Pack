"""
Exercise No. 102

The list of companies from the WIG.GAMES index is given with the closing price and currency:

    gaming = {
        '11B': [362.5, 'PLN'],
        'CDR': [74.25, 'USD'],
        'CIG': [0.85, 'PLN'],
        'PLW': [79.5, 'USD'],
        'TEN': [300.0, 'PLN']
    }

Using the continue statement, create a for loop that will change the closing price from USD to PLN in this dictionary.
Take USDPLN = 4.0.

In response, print the gaming dictionary to the console.

Expected result:

    {'11B': [362.5, 'PLN'], 'CDR': [297.0, 'PLN'], 'CIG': [0.85, 'PLN'], 'PLW': [318.0, 'PLN'], 'TEN': [300.0, 'PLN']}
"""
# Solution I
gaming = {
    '11B': [362.5, 'PLN'],
    'CDR': [74.25, 'USD'],
    'CIG': [0.85, 'PLN'],
    'PLW': [79.5, 'USD'],
    'TEN': [300.0, 'PLN']
}

for key, value in gaming.items():
    if value[1] == 'USD':
        value[0] *= 4
        value[1] = 'PLN'
    else:
        continue

print(gaming)


# Solution II
gaming = {
    '11B': [362.5, 'PLN'],
    'CDR': [74.25, 'USD'],
    'CIG': [0.85, 'PLN'],
    'PLW': [79.5, 'USD'],
    'TEN': [300.0, 'PLN']
}

for ticker, info in gaming.items():
    if info[1] == 'PLN':
        continue
    info[0] = info[0] * 4.0
    info[1] = 'PLN'

print(gaming)
