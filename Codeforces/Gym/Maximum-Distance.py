# https://codeforces.com/gym/102951/problem/A

num = int(input())
x_cord = list(map(int, input().split()))
y_cord = list(map(int, input().split()))

distance = 0

for i in range(num):
    for j in range (i + 1):
        distance = max(((x_cord[i] - x_cord[j]) ** 2) + ((y_cord[i] - y_cord[j]) ** 2), distance)

print(distance)
