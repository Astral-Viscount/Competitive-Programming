n = int(input())
a = list(input())
b = list(input())

swaps = 0

for i in range(n):
    if a[i] != b [i]:
        swaps += 1

print(swaps - 1)