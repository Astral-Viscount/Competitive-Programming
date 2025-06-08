# https://prog4fun.csse.canterbury.ac.nz/mod/quiz/attempt.php?attempt=9722&cmid=3199&page=7

""" Fisrt Solution
x, y, z = map(int, input().split())
p = int(input())

ports = {}
best = float('inf')

for _ in range(p):
    name, px, py, pz, port = input().split()
    
    px = int(px)
    py = int(py)
    pz = int(pz)
    
    if port == "True":
        dis = (((px - x)**2) + ((py - y)**2) + ((pz - z)**2)) ** 0.5
        if dis < best:
            best = dis
            ports[name] = (px, py, pz)

last_item = ports.popitem()

values = []
for i in last_item:
    values.append(i)

output = []
output.append(values[0])
for j in values[1]:
    output.append(j)

for k in output:
    print(k, end=" ")
"""

# Refined Final and Better Code

x, y, z = map(int, input().split())
p = int(input())

best = float('inf')
best_planet = ""
best_coords = ()

for _ in range(p):
    name, px, py, pz, port = input().split()
    px, py, pz = int(px), int(py), int(pz)

    if port == "True":
        dis = ((px - x) ** 2 + (py - y) ** 2 + (pz - z) ** 2) ** 0.5
        if dis < best:
            best = dis
            best_planet = name
            best_coords = (px, py, pz)

print(best_planet, best_coords[0], best_coords[1], best_coords[2])
