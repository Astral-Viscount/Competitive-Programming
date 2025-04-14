# https://codeforces.com/problemset/problem/71/A

n = int(input())

word = []

for _ in range(n):
    word.append(input().split())

for i in range(len(word)):
    letter = word[i][0]
    if len(letter) > 10:
        print(f"{letter[0]}{len(letter) - 2}{letter[-1]}")
    else:
        print(letter)
