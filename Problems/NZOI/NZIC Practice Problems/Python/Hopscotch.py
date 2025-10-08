# https://train.nzoi.org.nz/problems/800

num_stats = int(input())

stats = []

value = 'plausible'

for i in range(num_stats):
    i = input()
    stats.append(i)

for j in range(1, len(stats)):
    if (stats[j] == 'S' and stats[j-1] == 'E') or (stats[j] == 'N' and stats[j-1] == 'S') or (stats[j] == 'E' and stats[j-1] == 'E') or (stats[j] == 'N' and stats[j-1] == 'N'):
        value = 'impossible'

print(value)
