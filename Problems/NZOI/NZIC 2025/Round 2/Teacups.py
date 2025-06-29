t = int(input())
cups = []
amount = {}

for _ in range(t):
    num = int(input())
    cups.append(num)
    if num in amount:
        amount[num] += 1
    else:
        amount[num] = 1

pair = []
remain = []

for i in sorted(amount):
    count = amount[i]

    for _ in range(count // 2):
        pair.append(str(i))
        pair.append(str(i))

    if count % 2 == 1:
        remain.append(str(i))

print(f'Shelf 1: {" ".join(pair)}')
print(f'Shelf 2: {" ".join(remain)}')
