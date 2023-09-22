"""
Exercise No. 111

Write a program that reads playway.txt file containing Playway stock data, and then calculates the average closing price
(3-day average).

Print the result to the console as shown below.

Expected result:

    3-day average closing price: xxx.xx
"""
with open('..\Data\playway.txt', 'r') as file:
     lines = file.read().splitlines()

close = []

for idx, line in enumerate(lines):
    if idx > 0:
        close.append(int(line.split(',')[-2]))

close_avg = sum(close) / len(close)
print(f'3-day average closing price: {close_avg:.2f}')
