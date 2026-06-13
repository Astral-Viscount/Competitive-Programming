# https://prog4fun.csse.canterbury.ac.nz/mod/quiz/attempt.php?attempt=11313&cmid=1851&page=8

demerit = { "TT": 75,
            "TX": 50,
            "PR": 80,
            "RT": 30,
            "AP": 25,
            "PX": 60
}

while True:

    w, n = map(int, input().split())

    if w == 0:
        break

    students = {}

    for _ in range(n):
        name, code = input().split()

        students[name] = students.get(name, 0) + demerit[code]
    
    bad_students = []
    for student_name, student_point in students.items():
            if student_point >= 100:
                bad_students.append(student_name)

    if bad_students:
        print(f"Week {w} {', '.join(bad_students)}")
    else:
        print(f"Week {w} No phones confiscated")
