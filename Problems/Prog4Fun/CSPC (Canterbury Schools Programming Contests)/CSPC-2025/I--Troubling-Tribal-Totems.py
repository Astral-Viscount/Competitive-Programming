# https://prog4fun.csse.canterbury.ac.nz/mod/quiz/attempt.php?attempt=11308&cmid=5961&page=2#question-15609-9

n = int(input())

votes = {}

for _ in range(n):
    name = input()
    votes[name] = votes.get(name, 0) + 1

h = int(input())

for _ in range(h):
    totem = input()
    votes[totem] = 0

print(f"{max(votes, key=votes.get)}, the group has spoken.") 