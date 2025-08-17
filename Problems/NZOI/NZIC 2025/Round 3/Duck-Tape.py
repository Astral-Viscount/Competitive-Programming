# https://train.nzoi.org.nz/problems/1522

n, s, e = map(int, input().split())
tapes = [tuple(map(int, input().split())) for _ in range(n)]

tapes.sort()

current = s
index = 0
cover = False
total = len(tapes)

while current <= e:
    
    best = current - 1
    
    new = False
    
    while index < total and tapes[index][0] <= current:

        if tapes[index][1] > best:
            best = tapes[index][1]

        index += 1
        new = True
    
    if best < current:
        cover = False
        break

    current = best + 1
    
    if best >= e:
        cover = True
        break

if cover:
    print(1)
else:
    print(0)
