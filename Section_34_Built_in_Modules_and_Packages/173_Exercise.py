"""
Exercise No. 173

Using the datetime built-in module, calculate the difference for dates (date 2 - date 1):

    - date 1: 2020-06-01
    - date 2: 2020-07-18

Print the result to the console as shown below.

Expected result:

    47 days, 0:00:00
"""
import datetime

date1 = datetime.date(2020, 6, 1)
date2 = datetime.date(2020, 7, 18)

date_difference = date2 - date1

print(date_difference)
