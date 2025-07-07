# https://codeforces.com/problemset/problem/96/A

players = list(input())

count = 0
p = None

for player in players:
    
    if player != p:
        p = player
        count = 0
    else:
        count += 1
        if count >= 6:
            print("YES")
            break
else:
    print("NO")

