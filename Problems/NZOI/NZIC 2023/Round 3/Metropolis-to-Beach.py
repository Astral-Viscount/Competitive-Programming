# https://train.nzoi.org.nz/problems/1328

n = int(input())

elevation= []
max_elevation = []

for _ in range(n):
    elevation.append(int(input()))

for i in range(n - 1):
    if elevation[i] + 1 == elevation[i + 1]:
        max_elevation.append(elevation[i])
        




# diff = elevation[i] + elevation[i + 1]
#         if diff > max_elevation:
#             max_elevation = diff

print(elevation)
print(sum(set(max_elevation)))