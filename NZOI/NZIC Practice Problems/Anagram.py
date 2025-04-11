# https://train.nzoi.org.nz/problems/489

first_word = input()
second_word = input()

count = 0

for letter in first_word:
    if letter in second_word:
        count  += 1

if count >= len(first_word):
    print("yes")
else:
    print("no")
