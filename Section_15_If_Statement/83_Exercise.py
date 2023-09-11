"""
Exercise No. 83

The following password is given:

    password = 'cskdnjcasa#!'

Check if the password has at least 11 characters and contains the special character '!'.:cvar

If so, print 'Password correct', otherwise 'Password incorrect'.

Expected result:

    Password correct
"""
password = 'cskdnjcasa#!'

if len(password) >= 11 and '!' in password:
    print('Password correct')
else:
    print('Password incorrect')
