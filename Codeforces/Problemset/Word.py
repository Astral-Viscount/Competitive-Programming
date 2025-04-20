# https://codeforces.com/problemset/problem/59/A

word = input()

upper = 0
lower = 0

for letter in word:
    if letter.isupper():
        upper += 1
    else:
        lower += 1

if upper > lower:
    print(word.upper())
else:
    print(word.lower())
