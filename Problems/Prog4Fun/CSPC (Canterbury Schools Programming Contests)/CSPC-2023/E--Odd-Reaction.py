# https://prog4fun.csse.canterbury.ac.nz/mod/quiz/attempt.php?attempt=9722&cmid=3199&page=5

while True:
    n = int(input())
    
    if n == -1:
        break
    elif n % 2 == 0:
        print(n)
    else:
        print(n+1)
