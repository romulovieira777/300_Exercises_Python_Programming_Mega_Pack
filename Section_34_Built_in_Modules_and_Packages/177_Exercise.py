"""
Exercise No. 177

Using the built-in module for regular expressions, split the following text by whitespace (spaces):

    text = "Programing in Python - from A to Z"

Print the result to the console.

Tip: Use the re.split() function and the regular expression '\s+'.

Expected result:

    ['Programing', 'in', 'Python', '-', 'from', 'A', 'to', 'Z']
"""
import re

text = "Programing in Python - from A to Z"

result = re.split(pattern="\s+", string=text)

print(result)
