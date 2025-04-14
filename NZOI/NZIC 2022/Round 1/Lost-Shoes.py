# https://train.nzoi.org.nz/problems/1229

shoes = sorted(list(input().strip()))

color = []

for shoe in shoes:
    pair = shoes.count(shoe) % 2
    if pair != 0:
        color.append(shoe)
        shoes = [i for i in shoes if i != shoe]
    else:
        shoes = [i for i in shoes if i != shoe]

print(color)

