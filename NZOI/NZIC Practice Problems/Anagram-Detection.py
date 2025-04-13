# https://train.nzoi.org.nz/problems/489

first_word = input()
second_word = input()

if sorted(first_word) == sorted(second_word):
    print("yes")
else:
    print("no")
