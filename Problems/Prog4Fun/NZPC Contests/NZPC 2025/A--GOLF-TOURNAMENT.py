# https://prog4fun.csse.canterbury.ac.nz/mod/quiz/attempt.php?attempt=11316&cmid=5965

golfers = {}

while True:    

    name, h, s = input().split()

    if name == "X":
        break

    h = int(h)
    s = int(s)

    golfers[name] = golfers.get(name, 0) + (s - h)

sorted_golfers = sorted(golfers.items(), key=lambda x: x[1])

for key, value in sorted_golfers:
    print(f"{key} {value}")
