"""
Exercise No. 77

The following dictionary is given:

    stats = {
        'site': 'e-smartdata.org',
        'traffic': 100,
        'type': 'organic'
    }

Delete the 'traffic' key pair form this dictionary and print it to the console.

Expected result:

    {'site': 'e-smartdata.org', 'type': 'organic'}
"""
# Solution I
stats = {
    'site': 'e-smartdata.org',
    'traffic': 100,
    'type': 'organic'
}

stats.pop('traffic')
print(stats)


# Solution II
stats = {
    'site': 'e-smartdata.org',
    'traffic': 100,
    'type': 'organic'
}

del stats['traffic']
print(stats)
