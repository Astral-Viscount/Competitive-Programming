# https://prog4fun.csse.canterbury.ac.nz/mod/quiz/attempt.php?attempt=11308&cmid=5961&page=1&mdlscrollto=1562.4000244140625

best_name = ""
best_score = 0

while True:
    name, score = input().split()
    if name == "#":
        break
    else:
        score = int(score)
        if score > best_score:
            best_score = score
            best_name = name

print(best_name)

"""
students = {}

while True:
    name, score = input().split()
    if name == "#":
        break
    else:
        score = int(score)
        students[name] = score

print(f"{max(students, key=students.get)}")
"""