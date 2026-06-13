# https://prog4fun.csse.canterbury.ac.nz/mod/quiz/attempt.php?attempt=11308&cmid=5961&page=2&mdlscrollto=200

n, t = input().split()
t = t.lower()

count = 0
i = 0
output = []

while i < (int(n)):
    bird = input().lower()

    if bird == "end":
        i += 1
        output.append(count)
        count = 0
    elif bird == t:
        count += 1

print(*output)