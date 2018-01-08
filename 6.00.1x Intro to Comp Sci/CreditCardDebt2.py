# Evan Douglass

# This program calculates the minimum fixed monthly payment
# (as a multiple of ten) that will pay off a given debt in
# less than one year.

# initialize values
balance = 3926
annualInterestRate = 0.2

# monthly interest rate
monthlyRate = annualInterestRate / 12.0


def findEndBalance(balance, monthlyRate, payment):
    '''
    balance (float or int): Original balance in account.
    monthlyRate (float): Monthly interest rate.
    payment (int): Monthly payment. Assumes multiples of 10.

    returns the ending balance after 12 months as a float or int.
    '''
    test_balance = balance
    for month in range(12):
        test_balance -= payment
        test_balance += (test_balance * monthlyRate)
    return test_balance


# increment test values for payment until findEndBalance returns negative
test = 0
while round(findEndBalance(balance, monthlyRate, test), 2) > 0:
    test += 10

print('Lowest Payment:', test)
