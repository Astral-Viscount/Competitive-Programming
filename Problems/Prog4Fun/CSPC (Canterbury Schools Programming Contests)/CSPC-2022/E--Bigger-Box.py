# https://prog4fun.csse.canterbury.ac.nz/mod/quiz/attempt.php?attempt=9723&cmid=2793&page=4https://prog4fun.csse.canterbury.ac.nz/mod/quiz/attempt.php?attempt=9723&cmid=2793&page=4

wc, bc, hc =  map(int, input().split())

volume_c = wc * bc * hc

while True:
    w, b, h = input().split()

    if w == "#":
        break

    volume = int(w) * int(b) * int(h)

    if volume > volume_c:
        print("Bigger")
    else:
        print("Smaller")
