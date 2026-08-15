#

q = int(input())
n = int(input())

results = []

for _ in  range(n):
    stuff = input().split()

    name = stuff[0]

    for jump in stuff[1::]:
        if jump.isdigit():
            if int(jump) >= q:
                results.append(name)
                break

if results:
    for res in results:
        print(res)
else:
    print("Nobody qualifies!")
    