# https://codeforces.com/contest/2094/problem/A

t = int(input())

sentence = []

for _ in range(t):
    sentence.append(input().split())

for i in range(len(sentence)):
    word = sentence[i]
    for j in range(len(word)):
        letter = word[j]
        print(letter[0], end='')
    print()
