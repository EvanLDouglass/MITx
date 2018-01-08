# Evan Douglass

# This program takes a credit card balance and annual interest rate and
# calculates the balance after 12 months assuming only the minimum payment
# is made.

# Establish constants
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

# calculate monthly interest
monthlyInterestRate = annualInterestRate / 12


# find minimum payment function
def minMonthlyPayment(balance, min_perc):
    '''
    balance: float - balance in the account for payment period.
    min_perc: float - percentage of balance required for minimum payment.

    returns the minimum payment required for the month as a float.
    '''
    return balance * min_perc


# find new balance function
def newBalance(unpaid, interest):
    '''
    unpaid: float - the unpaid balance on an account.
    interest: float - the monthly interest rate.

    returns the new balance on the account as a float.
    '''
    return unpaid + unpaid * interest


# calculate the account balance each month for 12 months
for month in range(12):
    balance = newBalance(balance, monthlyInterestRate)
    payment = minMonthlyPayment(balance, monthlyPaymentRate)
    balance -= payment

# report year end results
print('Remaining balance:', round(balance, 2))
