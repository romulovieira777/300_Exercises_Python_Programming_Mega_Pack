"""
Exercise No. 27

From the following text:

    string = "1 0 0 1 0 1"

remove spaces using slicing. Then convert the result to decimal notation and print to the console as show below.

Expected result:

    Number found: 37
"""
# Solution I
string = "1 0 0 1 0 1"
string = string.replace(" ", "")
print("Number found:", int(string, 2))


# Solution II
string = '1 0 0 1 0 1'
binary = string[::2]
number = int(binary, 2)
print(f'Number found: {number}')
