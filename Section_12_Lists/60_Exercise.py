"""
Exercise No. 60

The following text is given:

    text = 'Python programming'

Standardize the text (replace uppercase letters with lowercase). Then create a list of unique characters in the text.
Remove the space from this list and sort from a to z. After all print the list to the console.

Tip: You can use a set to generate unique characters.

Expected result:

    ['a', 'g', 'h', 'i', 'm', 'n', 'o', 'p', 'r', 't', 'y']
"""
# Solution I
text = 'Python programming'
text = text.lower()
text = set(text)
text.remove(' ')
text = list(text)
text.sort()

print(text)


# Solution II
text = 'Python programming'
text = text.lower()
characters = list(set(text))
characters.remove(' ')
characters.sort()

print(characters)
