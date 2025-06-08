# https://prog4fun.csse.canterbury.ac.nz/mod/quiz/attempt.php?attempt=9722&cmid=3199&page=6

count = 0

while True:
    w, m = input().split()
    
    if w == "#":
        break
    elif w == m[::-1]:
        count+=1
print(count)
