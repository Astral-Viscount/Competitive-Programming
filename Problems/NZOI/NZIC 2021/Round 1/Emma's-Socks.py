# https://train.nzoi.org.nz/problems/1213

socks = {'Red': 0, 'Blue': 0, 'Pink': 0, 'Purple': 0}

for i in range(7):
    color = input()
    socks[color] = socks[color] + 1


for key, value in socks.items():
    if value == 1:
        print(key)
