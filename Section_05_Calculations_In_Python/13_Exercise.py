"""
Exercise No. 13

Write a program that calculates the future value of 1000 USD with an annual interest rate of 3%, annual capitalization
and a 5-year investment period. Round the result to the nearest cent.

Tip: Use compound capitalization of interest.

Print the result to the console as shown below.

Expected result:

    The future value of the investment: 1159.27 USD
"""
# Solution I
value = 1000
interest_rate = 0.03
capitalization = 1
investment_period = 5

future_value = value * (1 + interest_rate / capitalization) ** (capitalization * investment_period)

print(f"The future value of the investment: {future_value:.2f} USD")


# Solution II
pv = 1000
r = 0.03
n = 5
fv = pv * (1 + r) ** n

print(f"The future value of the investment: {fv:.2f} USD")
