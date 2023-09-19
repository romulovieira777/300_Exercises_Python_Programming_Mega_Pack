"""
Exercise No. 100

The following list of hashtags is given:

    hashtags = ['holiday', 'sport', 'fit', None, 'fashion']

Check if all objects in the list are if str type. If so, print True, otherwise print False. Use the break statement in
your solution.

Expected result:

    False
"""
hashtags = ['holiday', 'sport', 'fit', None, 'fashion']

for item in hashtags:
    if not isinstance(item, str):
        print(False)
        break
else:
    print(True)
