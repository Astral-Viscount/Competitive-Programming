# https://orac.amt.edu.au/problem/121/

t = int(input())

notes = 0

while t != 0:
    if t >= 100:
        t -= 100
        notes += 1
    elif t >= 20:
        t -= 20
        notes += 1
    elif t >= 5:
        t -= 5
        notes += 1
    elif t >= 1:
        t -= 1
        notes += 1
    
print(notes)