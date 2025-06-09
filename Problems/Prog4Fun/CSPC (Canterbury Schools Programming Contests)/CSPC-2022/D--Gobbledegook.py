# https://prog4fun.csse.canterbury.ac.nz/mod/quiz/attempt.php?attempt=9723&cmid=2793&page=3

a, b = input().split()
n = int(input())

for _ in range(n):
    word = input()
    
    fixed = ""

    for letter in word:
        if letter == a:
            fixed += b
        elif letter == b:
            fixed += a
        else:
            fixed += letter

    print(fixed)
