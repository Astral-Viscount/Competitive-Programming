# https://prog4fun.csse.canterbury.ac.nz/mod/quiz/attempt.php?attempt=9684&cmid=4328&page=3

while True:
    a, b = map(int, input().split())
    
    if (a or b) != 0:
        print(a * b)
    else:
        break
    