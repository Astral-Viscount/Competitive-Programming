# https://prog4fun.csse.canterbury.ac.nz/mod/quiz/attempt.php?attempt=8737&cmid=4329&page=4

team = []
indexes = []
score = 0
index = -1
no_draw = True

for _ in range(8):
    team.append(input())

for _ in range(8):
    h, o = map(int, input().split())
    index += 1

    if h == 0 and o == 0:
        score += 2
    elif h == o:
        score += 3
        no_draw = False
        indexes.append(index)
    else:
        score += 1

print(f"Points scored: {score}")

if no_draw:
    print("No scoring draws")
else:
    for i in indexes:
        print(team[i])
