# https://codeforces.com/problemset/problem/835/A

s, v1, v2, t1, t2 = map(int, input().split())

first = (t1 * 2) + (v1 * s)
second = (t2 * 2) + (v2 * s)

if first < second:
    print("First")
elif second < first:
    print("Second")
else:
    print("Friendship")
