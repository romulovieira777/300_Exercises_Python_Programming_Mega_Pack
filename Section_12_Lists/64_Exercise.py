"""
Exercise No. 64

The following list is given:

    hashtags = ['summer', 'time', 'vibes']

Using the appropriate method, combine the elements of the list with the '#' character. Also add this sign to the
beginning of the text and print the result to the console as shown below.

Expected result:

    #summer#time#vibes
"""
# Solution I
hashtags = ['summer', 'time', 'vibes']
hashtags = '#'.join(hashtags)
hashtags = '#' + hashtags

print(hashtags)


# Solution II
hashtags = ['summer', 'time', 'vibes']
print('#' + '#'.join(hashtags))
