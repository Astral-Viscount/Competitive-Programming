# https://orac2.info/problem/1464/

n = int(input())
word = list(input())


if word[0] == "?":
    word[0] = word[1]
else:
    for i in range(1, n):
        if word[i] == "?":
            word[i] = word[i - 1]

score = 0

for i in range(n - 1):
    if word[i] == word[i + 1]:
        score += 1

print(score)
