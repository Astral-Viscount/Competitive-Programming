# https://prog4fun.csse.canterbury.ac.nz/mod/quiz/attempt.php?attempt=11313&cmid=1851&page=7

house = {}

while True:
    taking = input()

    if taking == "END":
        break

    if taking == "0 0 0":
        continue

    stuff = taking.split()

    if not stuff[-1].isdigit():
        continue

    points = int(stuff[-1])
    house_name = stuff[1]

    house[house_name] = house.get(house_name, 0) + points

sorted_house = sorted(house.items(), key=lambda x: (x[1], x[0]))

rank = 4

for name, point in sorted_house:
    print(f"{rank} {name} {point}")
    rank -= 1

"""For unknown amount of houses

sorted_desc = sorted(house.items(), key=lambda i: i[1], reverse=True)

ranked_leaderboard = []
for rank, (key, value) in enumerate(sorted_desc, start=1):
    ranked_leaderboard.append((rank, key, value))

for rank, key, value in reversed(ranked_leaderboard):
    print(f"{rank} {key} {value}")

"""