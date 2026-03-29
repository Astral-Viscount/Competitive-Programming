# https://train.nzoi.org.nz/problems/1562

m , p = map(int, input().split())

mathematicians = []

for _ in range(m):
    a , b = map(int, input().split())
    mathematicians.append((a, b))

physicists = []

for _ in range(p):
    a , b = map(int, input().split())
    physicists.append((a, b))

mathematicians.sort()
physicists.sort()

years = 0

math_pointer = 0
phys_pointer = 0

while math_pointer < m and phys_pointer < p:

    math_born, math_death = mathematicians[math_pointer]
    phys_born, phys_death = physicists[phys_pointer]

    alive_together = min(math_death, phys_death) - max(math_born, phys_born) + 1

    if alive_together > 0:
        years = max(years, alive_together)

    if math_death < phys_death:
        math_pointer += 1
    else:
        phys_pointer += 1

print(years)
