"""
Exercise No. 176

Using the built-in module for regular expressions, find all email addresses in the following text:

    raw_text = "Send an email to info@template.com or sales-info@template.it"

Print the result to the console.

Tip: Use the findall() function and the regular expression '[\w\.-]+@[\w\.-]+'

Expected result:

    ['info@template.com', 'sales-info@template.it']
"""
import re

raw_text = "Send an email to info@template.com or sales-info@template.it"

result = re.findall(pattern="[\w\.-]+@[\w\.-]+", string=raw_text)

print(result)
