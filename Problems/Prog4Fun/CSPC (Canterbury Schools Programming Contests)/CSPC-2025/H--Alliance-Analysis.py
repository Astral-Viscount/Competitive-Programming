# https://prog4fun.csse.canterbury.ac.nz/mod/quiz/attempt.php?attempt=11308&cmid=5961&page=2&mdlscrollto=1800

v = int(input())

votes = []

for _ in range(v):
    votes.append(input())

print(len(set(votes)))