"""
Exercise No. 182

Using the random built-in module set the random seed as follows:

    random.seed(15)

And shuffle (pseudo-randomly) items in the following list:

    items = ['python', 'java', 'sql', 'c++', 'c']

In response, print the list to the console.

Expected result:

    ['c', 'c++', 'sql', 'python', 'java']
"""
import random


random.seed(15)

items = ['python', 'java', 'sql', 'c++', 'c']

random.shuffle(items)

print(items)
