"""
Exercise No. 105

Using the while loop. calculate how many years you have to wait for the return on the investment describe below to at
least double your money (we only take into account the full periods).

Description:

    n - number of periods (in years)
    pv - present value
    r - interest rate (annual)
    fv - future value

Investment parameters:

    pv = 1000
    r = 0.04

Print result to the console as shown below.

Expected result:

    Future value: 2025.82 USD. Number of periods: 18 years
"""
# Solution I
pv = 1000
r = 0.04
n = 0
fv = pv * (1 + r) ** n

while fv < 2000:
    n += 1
    fv = pv * (1 + r) ** n

print(f"Future value: {fv:.2f} USD. Number of periods: {n} years")


# Solution II
n = 1
pv = 1000
r = 0.04
fv = pv * (1 + r)

while fv <= 2000:
    fv = fv * (1 + r)
    n += 1
print(f'Future value: {fv:.2f} USD. Number of periods: {n} years')
