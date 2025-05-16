# https://train.nzoi.org.nz/problems/1144

n = int(input())
school = sorted(list(map(int, input().split())))
competitor = sorted(list(map(int, input().split())))

win = 0
index = 0

for player in school:
    if index < n and player > competitor[index]:
        win += 1
        index += 1

print(win)
