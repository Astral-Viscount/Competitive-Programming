# https://codeforces.com/problemset/problem/1374/B

t = int(input())

for _ in range(t):
    num = int(input())

    counter = 0
    while num != 1:

        if num % 6 == 0:
            divide = num / 6
            num = divide
            counter += 1
        else:
            num *= 2
            counter += 1

    print(counter)