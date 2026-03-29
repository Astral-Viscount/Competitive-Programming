# https://train.nzoi.org.nz/problems/1680

n = int(input())

votes = {}

for _ in range(n):
    vote = input()
    if vote in votes:
        votes[vote] += 1
    else:
        votes[vote] = 1

max_vote = max(votes.values())
max_places = [place for place, count in votes.items() if count == max_vote]

if len(max_places) > 1:
    print("It's a tie.")
else:
    print(f"{max_places[0]} wins.")
