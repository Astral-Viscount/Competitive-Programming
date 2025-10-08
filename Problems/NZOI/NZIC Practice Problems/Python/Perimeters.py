# https://train.nzoi.org.nz/problems/777

x_cord = input()
y_cord = input()

cords = list(map(int, x_cord.split() + y_cord.split()))

"""
Or,
cords = [int(x) for x in x_cord.split()]
cords.extend(int(y) for y in y_cord.split())
"""

vertical = cords[-1] - cords[1]
horizontal = cords[-2] - cords[0]

print((vertical * 2) + (horizontal * 2))
