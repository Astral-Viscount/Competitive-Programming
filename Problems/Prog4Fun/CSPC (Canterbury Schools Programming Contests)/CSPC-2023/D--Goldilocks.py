# https://prog4fun.csse.canterbury.ac.nz/mod/quiz/attempt.php?attempt=9722&cmid=3199&page=4

while True:
    t = int(input())
    if t == -1:
        break
    elif t < 34:
        print("too cold")
    elif t > 42:
        print("too hot")
    else:
        print("just right")
