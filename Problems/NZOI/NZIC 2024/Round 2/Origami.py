# https://train.nzoi.org.nz/problems/1327

x, y, a, b = map(int, input().split())

output = []

if a != b:
    output.append((x // a) * (y // b))
    output.append((x // b) * (y // a)) 
else:
    output.append((x // a) * (y // b))

print(max(output))
