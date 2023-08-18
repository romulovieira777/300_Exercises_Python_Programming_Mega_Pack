"""
Exercise No. 36

The following codes are given:

    code1 = 'FVNISJND-20'
    code2 = 'FVNISJND20'

Using the appropriate method, check whether the codes consist only of alphanumeric (numbers + letters). Print the result
to the console as shown below.

Expected result:

    code1: False
    code2: True
"""
code1 = 'FVNISJND-20'
code2 = 'FVNISJND20'

print(f"code1: {code1.isalnum()}")
print(f"code2: {code2.isalnum()}")
