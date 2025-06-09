# https://prog4fun.csse.canterbury.ac.nz/mod/quiz/attempt.php?attempt=9723&cmid=2793&page=5

values = {
    "walking": 1,
    "running": 2,
    "swimming": 3,
    "cycling": 2,
    "yoga": 1,
    "weights": 3
}

scores = {}

while True:
    name, exercise, time = input().split()

    if name == "#":
        break

    score = int(time) * values[exercise]
    
    if name in scores:
        scores[name] += score
    else:
        scores[name] = score

best = max(scores, key=scores.get)
highest = scores[best] #max(scores.values())

print(f"{best} scored the highest with {highest} points.")
