# Evan Douglass

# This program calculates the minimum fixed monthly payment
# that will pay off a given debt in less than one year.

# initialize values
balance = 320000
annualInterestRate = 0.2


def findEndBalance(balance, monthlyRate, payment):
    '''
    balance (float or int): Original balance in account.
    monthlyRate (float): Monthly interest rate.
    payment (int or float): Monthly payment.

    returns the ending balance after 12 months as a float or int.
    '''
    test_balance = balance
    for month in range(12):
        test_balance -= payment
        test_balance += (test_balance * monthlyRate)
    return test_balance


# initial calculations
monthlyRate = annualInterestRate / 12
upper_bound = (balance * (1 + monthlyRate)**12) / 12
lower_bound = balance / 12
test = (upper_bound + lower_bound) / 2

# bisection search to find lowest payment
bal = findEndBalance(balance, monthlyRate, test)
while not(-0.01 <= bal <= 0):
    if bal < 0:
        upper_bound = test
        test = (upper_bound + lower_bound) / 2
        bal = findEndBalance(balance, monthlyRate, test)
    elif bal > 0:
        lower_bound = test
        test = (upper_bound + lower_bound) / 2
        bal = findEndBalance(balance, monthlyRate, test)

print('Lowest Payment:', round(test, 2))
