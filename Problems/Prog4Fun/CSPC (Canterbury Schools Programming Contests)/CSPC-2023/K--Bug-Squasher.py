# https://prog4fun.csse.canterbury.ac.nz/mod/quiz/attempt.php?attempt=9722&cmid=3199&page=11

points = {
    "Easy": 2,
    "Medium": 5,
    "Hard": 12
}

people = {}

while True:
    values = list(input().split())

    name = values[0]
    bugs = values[1:]

    if name == "#":
        break

    point = 0
    for bug in bugs:
        point += points[bug]

    if name not in people:
        people[name] = point
    
    else:
        people[name] += point

max_value = max(people.values())
best = []

for key, value in people.items():
    if value == max_value:
        best.append(key)

# I am proud of this even though it's not the most efficient way to output
if len(best) > 1:
    print("Employees of the month are ", end="")
    for i in best[0:(len(best) - 1)]:
        print(i, end=", ")
    print(f"{best[-1]}.")
else:
    print(f"Employee of the month is {best[0]}.")
