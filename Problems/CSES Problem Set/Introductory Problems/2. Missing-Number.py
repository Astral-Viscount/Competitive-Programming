# https://cses.fi/problemset/task/1083

n = int(input())
num = sorted(list(map(int, input().split())))

for i in range(1, n + 1):
    try:
        if i != num[i - 1]:
            print(i)
            break
    except IndexError:
        print(n)
