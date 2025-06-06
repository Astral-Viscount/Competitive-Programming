# https://prog4fun.csse.canterbury.ac.nz/mod/quiz/attempt.php?attempt=9684&cmid=4328&page=8

num_lines = int(input())

for _ in range(num_lines):
    code = input().strip()
    decode = 0
    
    for i, ch in enumerate(reversed(code)):
        if ch == '*':
            decode += 2 ** i

    print(decode)