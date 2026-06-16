# https://prog4fun.csse.canterbury.ac.nz/mod/quiz/attempt.php?attempt=11316&cmid=5965&page=4

penalty = { "GDX" : 5, 
            "SNK" : 15, 
            "PRV" : 25, 
            "TWO" : 20, 
            "LNO" : 15, 
            "LRB" : 10}

students = {}

w = int(input())

while True:
    stuff = input().split()

    if stuff[0] == "END":
        break
    
    name, code = stuff[0], stuff[1]

    point = penalty.get(code, 0)
    students[name] = students.get(name, 0) + point

detention = []
meeting = []

for student, points in students.items():
    if 50 >= points > 30:
        detention.append(student)
    elif points > 50:
        meeting.append(student)

print(f"Week {w}")
print("Students for detention:")
print(*detention) if detention else print("None")
print("Parental meeting for:")
print(*meeting) if meeting else print("None")