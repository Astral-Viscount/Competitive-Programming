# https://train.nzoi.org.nz/problems/851

n = int(input())

words = []

for _ in range(n):
    words.append(input())

character = input()

for i in range(n):
    print(words[i].count(character))
