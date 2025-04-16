# https://codeforces.com/problemset/problem/236/A

username = set(input().replace("", ""))

if len(username) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
