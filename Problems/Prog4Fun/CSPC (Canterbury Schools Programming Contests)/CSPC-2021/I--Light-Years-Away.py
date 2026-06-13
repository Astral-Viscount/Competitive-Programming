# https://prog4fun.csse.canterbury.ac.nz/mod/quiz/attempt.php?attempt=11313&cmid=1851&page=9

import math

n = int(input())

for _ in range(n):
    stuff = input().split()
    planet = stuff[0]
    x, y, z = map(int, stuff[1::])

    if math.sqrt(pow(x, 2) + pow(y, 2) + pow(z, 2)) < 1000:
        print(f"{planet} is in range")
    else:
        print(f"{planet} is out of range")
