# Evan Douglass

# This program is a number guessing game that uses bisection search

import time

# initialize game
low = 0
high = 100

print('Please think of a number between 0 and 100!')
time.sleep(0.5) # pause for 0.5 second

# guess function returns the average of low and high
def guess(low, high):
    return (low + high) // 2

# repeatedly guess and check
while True:
    g = guess(low, high)
    print('Is your secret number', str(g) + '?')
    command = input("""Enter 'h' to indicate the guess is too high.
    Enter 'l' to indicate the guess is too low.
    Enter 'c' to indicate I guessed correctly. --> """)
    print()

    if command == 'c':
        print('Game over. Your secret number was:', g)
        break
    elif command == 'h':
        high = g
    elif command == 'l':
        low = g
    else:
        print('Sorry, I did not understand your input')
        print()
