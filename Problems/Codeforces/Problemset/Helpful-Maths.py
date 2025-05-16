# https://codeforces.com/problemset/problem/339/A

num = list(map(int, input().replace("+", "")))

num.sort()
amount = len(num)

if amount > 1:
    for i in range(amount - 1):
        print(f"{num[i]}+", end='')
    print(num[-1])
else:
    print(num[0])
