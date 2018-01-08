s = input()

current = s[0]
longest = s[0]

for letter in s[1:]:
    if letter >= current[-1]:
        current += letter
        if len(current) > len(longest):
            longest = current
    else:
        current = letter

print('Longest substring in alphabetical order is:', longest)
