"""
Exercise No. 04

Create two variables (you can freely choose names) and assign to them following values:

    - 'Python'
    - '3.8'

Using these variables and the print() function, print to the console the following text:

    I am learning Python version 3.8
"""
language = "Python"
version = "3.8"

print("I am learning", language, "version", version + ".")
print("I am learning " + language + " version " + version + ".")
print("I am learning {} version {}.".format(language, version))
print(f"I am learning {language} version {version}")
