# https://prog4fun.csse.canterbury.ac.nz/mod/quiz/attempt.php?attempt=9722&cmid=3199&page=10

n = int(input())

num = map(int, input().split())

if len(set(num)) == n:
    print("distinct")
else:
    print("contains duplicates")
